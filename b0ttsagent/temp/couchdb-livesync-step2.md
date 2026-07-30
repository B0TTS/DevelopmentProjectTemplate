# Step 2 — Write CouchDB `.env` + `docker-compose.yml` on the VPS

> Run this whole block on the VPS over SSH. No secrets are written into any repo
> file — the admin password is generated on the VPS with `openssl rand` and shown
> once so you can save it to your password manager.

```bash
cd /home/couchdb

# 1) Generate a strong admin password (lives ONLY in /home/couchdb/.env + your password manager)
COUCHDB_PASS="$(openssl rand -base64 24)"

# 2) Write .env  (sudo tee because /home/couchdb is owned by the couchdb user)
cat <<EOF | sudo tee /home/couchdb/.env > /dev/null
COUCHDB_USER=admin
COUCHDB_PASSWORD=${COUCHDB_PASS}
EOF
sudo chmod 600 /home/couchdb/.env
sudo chown couchdb:couchdb /home/couchdb/.env
unset COUCHDB_PASS

# 3) Write docker-compose.yml
cat <<'EOF' | sudo tee /home/couchdb/docker-compose.yml > /dev/null
services:
  couchdb:
    image: couchdb:3.5.2
    container_name: couchdb
    user: "5984:5984"
    restart: unless-stopped
    environment:
      - COUCHDB_USER=${COUCHDB_USER}
      - COUCHDB_PASSWORD=${COUCHDB_PASSWORD}
    volumes:
      - ./couchdb-data:/opt/couchdb/data
      - ./couchdb-etc:/opt/couchdb/etc/local.d
    ports:
      - "127.0.0.1:5984:5984"
EOF
sudo chown couchdb:couchdb /home/couchdb/docker-compose.yml

# 4) Show the generated password ONCE — copy it to your password manager now
#    (label it: CouchDB admin / user "admin")
sudo cat /home/couchdb/.env
```

## What you should see

- `sudo cat /home/couchdb/.env` prints:
  ```
  COUCHDB_USER=admin
  COUCHDB_PASSWORD=<a long base64 string>
  ```
- No "permission denied" errors (we use `sudo tee` because `/home/couchdb` is owned by the `couchdb` user, not `deploy`).

## Verify

After running the block, optionally confirm both files landed and have correct ownership/perms:

```bash
sudo ls -la /home/couchdb
sudo cat /home/couchdb/docker-compose.yml
```

Expect:
- `.env` → `-rw-------` owned by `couchdb couchdb`
- `docker-compose.yml` → `-rw-r--r--` (or similar) owned by `couchdb couchdb`
- `docker-compose.yml` contents match the YAML above (image `couchdb:3.5.2`, `user: "5984:5984"`, `127.0.0.1:5984:5984`, the two volumes).

## Notes

- We do NOT start the container here — that's Step 3 (after `chown`-ing the data
  dirs to `5984:5984` so the container, which runs as uid 5984, can write to them).
- `127.0.0.1:5984:5984` binds CouchDB to localhost only — never public. Tailscale
  Serve will proxy it in a later step.
- Compose auto-loads `/home/couchdb/.env` when run from `/home/couchdb`, so the
  `${COUCHDB_USER}` / `${COUCHDB_PASSWORD}` in the YAML get substituted at runtime.
