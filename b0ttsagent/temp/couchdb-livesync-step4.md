# Step 4 — Run LiveSync's couchdb-init.sh (CORS + auth config)

# The script reads hostname / username / password from the environment.
# We source .env so the password never appears on the command line (ps-safe).
source <(sudo cat /home/couchdb/.env)
export hostname="http://localhost:5984"
export username="${COUCHDB_USER}"
export password="${COUCHDB_PASSWORD}"

curl -s https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/main/utils/couchdb/couchdb-init.sh | bash

unset hostname username password COUCHDB_USER COUCHDB_PASSWORD

# --- Verify CORS got configured correctly ---
source <(sudo cat /home/couchdb/.env)
echo "cors/origins:"
curl -s -u "${COUCHDB_USER}:${COUCHDB_PASSWORD}" http://localhost:5984/_node/_local/_config/cors/origins
echo ""
echo "httpd/enable_cors:"
curl -s -u "${COUCHDB_USER}:${COUCHDB_PASSWORD}" http://localhost:5984/_node/_local/_config/httpd/enable_cors
echo ""
unset COUCHDB_USER COUCHDB_PASSWORD
