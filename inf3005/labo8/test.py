import requests
import json
import sys

url = "http://localhost:5000"
endpoint = "/api/livre"

data = {
    "annee_pub": "2010-10-10",
    "auteur": "oliver",
    "nb_chapitres": 10,
    "nb_pages": 100,
    "titre": "james"
}

headers = {"Content-type": "application/json"}
full_url = url + endpoint

r = requests.post(full_url, data=json.dumps(data), headers=headers)
print "Status Code: %s" % r.status_code
print r.text
