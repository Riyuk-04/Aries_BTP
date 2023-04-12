from flask import Flask, request, render_template
from utils import *
import json

app = Flask(__name__, template_folder='templates')

@app.route('/issuer')
def issuer():
    return render_template('issuer.html')

@app.route('/alice')
def alice():
    return render_template('alice.html')

@app.route('/hospital')
def hospital():
    return render_template('hospital.html')


@app.route('/create_public_did', methods=['POST'])
def create_public_did_endpoint():
    agent1_admin_port = request.json['agent1_admin_port']
    steward_admin_port = request.json['steward_admin_port']
    result = create_public_did(agent1_admin_port, steward_admin_port)
    return {'result': result}

@app.route('/make_Connection', methods=['POST'])
def make_Connection_endpoint():
    # request = json.dumps(request)
    # request = request.json()
    agent1_admin_port = request.json['agent1_admin_port']
    steward_admin_port = request.json['steward_admin_port']
    result = make_Connection(agent1_admin_port, steward_admin_port)
    return {'result': result}

@app.route('/gen_Schema', methods=['POST'])
def gen_Schema_endpoint():
    agent_admin_port = request.json['agent_admin_port']
    schema = request.json['schema']
    schema = json.dumps(schema)
    result = gen_Schema(agent_admin_port, schema)
    return {'result': result}

@app.route('/gen_CredDef', methods=['POST'])
def gen_CredDef_endpoint():
    agent_admin_port = request.json['agent_admin_port']
    credDef = request.json['credDef']
    credDef = json.dumps(credDef)
    result = gen_CredDef(agent_admin_port, credDef)
    return {'result': result}

@app.route('/issue_Cred', methods=['POST'])
def issue_Cred_endpoint():
    connection_id  = request.data.decode()
    steward_admin_port = 8001
    cred = {
        "auto_remove": True,
        "comment": "string",
        "connection_id": connection_id,
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
            "cred_def_id": "Th7MpTaRZVRYnPiabds81Y:3:CL:15:default",
            "issuer_did": "Th7MpTaRZVRYnPiabds81Y",
            "schema_id": "Th7MpTaRZVRYnPiabds81Y:2:prefs:1.0",
            "schema_issuer_did": "Th7MpTaRZVRYnPiabds81Y",
            "schema_name": "prefs",
            "schema_version": "1.0"
            }
        },
        "trace": True
    }
    cred = json.dumps(cred)
    result = issue_Cred(steward_admin_port, cred)
    return {'result': result}

@app.route('/send_cred_req', methods=['POST'])
def send_cred_req_endpoint():
    agent_admin_port = 9001
    agent_did = request.data.decode()
    result = send_cred_req(agent_admin_port, agent_did)
    return {'result': result}

@app.route('/send_proof_req', methods=['POST'])
def send_proof_req_endpoint():
    steward_admin_port = 10001
    connection_id = request.data.decode()
    proof = {
        "comment": "This is a comment about the reason for the proof",
        "connection_id": connection_id,
        "presentation_request": {
            "indy": {
            "name": "Proof of Education",
            "version": "1.0",
            "requested_attributes": {
                "0_name_uuid": {
                "name": "score",
                "restrictions": [
                    {
                    "cred_def_id": "Th7MpTaRZVRYnPiabds81Y:3:CL:15:default"
                    }
                ]
                }
            },
            "requested_predicates": {

            }
            }
        }
    }
    proof = json.dumps(proof)
    result = send_proof_req(steward_admin_port, proof)
    return {'result': result}

@app.route('/send_presentation', methods=['POST'])
def send_presentation_endpoint():
    agent_admin_port = 9001
    result = send_presentation(agent_admin_port)
    return {'result': result}

@app.route('/proof_record', methods=['POST'])
def proof_record_endpoint():
    agent_admin_port = request.json['agent_admin_port']
    result = proof_record(agent_admin_port)
    return {'result': result}

@app.route('/see_credentials', methods=['POST'])
def see_credentials_endpoint():
    agent_admin_port = request.json['agent_admin_port']
    result = see_credentials(agent_admin_port)
    return {'result': result}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)