from flask import Flask
from flask import jsonify
import requests
import time
import json

    ##Creates and post public DID
    ##SAMPLE RESP : {'result': {'did': 'Hc4GRdjapBrCZf83ypqJGW', 'verkey': 'A3u7HykmMQdv1vsBqiTdMbZVdf6u2Sos4nNuMafMS5Kn', 'posture': 'posted', 'key_type': 'ed25519', 'method': 'sov'}}
def create_public_did(agent1_admin_port, steward_admin_port):
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
    
    did  = r_create_did['result']['did']
    verkey = r_create_did['result']['verkey']

    url_reg_nym = "http://127.0.0.1:" + str(steward_admin_port) + "/ledger/register-nym?did=" + str(did) + "&verkey=" + str(verkey)
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
    
    return r_post_did

def make_Connection(agent1_admin_port, steward_admin_port):
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
    
    alice_conn_id = r_rcv_inv['connection_id']

    url_accept_inv = "http://127.0.0.1:" + str(agent1_admin_port) + "/connections/" + str(alice_conn_id) + "/accept-invitation"
    headers_accept_inv = {"accept": "application/json"}
    payload_accept_inv = {}

    try:
        r_accept_inv = requests.post(url=url_accept_inv, json=payload_accept_inv, headers=headers_accept_inv)
        r_accept_inv = r_accept_inv.json()
    except Exception as errh:
        print(errh)


    time.sleep(0.1)
    url_accept_req = "http://127.0.0.1:" + str(steward_admin_port) + "/connections/" + str(steward_conn_id) + "/accept-request"
    headers_accept_req = {"accept": "application/json"}
    payload_accept_req = {}

    try:
        r_accept_req = requests.post(url=url_accept_req, data=payload_accept_req, headers=headers_accept_req)
        r_accept_req = r_accept_req.json()
    except Exception as errh:
        print(errh)
    
    return steward_conn_id, alice_conn_id

def gen_Schema(agent_admin_port, schema):
    url_schema = "http://127.0.0.1:" + str(agent_admin_port) + "/schemas"
    headers_schema = {"accept": "application/json", "Content-Type": "application/json"}
    payload_schema = str(schema)

    try:
        r_schema = requests.post(url=url_schema, data=payload_schema, headers=headers_schema)
        r_schema = r_schema.json()
    except Exception as errh:
        print(errh)

    return r_schema

def gen_CredDef(agent_admin_port, credDef):
    print(credDef)
    url_CredDef = "http://127.0.0.1:" + str(agent_admin_port) + "/credential-definitions"
    headers_CredDef = {"accept": "application/json", "Content-Type": "application/json"}
    payload_CredDef = credDef
    try:
        r_CredDef = requests.post(url=url_CredDef, data=payload_CredDef, headers=headers_CredDef)
        if r_CredDef.status_code == 200:
            r_CredDef = r_CredDef.json()
        else:
            print(r_CredDef.text)
    except Exception as errh:
        print(errh)

    return r_CredDef

def issue_Cred(steward_admin_port, agent_admin_port, cred):
    url_send_offer = "http://127.0.0.1:" + str(steward_admin_port) + "/issue-credential-2.0/send"
    headers_send_offer = {"accept": "application/json", "Content-Type": "application/json"}
    payload_send_offer = cred
    try:
        r_send_offer = requests.post(url=url_send_offer, data=payload_send_offer, headers=headers_send_offer)
        if r_send_offer.status_code == 200:
            r_send_offer = r_send_offer.json()
        else:
            print(r_send_offer.text)
    except Exception as errh:
        print(errh)

    return r_send_offer

def send_cred_req(agent_admin_port, agent_did):
    url_fetch_cred_ex = "http://127.0.0.1:" + str(agent_admin_port) + "/issue-credential-2.0/records"
    headers_fetch_cred_ex = {"accept": "application/json"}
    payload_fetch_cred_ex = {}
    try:
        r_fetch_cred_ex = requests.get(url=url_fetch_cred_ex, data=payload_fetch_cred_ex, headers=headers_fetch_cred_ex)
        if r_fetch_cred_ex.status_code == 200:
            r_fetch_cred_ex = r_fetch_cred_ex.json()
        else:
            print(r_fetch_cred_ex.text)
    except Exception as errh:
        print(errh)
    
    cred_ex_id = r_fetch_cred_ex['results'][0]['cred_ex_record']['cred_ex_id']
    
    url_send_req = "http://127.0.0.1:" + str(agent_admin_port) + "/issue-credential-2.0/records/" + str(cred_ex_id) + "/send-request"
    headers_send_req = {"accept": "application/json", "Content-Type": "application/json"}
    payload_send_req_t = {
        "holder_did": agent_did
    }
    payload_send_req = json.dumps(payload_send_req_t)
    try:
        r_send_req = requests.post(url=url_send_req, data=payload_send_req, headers=headers_send_req)
        if r_send_req.status_code == 200:
            r_send_req = r_send_req.json()
        else:
            print(r_send_req.text)
    except Exception as errh:
        print(errh)

    return r_send_req

if __name__ == "__main__":
    # agent_did = create_public_did(9001, 8001)
    # print(agent_did)
    # steward_agent_conn_id, agent_steward_conn_id = make_Connection(9001, 8001)
    # print(steward_agent_conn_id, agent_steward_conn_id)

    # sample_schema = {
    #     "attributes": [
    #         "score"
    #     ],
    #     "schema_name": "prefs",
    #     "schema_version": "1.0"
    # }
    # json_schema = json.dumps(sample_schema)
    # schema = gen_Schema(8001, json_schema)
    # print(schema)

    # sample_CredDef = {
    #     "revocation_registry_size": 1000,
    #     "schema_id": "Th7MpTaRZVRYnPiabds81Y:2:prefs:1.0",
    #     "support_revocation": False,
    #     "tag": "default"
    # }
    # json_CredDef = json.dumps(sample_CredDef)
    # CredDef = gen_CredDef(8001, json_CredDef)
    # print(CredDef)

    #####################################################

    sample_cred = {
        "auto_remove": True,
        "comment": "string",
        "connection_id": "b20a154e-6c16-49ec-ba83-bac593c6a47e",
        "credential_preview": {
            "@type": "issue-credential/2.0/credential-preview",
            "attributes": [
            {
                "mime-type": "text/plain",
                "name": "score",
                "value": "69"
            }
            ]
        },
        "filter": {
            "indy": {
            "cred_def_id": "Th7MpTaRZVRYnPiabds81Y:3:CL:14:default",
            "issuer_did": "Th7MpTaRZVRYnPiabds81Y",
            "schema_id": "Th7MpTaRZVRYnPiabds81Y:2:prefs:1.0",
            "schema_issuer_did": "Th7MpTaRZVRYnPiabds81Y",
            "schema_name": "prefs",
            "schema_version": "1.0"
            }
        },
        "trace": True
    }

    # json_Cred = json.dumps(sample_cred)
    # Cred_resp = issue_Cred(8001, 9001, json_Cred)
    # print(Cred_resp)

    print(send_cred_req(9001, "7EosWdvAhYnzUJE2YCjiNr"))

    #############################################################
