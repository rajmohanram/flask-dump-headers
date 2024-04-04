# Dump Request Headers to stdout

- flask run --debug

### cURL GET request
curl -s http://localhost:5000 -H 'Accept: application/json' -H 'X-Test: hello' | json_pp

OR

curl -s http://localhost:5000 -H 'Accept: application/json' -H 'X-Test: hello' | jq
