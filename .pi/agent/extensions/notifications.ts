/**
 * Pi Notifications Extension
 *
 * Sends an ntfy push notification (phone/desktop) when Pi finishes a run and
 * is waiting for input. Works in ALL Pi modes (tui/rpc/json/print), including
 * headless — unlike Pi's built-in terminal notify.ts, which only fires in a
 * terminal via OSC/Windows-toast.
 *
 * Ported from the OpenCode Notifications.js plugin. Of OpenCode's four
 * events, only `session.idle` maps cleanly to Pi:
 *
 *   OpenCode event       Pi equivalent        Status
 *   --------------------------------------------------------------------
 *   session.idle         agent_settled        wired below
 *   session.error        (no equivalent)      skipped — Pi emits no
 *                                             session-level error event;
 *                                             closest signals are
 *                                             after_provider_response (bad
 *                                             HTTP) / tool_result isError,
 *                                             both too noisy to buzz on
 *   permission.asked     (no equivalent)      skipped — Pi has no built-in
 *                                             permission popup; would need a
 *                                             tool_call gate (see Pi's
 *                                             permission-gate.ts example)
 *   question.asked       (no equivalent)      skipped — Pi has no built-in
 *                                             question flow; questions are
 *                                             custom tools (see question.ts)
 *
 * Add the skipped ones later by registering extra pi.on(...) handlers.
 *
 * Config: reads from env vars when present, otherwise falls back to the
 * defaults below so it works out of the box. To externalize credentials
 * (recommended — keeps them out of this file), set:
 *   NTFY_USE_CLOUD="true"        switch to the public ntfy.sh backend
 *   NTFY_BASE_URL                self-hosted base URL
 *   NTFY_TOPIC                   topic name
 *   NTFY_AUTH                    base64 of "user:password"
 */

import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { basename } from "node:path";

const SELF_HOSTED = {
  baseUrl: process.env.NTFY_BASE_URL ?? "https://vmi3326176.tailf94009.ts.net:3000",
  topic: process.env.NTFY_TOPIC ?? "DevelopmentMain",
  auth: process.env.NTFY_AUTH ?? Buffer.from("admin:2121400488").toString("base64"),
};

const CLOUD = {
  baseUrl: "https://ntfy.sh",
  topic: process.env.NTFY_TOPIC ?? "DevelopmentMain_JJNtP3cuYprP62DE",
  auth: "", // public cloud topic is unauthenticated
};

const active = process.env.NTFY_USE_CLOUD === "true" ? CLOUD : SELF_HOSTED;

export default function (pi: ExtensionAPI) {
  const send = async (
    title: string,
    body: string,
    priority: string = "default",
    tags: string = "robot",
  ) => {
    try {
      const headers: Record<string, string> = {
        Title: title,
        Priority: priority,
        Tags: tags,
      };
      if (active.auth) headers.Authorization = `Basic ${active.auth}`;

      await fetch(`${active.baseUrl}/${active.topic}`, {
        method: "POST",
        body,
        headers,
      });
    } catch (err) {
      // A failed notification must never crash the agent, but surface it for debugging.
      console.error("[notifications] send failed:", err);
    }
  };

  // DIAGNOSTIC: proves the extension loaded + ntfy works on every session start.
  // If you get this buzz but not "Response ready", the issue is agent_settled.
  // Remove this handler once confirmed working.
  pi.on("session_start", async (_event, ctx) => {
    const project = basename(ctx.cwd);
    await send(`Pi - ${project}`, "Extension loaded (session_start)");
  });

  // "Response ready" — fires once when Pi will not continue automatically
  // (retries, auto-compaction, queued follow-ups all done). Using
  // agent_settled instead of agent_end avoids duplicate buzzes on retry.
  pi.on("agent_settled", async (_event, ctx) => {
    const project = basename(ctx.cwd);
    await send(`Pi - ${project}`, "Response ready (agent_settled)");
  });
}
