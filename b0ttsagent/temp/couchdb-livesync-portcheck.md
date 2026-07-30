# Port conflict check — run BEFORE Step 2

# 1) All current Docker port mappings (the nav guide's standard conflict check)
sudo docker ps --format "table {{.Names}}\t{{.Ports}}"

# 2) Anything (Docker or not) already listening on 5984 (the CouchDB host bind)?
sudo ss -tlnp | grep 5984 || echo "5984 is FREE"

# 3) Current Tailscale Serve mappings — confirm 3001 is NOT already taken
tailscale serve status
