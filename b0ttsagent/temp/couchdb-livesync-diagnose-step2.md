# Diagnose Step 2 — are the files really there?

# Markers (echo) so we can tell if output is being eaten by the terminal.
echo "=== sanity: terminal shows output ==="
echo TEST-OUTPUT
pwd

echo "=== file byte counts ==="
sudo wc -c /home/couchdb/.env /home/couchdb/docker-compose.yml 2>&1

echo "=== dir listing (stderr merged) ==="
sudo ls -la /home/couchdb/ 2>&1

echo "=== .env contents ==="
sudo cat /home/couchdb/.env 2>&1

echo "=== compose contents ==="
sudo cat /home/couchdb/docker-compose.yml 2>&1

echo "=== END ==="
