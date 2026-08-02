# Obsidian LiveSync Alternatives & Postgres Consolidation Research

**Date:** 07-18-2026
**Session scope:** Can we reroute LiveSync to use the existing VPS Postgres backend? → Broader survey of LiveSync alternatives.

---

## What was accomplished

Two rounds of deep research with GitHub source evidence:

### Round 1 — Can LiveSync use Postgres instead of CouchDB?

**Answer: No — not without forking the plugin.**

- Cloned and inspected the [`obsidian-livesync`](https://github.com/vrtmrz/obsidian-livesync) source (HEAD `e114f66`).
- LiveSync supports exactly 3 remote types, hardcoded: `REMOTE_COUCHDB`, `REMOTE_MINIO` (object storage), `REMOTE_P2P` (WebRTC). No Postgres.
- Source evidence:
  - [`ModuleReplicatorCouchDB.ts#L11-L15`](https://github.com/vrtmrz/obsidian-livesync/blob/e114f66fb2b7c6f3fec2d53701f6638d2557e606/src/modules/core/ModuleReplicatorCouchDB.ts#L11-L15) — literal comment: "If new remote types were added, add them here." Hardcoded if/else returns CouchDB replicator.
  - [`ModuleReplicatorMinIO.ts#L10-L12`](https://github.com/vrtmrz/obsidian-livesync/blob/e114f66fb2b7c6f3fec2d53701f6638d2557e606/src/modules/core/ModuleReplicatorMinIO.ts#L10-L12) — returns journal replicator for MinIO.
  - [`LiveSyncBaseCore.ts#L142-L144`](https://github.com/vrtmrz/obsidian-livesync/blob/e114f66fb2b7c6f3fec2d53701f6638d2557e606/src/LiveSyncBaseCore.ts#L142-L144) — only CouchDB + MinIO replicators registered.
  - Zero Postgres references in the entire codebase (only fly.io provisioning notes saying `<none>`).
- Maintainer stance ([Discussion #60](https://github.com/vrtmrz/obsidian-livesync/discussions/60)): "there is no other practicable backend now. CouchDB is a particular database that is very good at synchronization... With other databases, synchronization would have been harder (especially with over three devices)."
- **The one seam:** The object-storage path uses a journal-based replication model with a small `IJournalStorage` interface ([`JournalStorageAdapter.d.ts#L5-L12`](https://github.com/vrtmrz/obsidian-livesync/blob/e114f66fb2b7c6f3fec2d53701f6638d2557e606/_types/src/lib/src/replication/journal/objectstore/JournalStorageAdapter.d.ts#L5-L12)) — 7 methods, a key-value blob store trivially implementable on Postgres. A `PostgresStorageAdapter` is feasible, but requires **forking both `obsidian-livesync` and its `livesync-commonlib` submodule**, adding a new remote type, writing settings UI, and maintaining the fork forever.
- Alternative: `obsync-pg-plugin` (raw Postgres, v1.0.0, last commit 2026-02-01) — no E2E encryption, store plaintext in Postgres, not real-time bidirectional.

**Recommendation from Round 1:** Keep CouchDB. The Postgres stack serves a completely different workload (Roblox leaderboard). Consolidating saves one tiny container at a massive engineering or security cost.

### Round 2 — What about other LiveSync alternatives (broader survey)?

Cloned and inspected multiple repos and did web research. The big finding:

**Only LiveSync has true at-rest E2E encryption** (server physically cannot read notes). Every meaningful alternative either stores plaintext or only encrypts in transit.

| Alternative | At-rest E2E | Self-hosted | Real-time | Conflict model | Mobile | Maturity |
|---|---|---|---|---|---|---|
| **LiveSync** (current) | ✅ | ✅ | ✅ | CouchDB repl | ✅ Android+iOS | Battle-tested |
| **obsetync** | ❌ transport-only | ✅ Docker | ✅ WS | 3-way merge | iOS only | v1.9.4, brand-new public |
| **Syncline** | ❌ planned | ✅ CLI | ✅ WS | **CRDT (best)** | ✅ Android+iOS | New, not community-listed |
| **obsidian-crdt-sync** | ❌ | ✅ Docker | ✅ WS | Yjs CRDT | ✅ | Very new (1★) |
| **Remotely Save** | ⚠️ optional | ✅ S3/WebDAV | ❌ periodic | Basic (PRO=smart) | ✅ | Mature, popular |
| **obsidian-git** | ❌ | ✅ git host | ❌ manual | Git (mobile caveat) | ✅ | 11.5k★ |
| **Syncthing** | ⚠️ TLS P2P | ✅ P2P | ✅ file-level | Weak (.conflict) | ✅ Android | Mature |

**Top findings:**

1. **obsetync** (`Savemech/obsetync`, HEAD `49809fc`): Rust server, Docker, content-addressed (blake3 + FastCDC), Merkle tree, 3-way merge. BUT: iOS only (no Android), and *transport-only* encryption — server [decrypts requests](https://github.com/Savemech/obsetync/blob/49809fcfad7cd8060f0bc28d62d99e3d6a83fc4a/crates/sync-server/src/secure.rs#L135) and [stores plaintext blobs](https://github.com/Savemech/obsetync/blob/49809fcfad7cd8060f0bc28d62d99e3d6a83fc4a/crates/sync-core/src/content_store.rs#L88-L93). v1.9.4 with 11-file e2e test suite — mature code, brand-new public presence.

2. **Syncline** (`tomas789/syncline`): Rust + CRDT character-level merging — mathematically no conflicts ever. This is the strongest conflict resolution of ANY option, directly addressing the LiveSync maintainer's "3+ devices is hard" concern. Single SQLite file, WebSocket real-time, Android+iOS mobile. BUT: "E2E encryption planned but not yet implemented" — relies on TLS via reverse proxy. Not yet in Obsidian community plugin list.

3. **Remotely Save:** The *only* alternative with an optional-E2E story. File-level, periodic (not real-time), smart conflict = PRO. Can point at self-hosted MinIO/WebDAV on the VPS. Mature and popular but architecturally simpler than LiveSync.

---

## Current state

- **LiveSync is running** on the VPS (CouchDB 3.5.2 Docker, `127.0.0.1:5984`, Tailscale Serve `:3001` HTTPS). 2 of 3 devices synced (laptop + phone), PC backlogged.
- **Postgres 17 is running** on the VPS (postgrest stack, `postgrest-db` container, `appdb`, PgBouncer `:6432`, Cloudflare Tunnel → `b0tts.dev/api`). Used for a Roblox clan leaderboard — totally separate workload.
- **Vault is sensitive** — E2E encrypted (AES-GCM) + path obfuscation, 110 docs, NOT in git.
- Both current stacks are documented in navguides: `ObsidianLiveSyncNavGuide.md`, `PostgrestApiGuide.md`, `PgwebNavGuide.md`, `VpsNavGuide.md`.

**Open decisions:** None made yet. The user received both research answers but hasn't indicated whether to act on any recommendation or continue exploring.

---

## Key findings for the next session

### Paths available if the user wants to move off CouchDB

| Path | What it takes | What you lose | What you gain |
|---|---|---|---|
| **Keep LiveSync + CouchDB** | Zero work | Nothing | Nothing to fix |
| **Switch to Syncline** | Deploy Docker/CLI on VPS, install BRAT plugin on all devices, initial sync | At-rest E2E (plaintext SQLite) | CRDT zero-conflict sync, single-file backup, true mobile |
| **Switch to obsetync** | Deploy Docker on VPS, install plugin on all devices (iOS only!) | At-rest E2E, Android support | Content-addressed incremental sync, Merkle tree diff |
| **Add obsidian-git alongside LiveSync** | Set up git repo, install plugin | Nothing (complementary) | Version history + backup without touching LiveSync |
| **Switch to Remotely Save + MinIO on VPS** | Deploy MinIO container, configure plugin, initial sync | Real-time, chunk-level incremental | Optional E2E, simple, no fork needed |
| **Fork LiveSync + PostgresStorageAdapter** | ~1-2 days engineering, ongoing fork maintenance | Community updates, journal sync model (less tested) | True at-rest E2E on Postgres (chunks encrypted before adapter stores them) |

### Must-verify before any migration

1. **Phone OS:** The navguide doesn't specify iOS vs Android. If Android, obsetync is ruled out. Syncline and Remotely Save support both.
2. **E2E at-rest requirement:** The vault navguide flags "sensitive" — any move away from LiveSync means accepting plaintext-at-rest (or at best TLS-only transport) on the VPS. Is the user OK with relying on VPS filesystem security rather than cryptographic guarantees?
3. **CouchDB container resource usage:** If consolidation is the goal, is the CouchDB container actually using meaningful resources? (Likely not — CouchDB for 110 docs is tiny.)

---

## Suggested skills for the next session

- `librarian` — if deeper source investigation of any specific alternative is needed (e.g., digging into Syncline's encryption roadmap or obsetync's Android plans).
- `create-planning-docs` — if the user decides to pursue a migration path and wants formal CONTEXT.md → PLAN.md.
- `creative-brainstorm` — if the user wants to explore hybrid approaches (e.g., LiveSync + obsidian-git, or LiveSync + Remotely Save backup).
- `tutorial` — if the user wants a step-by-step walkthrough of deploying any of these alternatives on the VPS.

---

## Key files and paths

| Path | Content |
|---|---|
| `b0ttsagent/NavGuides/ObsidianLiveSyncNavGuide.md` | Current LiveSync/CouchDB setup |
| `b0ttsagent/NavGuides/PostgrestApiGuide.md` | Postgres 17 + PostgREST + PgBouncer setup |
| `b0ttsagent/NavGuides/PgwebNavGuide.md` | Decommissioned pgweb (port conflict note) |
| `b0ttsagent/NavGuides/VpsNavGuide.md` | VPS infrastructure overview |
| `C:/tmp/pi-github-repos/vrtmrz/obsidian-livesync/` | Cloned LiveSync repo (HEAD `e114f66`) |
| `C:/tmp/pi-github-repos/Savemech/obsetync/` | Cloned obsetync repo (HEAD `49809fc`, shallow) |
| `C:/tmp/pi-github-repos/dsnbyte/obsidian-supabase-sync/` | Cloned Supabase sync plugin repo |
| `C:/tmp/pi-github-repos/Vonshlovens/obsync-pg-plugin/` | Cloned obsync-pg repo (v1.0.0) |

### VPS access

Per navguides: `ssh deploy@vmi3326176.tailf94009.ts.net` (Tailscale). Docker compose for CouchDB at `/home/couchdb/`. Postgres stack at `/home/postgrest/`.

> **Never SSH into the VPS** per AGENTS.md rules. All VPS info comes from the navguides referenced above.

---

## What was NOT explored (candidates for next session)

- Syncline's E2E roadmap timeline (planned but no date in the README)
- obsetync's Android support plans (README says desktop + iOS; no Android roadmap visible)
- Actual resource usage comparison (CouchDB container vs Syncline server vs obsetync server)
- Whether the user's phone is iOS or Android (critical for obsetync viability)
- Hybrid approaches (e.g., keep LiveSync, add obsidian-git as backup layer)
- The decommissioned pgweb teardown and stale `:8443` Tailscale Serve entry (low-risk VPS cleanup)
