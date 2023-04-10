from flask import Flask
from flask import jsonify
import requests
import time
import json

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

def issue_Cred(steward_admin_port, cred):
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

def send_proof_req(steward_admin_port, proof):
    url_proof_req = "http://127.0.0.1:" + str(steward_admin_port) + "/present-proof-2.0/send-request"
    headers_proof_req = {"accept": "application/json", "Content-Type": "application/json"}
    payload_proof_req = proof

    try:
        r_proof_req = requests.post(url=url_proof_req, data=payload_proof_req, headers=headers_proof_req)
        if r_proof_req.status_code == 200:
            r_proof_req = r_proof_req.json()
        else:
            print(r_proof_req.text)
    except Exception as errh:
        print(errh)

    return r_proof_req

def send_presentation(agent_admin_port):
    url_fetch_pres = "http://127.0.0.1:" + str(agent_admin_port) + "/present-proof-2.0/records"
    headers_fetch_pres = {"accept": "application/json"}
    payload_fetch_pres = {}

    try:
        r_fetch_pres = requests.get(url=url_fetch_pres, data=payload_fetch_pres, headers=headers_fetch_pres)
        if r_fetch_pres.status_code == 200:
            r_fetch_pres = r_fetch_pres.json()
        else:
            print(r_fetch_pres.text)
    except Exception as errh:
        print(errh)

    pres_ex_id = r_fetch_pres['results'][0]['pres_ex_id']

    url_fetch_cred = "http://127.0.0.1:" + str(agent_admin_port) + "/present-proof-2.0/records/" + str(pres_ex_id) + "/credentials"
    headers_fetch_cred = {"accept": "application/json"}
    payload_fetch_cred = {}

    try:
        r_fetch_cred = requests.get(url=url_fetch_cred, data=payload_fetch_cred, headers=headers_fetch_cred)
        if r_fetch_cred.status_code == 200:
            r_fetch_cred = r_fetch_cred.json()
        else:
            print(r_fetch_cred.text)
    except Exception as errh:
        print(errh)

    print(r_fetch_cred)
    cred_id = r_fetch_cred[0]['cred_info']['referent']

    presentation = {
        "indy": {
            "requested_attributes": {
            "0_name_uuid": {
                "cred_id": cred_id,
                "revealed": True
            }
            },
            "requested_predicates": {
            },
            "self_attested_attributes": {
            },
            "trace": False
        },
        "trace": True
    }

    json_presentation = json.dumps(presentation)

    url_present_proof = "http://127.0.0.1:" + str(agent_admin_port) + "/present-proof-2.0/records/" + str(pres_ex_id) + "/send-presentation"
    headers_present_proof = {"accept": "application/json", "Content-Type": "application/json"}
    payload_present_proof = json_presentation

    try:
        r_present_proof = requests.post(url=url_present_proof, data=payload_present_proof, headers=headers_present_proof)
        if r_present_proof.status_code == 200:
            r_present_proof = r_present_proof.json()
        else:
            print(r_present_proof.text)
    except Exception as errh:
        print(errh)

    return r_present_proof

def proof_record(agent_admin_port):
    url_proof_record = "http://127.0.0.1:" + str(agent_admin_port) + "/present-proof-2.0/records"
    headers_proof_record = {"accept": "application/json"}
    payload_proof_record = {}

    try:
        r_proof_record = requests.get(url=url_proof_record, data=payload_proof_record, headers=headers_proof_record)
        if r_proof_record.status_code == 200:
            r_proof_record = r_proof_record.json()
        else:
            print(r_proof_record.text)
    except Exception as errh:
        print(errh)

    return r_proof_record

def see_credentials(agent_admin_port):
    url_see_creds = "http://127.0.0.1:" + str(agent_admin_port) + "/credentials"
    headers_see_creds = {"accept": "application/json"}
    payload_see_creds = {}

    try:
        r_see_creds = requests.get(url=url_see_creds, data=payload_see_creds, headers=headers_see_creds)
        if r_see_creds.status_code == 200:
            r_see_creds = r_see_creds.json()
        else:
            print(r_see_creds.text)
    except Exception as errh:
        print(errh)

    return r_see_creds

if __name__ == "__main__":
    agent_did = create_public_did(9001, 8001)
    print(agent_did)
    steward_agent_conn_id, agent_steward_conn_id = make_Connection(9001, 8001)
    print(steward_agent_conn_id, agent_steward_conn_id)

    sample_schema = {
        "attributes": [
            "score"
        ],
        "schema_name": "prefs",
        "schema_version": "1.0"
    }
    json_schema = json.dumps(sample_schema)
    schema = gen_Schema(8001, json_schema)
    print(schema)

    sample_CredDef = {
        "revocation_registry_size": 1000,
        "schema_id": "Th7MpTaRZVRYnPiabds81Y:2:prefs:1.0",
        "support_revocation": False,
        "tag": "default"
    }
    json_CredDef = json.dumps(sample_CredDef)
    CredDef = gen_CredDef(8001, json_CredDef)
    print(CredDef)

    ####################################################

    sample_cred = {
        "auto_remove": True,
        "comment": "string",
        "connection_id": "34939087-ab1f-4fc4-9ba0-617ea498f416",
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

    json_Cred = json.dumps(sample_cred)
    Cred_resp = issue_Cred(8001, json_Cred)
    print(Cred_resp)
    time.sleep(0.1)
    print(send_cred_req(9001, "J2XEPfYJGSvYDjNGjCfj8J"))

    ###########################################################

    sample_proof = {
        "comment": "This is a comment about the reason for the proof",
        "connection_id": "34939087-ab1f-4fc4-9ba0-617ea498f416",
        "presentation_request": {
            "indy": {
            "name": "Proof of Education",
            "version": "1.0",
            "requested_attributes": {
                "0_name_uuid": {
                "name": "score",
                "restrictions": [
                    {
                    "cred_def_id": "Th7MpTaRZVRYnPiabds81Y:3:CL:14:default"
                    }
                ]
                }
            },
            "requested_predicates": {

            }
            }
        }
    }

    json_proof = json.dumps(sample_proof)
    # proof_resp = send_proof_req(8001, json_proof)
    # print(proof_resp)
    time.sleep(0.1)
    print(send_presentation(9001))

    ######################################################################