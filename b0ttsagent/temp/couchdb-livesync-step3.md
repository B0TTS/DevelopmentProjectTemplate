# Step 3 — chown data dirs to 5984:5984, start CouchDB, verify

# 1) Give the container (runs as internal uid 5984) write access to its data dirs.
#    Only the two data dirs — leave .env and docker-compose.yml owned by couchdb:couchdb.
sudo chown -R 5984:5984 /home/couchdb/couchdb-data /home/couchdb/couchdb-etc

# 2) Start CouchDB (sudo so compose can read the 600 .env owned by couchdb)
cd /home/couchdb && sudo docker compose up -d

# 3) Confirm it's running and healthy
sudo docker ps --filter name=couchdb

# 4) Hit the CouchDB welcome endpoint (localhost only — not exposed publicly)
curl http://localhost:5984

# 5) Sanity-check auth works with the creds from .env
source <(sudo cat /home/couchdb/.env)
curl -u "${COUCHDB_USER}:${COUCHDB_PASSWORD}" http://localhost:5984/_all_dbs
unset COUCHDB_USER COUCHDB_PASSWORD
