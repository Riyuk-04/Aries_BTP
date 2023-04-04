from flask import Flask, jsonify
import requests
import time
import json

app = Flask(__name__)

@app.route('/create_public_did/<int:agent1_admin_port>/<int:steward_admin_port>', methods=['POST'])
def create_public_did_endpoint(agent1_admin_port, steward_admin_port):
    url_create_did = "http://127.0.0.1:" + str(agent1_admin_port) + "/wallet/did/create"
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
    except Exception as errh:
        print(errh)

    did = r_create_did['result']['did']
    verkey = r_create_did['result']['verkey']

    url_reg_nym = "http://127.0.0.1:" + str(steward_admin_port) + "/ledger/register-nym?did=" + str(
        did) + "&verkey=" + str(verkey)
    headers_reg_nym = {"accept": "application/json"}
    payload_reg_nym = {}

    try:
        r_reg_nym = requests.post(url=url_reg_nym, json=payload_reg_nym, headers=headers_reg_nym)
        r_reg_nym = r_reg_nym.json()
    except Exception as errh:
        print(errh)

    url_post_did = "http://127.0.0.1:" + str(agent1_admin_port) + "/wallet/did/public?did=" + str(did)
    headers_post_did = {"accept": "application/json"}
    payload_post_did = {}

    try:
        r_post_did = requests.post(url=url_post_did, json=payload_post_did, headers=headers_post_did)
        r_post_did = r_post_did.json()
    except Exception as errh:
        print(errh)

    return jsonify(r_post_did)

@app.route('/make_Connection/<int:agent1_admin_port>/<int:steward_admin_port>', methods=['POST'])
def make_Connection_endpoint(agent1_admin_port, steward_admin_port):
    url_create_inv = "http://127.0.0.1:" + str(steward_admin_port) + "/connections/create-invitation"
    headers_create_inv = {"accept": "application/json", "Content-Type": "application/json"}
    payload_create_inv = {}

    try:
        r_create_inv = requests.post(url=url_create_inv, json=payload_create_inv, headers=headers_create_inv)
        r_create_inv = r_create_inv.json()
    except Exception as errh:
        print(errh)

    invitation = r_create_inv['invitation']
    steward_conn_id = r_create_inv['connection_id']

    url_rcv_inv = "http://127.0.0.1:" + str(agent1_admin_port) + "/connections/receive-invitation"
    headers_rcv_inv = {"accept": "application/json", "Content-Type": "application/json"}
    payload_rcv_inv = invitation

    try:
        r_rcv_inv = requests.post(url=url_rcv_inv, json=payload_rcv_inv, headers=headers_rcv_inv)
        r_rcv_inv = r_rcv_inv.json()
    except Exception as errh:
        print(errh)