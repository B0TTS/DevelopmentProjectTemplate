# Setup

## Bootstrap

### Quick SCaffold

**1. Scaffold the project with the template installer:**

```bash
npx @b0tts/template-dev-installer@latest
```

### Setup Agent Harnesses

**1. Create a renamed backup of your agent files (.pi, .opencode)**
 
**2. Install your agent repos from scratch to local project**

```
  git submodule update --init --recursive
```

**3. Install whatever plugins, skills, etc**

 - Go through your backed up agent files, and add copy over your skills per harness.

**4. Delete your backup agent file**

- You dont need it anymore just adds context bloat.

### Setup Main Git File

**1. Delete Sub modules:**

Disconnect/Delete any sub modules you don't need anymore.

**2. Cleanup gitignore**

Make sure youre tracking all the files you wanna track for the project.

### opencode MCPs

**1. Roblox Studio MCP** (read-only inspector) — browse the live place file from AI. Add to `.opencode/opencode.json`:

```json
"mcp": {
  "robloxstudio": {
    "type": "local",
    "command": ["npx", "-y", "robloxstudio-mcp-inspector@latest"],
    "enabled": true,
    "timeout": 30000
  }
}
```

**1.1 - Requirements:** Enable `HTTP Requests` in Roblox Studio (`File > Game Settings > Security`).

**2. Context7 MCP** — Roblox/Luau documentation lookups. Add to `.opencode/opencode.json`:

```json
"mcp": {
    "context7": {
      "type": "remote",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "{env:CONTEXT7_API_KEY}"
      },
      "enabled": true
    }
}
```

Then set the env var: `export CONTEXT7_API_KEY=ctx7sk-...`

**3. SearXNG MCP** — web search via the self-hosted VPS instance. Add to `.opencode/opencode.json`:

```json
"mcp": {
  "searxng": {
    "type": "local",
    "command": ["node", ".searxng-mcp/dist/cli.js"],
    "cwd": ".searxng-mcp",
    "environment": {
      "SEARXNG_URL": "http://100.122.184.37:8082"
    },
    "enabled": true
  }
}
```

**3.1 - Prerequisites:** `.searxng-mcp` is a git submodule (already pulled by the harness setup step) but `dist/` is gitignored, so build it first:

```bash
cd .searxng-mcp && npm run bootstrap
```

**3.2 - Requirements:** You must be on the Tailnet (or VPN) to reach the VPS searxng instance at `http://100.122.184.37:8082`. Verify it loaded by checking for the `searxng_instance_info` tool in opencode.

## Docker

**1. Create and start the Docker workspace:**

   ```bash
docker run -it \
  --name project_name \
  -v "C:\_Project_Directory:/workspace" \
  -w /workspace \
  -p 58741:58741 \
  -p 2222:22 \
  alpine:latest
   ```

(Flatten that to a single line using an AI chat or Docker Gordon, then run it.)

**2. Enter the container:**

```bash
docker exec -it project_name sh
```

**2.1 Find your container** (if you forgot the name):

```bash
docker ps
```

### Install Dependencies

**1. Node.js:**

```bash
apk add nodejs npm
```

**2. Git:**

```bash
apk add git
```

### OpenSSH (Remote Access)

**1. Install OpenSSH server:**

```bash
apk add openssh-server
```

**2. Generate host keys:**

```bash
ssh-keygen -A
```

**3. Enable root login with password — append to `/etc/ssh/sshd_config`:**

```bash
echo -e "PermitRootLogin yes\nPasswordAuthentication yes" >> /etc/ssh/sshd_config
```

**4. Set root password:**

```bash
passwd root
```

**5. Start SSH server:**

```bash
/usr/sbin/sshd
```

### Auto-Start SSH on Container Restart

After completing all setup above (dependencies, OpenSSH, tmux), save the container as an image so SSH auto-starts on future `docker start`:

**1. Exit the container:**

```bash
exit
```

