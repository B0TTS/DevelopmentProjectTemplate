# Step 5 — Expose CouchDB over Tailscale Serve HTTPS on :3001

# 1) Add the HTTPS serve entry (tailnet-only, backgrounded)
sudo tailscale serve --https=3001 --bg http://localhost:5984

# 2) Confirm the new entry is listed
tailscale serve status
