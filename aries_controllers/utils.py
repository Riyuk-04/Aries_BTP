from flask import Flask
from flask import jsonify
import requests
import time
import json

    ##Creates and post public DID
    ##SAMPLE RESP : {'result': {'did': 'Hc4GRdjapBrCZf83ypqJGW', 'verkey': 'A3u7HykmMQdv1vsBqiTdMbZVdf6u2Sos4nNuMafMS5Kn', 'posture': 'posted', 'key_type': 'ed25519', 'method': 'sov'}}
def create_public_did(agent1_admin_port, steward_admin_port):
    url_create_did = "http://0.0.0.0:" + str(agent1_admin_port) + "/wallet/did/create"
    headers_create_did = {"accept": "application/json", "Content-Type": "application/json"}
    payload_create_did = {
        "method": "sov",
        "options": {
            "key_type": "ed25519"
        }
    }

    try:
        r_create_did = requests.post(url=url_create_did, json=payload_create_did, headers=headers_create_did)
        r_create_did = r_create_did.json()
    except requests.exceptions.HTTPError as errh:
        raise errh
    
    did  = r_create_did['result']['did']
    verkey = r_create_did['result']['verkey']

    url_reg_nym = "http://0.0.0.0:" + str(steward_admin_port) + "/ledger/register-nym?did=" + str(did) + "&verkey=" + str(verkey)
    headers_reg_nym = {"accept": "application/json"}
    payload_reg_nym = {}

    try:
        r_reg_nym = requests.post(url=url_reg_nym, json=payload_reg_nym, headers=headers_reg_nym)
        r_reg_nym = r_reg_nym.json()
    except requests.exceptions.HTTPError as errh:
        raise errh
    
    url_post_did = "http://0.0.0.0:" + str(agent1_admin_port) + "/wallet/did/public?did=" + str(did)
    headers_post_did = {"accept": "application/json"}
    payload_post_did = {}

    try:
        r_post_did = requests.post(url=url_post_did, json=payload_post_did, headers=headers_post_did)
        r_post_did = r_post_did.json()
    except requests.exceptions.HTTPError as errh:
        raise errh
    
    return r_post_did

def make_Connection(agent1_admin_port, steward_admin_port):
    url_create_inv = "http://0.0.0.0:" + str(steward_admin_port) + "/connections/create-invitation"
    headers_create_inv = {"accept": "application/json", "Content-Type": "application/json"}
    payload_create_inv = {}

    try:
        r_create_inv = requests.post(url=url_create_inv, json=payload_create_inv, headers=headers_create_inv)
        r_create_inv = r_create_inv.json()
    except requests.exceptions.HTTPError as errh:
        raise errh

    invitation = r_create_inv['invitation']
    steward_conn_id = r_create_inv['connection_id']

    url_rcv_inv = "http://0.0.0.0:" + str(agent1_admin_port) + "/connections/receive-invitation"
    headers_rcv_inv = {"accept": "application/json", "Content-Type": "application/json"}
    payload_rcv_inv = invitation

    try:
        r_rcv_inv = requests.post(url=url_rcv_inv, json=payload_rcv_inv, headers=headers_rcv_inv)
        r_rcv_inv = r_rcv_inv.json()
    except requests.exceptions.HTTPError as errh:
        raise errh
    
    alice_conn_id = r_rcv_inv['connection_id']
    print(steward_conn_id, alice_conn_id)


    url_accept_inv = "http://0.0.0.0:" + str(agent1_admin_port) + "/connections/" + str(alice_conn_id) + "/accept-invitation"
    headers_accept_inv = {"accept": "application/json"}
    payload_accept_inv = {}

    try:
        r_accept_inv = requests.post(url=url_accept_inv, json=payload_accept_inv, headers=headers_accept_inv)
        r_accept_inv = r_accept_inv.json()
    except requests.exceptions.HTTPError as errh:
        raise errh


    time.sleep(0.1)
    url_accept_req = "http://0.0.0.0:" + str(steward_admin_port) + "/connections/" + str(steward_conn_id) + "/accept-request"
    headers_accept_req = {"accept": "application/json"}
    payload_accept_req = {}

    try:
        r_accept_req = requests.post(url=url_accept_req, data=payload_accept_req, headers=headers_accept_req)
        r_accept_req = r_accept_req.json()
    except requests.exceptions.HTTPError as errh:
        raise errh
    
    return steward_conn_id, alice_conn_id

def gen_Schema(agent_admin_port, schema):
    url_schema = "http://0.0.0.0:" + str(agent_admin_port) + "/schemas"
    headers_schema = {"accept": "application/json", "Content-Type": "application/json"}
    payload_schema = str(schema)

    try:
        r_schema = requests.post(url=url_schema, data=payload_schema, headers=headers_schema)
        r_schema = r_schema.json()
    except requests.exceptions.HTTPError as errh:
        raise errh

    return r_schema

def gen_CredDef(agent_admin_port, credDef):
    url_CredDef = "http://0.0.0.0:" + str(agent_admin_port) + "/credential-definitions"
    headers_CredDef = {"accept": "application/json", "Content-Type": "application/json"}
    payload_CredDef = credDef
    try:
        r_CredDef = requests.post(url=url_CredDef, data=payload_CredDef, headers=headers_CredDef)
        r_CredDef = r_CredDef.json()
    except requests.exceptions.HTTPError as errh:
        raise errh

    return r_CredDef

if __name__ == "__main__":
    # print(create_public_did(9001, 8001))
    # print(make_Connection(9001, 8001))
    sample_schema = {
  "attributes": [
    "score"
  ],
  "schema_name": "prefs",
  "schema_version": "1.0"
}
    json_schema = json.dumps(sample_schema)
    # print(gen_Schema(8001, json_schema))

    sample_CredDef = {
  "revocation_registry_size": 1000,
  "schema_id": "Th7MpTaRZVRYnPiabds81Y:2:prefs2:1.0",
  "support_revocation": True,
  "tag": "default"
}
    json_CredDef = json.dumps(sample_CredDef)
    print(gen_CredDef(8001, json_CredDef))