**2. Save the container as an image:**

```bash
docker commit project_name project_name-image
```

**3. Remove the old container:**

```bash
docker stop project_name && docker rm project_name
```

**4. Run a new container from the saved image:**

```bash
docker run -it \
  --name project_name \
  -v "C:\_Project_Directory:/workspace" \
  -w /workspace \
  -p 58741:58741 \
  -p 2222:22 \
  --entrypoint sh \
  project_name-image \
  -c "/usr/sbin/sshd && exec sh"
```

(Flatten that to a single line using an AI chat or Docker Gordon, then run it.)

**Note:** If you install new packages later, re-run step 2 to update the image:

```bash
docker commit project_name project_name-image
```

### tmux + Termius (Persistent Sessions)

**1. Install tmux:**

```bash
apk add tmux
```

**2. Create a named session:**

```bash
tmux new-session -d -s main
```

**3. Auto-attach on login — append to `~/.profile`:**

```bash
if command -v tmux &>/dev/null && [ -z "$TMUX" ]; then
  tmux attach -t main 2>/dev/null || tmux new -s main
fi
```

(Flatten that to a single line using an AI chat or Docker Gordon, then run it.)

**4. Connect from Termius (phone):**

| Field    | Value                    |
| -------- | ------------------------ |
| Host     | Your Windows PC local IP |
| Port     | 2222                     |
| User     | root                     |
| Password | *(the one you set)*      |

Run `ipconfig` on Windows to find your local IP.

**5. Using tmux from phone:**

- `tmux ls` — list sessions
- `tmux attach -t main` — attach to session
- `Ctrl+B, D` — detach (keeps session running)

### tmux Rendering (OpenCode Fix)

OpenCode's TUI renders incorrectly inside tmux without proper terminfo and terminal color support. Fix this before committing the container image.

**1. Install ncurses:**

```bash
apk add ncurses ncurses-terminfo
```

**2. Add tmux config:**

```bash
echo 'set -g default-terminal "tmux-256color"' >> ~/.tmux.conf
echo 'set -ga terminal-overrides ",*:Tc"' >> ~/.tmux.conf
echo 'set -ga terminal-features ",*:RGB"' >> ~/.tmux.conf
```

**3. Restart tmux to apply:**

```bash
tmux kill-server
tmux new -s main
```


## GSD
Make sure to run this step for your docker instances

**1. Install GSD:**

```
npx @opengsd/gsd-core@latest
```

**2. Install GSD SDK globally**

```
npm install -g @gsd-build/sdk
```

**Note:** you can also just ask the model to do it, so you don't have to reinstall every session.

**3. Configure model overrides** — paste into `.opencode/opencode.json` under `"agent"`.
 - Checkout optimizing agents personal obsidian ai notes guide for help in setting up agent overrides for your personal pricing/strategy.
 - For other override strategies, see `Setup/Model Overrides/model-override-strategies.md`.


### Notifications

Push notifications via [ntfy.sh](https://ntfy.sh) when the AI finishes, needs permission, or errors.

**1.** Create a `plugins` folder inside `.opencode/` in your project.

**2.** Copy `Notifications.js` from `C:\Users\Jonah\.config\opencode\Plugins\Notifications.js` into `.opencode/plugins/`.

**3.** Update placeholders in `.opencode/plugins/Notifications.js`:

- Replace the ntfy topic URL with your own (get one at [ntfy.sh](https://ntfy.sh)).
- Replace `project_name` in the title strings.

**4.** Subscribe — install the ntfy app ([Android](https://play.google.com/store/apps/details?id=io.heckel.ntfy) / [iOS](https://apps.apple.com/app/ntfy/id1625396347)) and subscribe to your topic.

### Cleanup

**Remove a specific project:**

```bash
docker stop project_name && docker rm project_name
docker rmi project_name-image
```

**Remove all unused images and containers:**

```bash
docker system prune
```

</instructions>