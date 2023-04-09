from flask import Flask, request, render_template
from utils import *
import json

app = Flask(__name__, template_folder='templates')

@app.route('/hospital')
def hospital():
    return render_template('hospital.html')

@app.route('/alice')
def alice():
    return render_template('alice.html')

@app.route('/verifier')
def verifier():
    return render_template('verifier.html')


@app.route('/create_public_did', methods=['POST'])
def create_public_did_endpoint():
    agent1_admin_port = request.json['agent1_admin_port']
    steward_admin_port = request.json['steward_admin_port']
    result = create_public_did(agent1_admin_port, steward_admin_port)
    return {'result': result}

@app.route('/make_Connection', methods=['POST'])
def make_Connection_endpoint():
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
    steward_admin_port = request.json['steward_admin_port']
    cred = request.json['cred']
    cred = json.dumps(cred)
    result = issue_Cred(steward_admin_port, cred)
    return {'result': result}

@app.route('/send_cred_req', methods=['POST'])
def send_cred_req_endpoint():
    agent_admin_port = request.json['agent_admin_port']
    agent_did = request.json['agent_did']
    result = send_cred_req(agent_admin_port, agent_did)
    return {'result': result}

@app.route('/send_proof_req', methods=['POST'])
def send_proof_req_endpoint():
    steward_admin_port = request.json['steward_admin_port']
    proof = request.json['proof']
    proof = json.dumps(proof)
    result = send_proof_req(steward_admin_port, proof)
    return {'result': result}

@app.route('/send_presentation', methods=['POST'])
def send_presentation_endpoint():
    agent_admin_port = request.json['agent_admin_port']
    result = send_presentation(agent_admin_port)
    return {'result': result}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)