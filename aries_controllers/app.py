from flask import Flask, request
from utils import *

app = Flask(__name__)

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
    result = gen_Schema(agent_admin_port, schema)
    return {'result': result}

@app.route('/gen_CredDef', methods=['POST'])
def gen_CredDef_endpoint():
    agent_admin_port = request.json['agent_admin_port']
    credDef = request.json['credDef']
    result = gen_CredDef(agent_admin_port, credDef)
    return {'result': result}

@app.route('/issue_Cred', methods=['POST'])
def issue_Cred_endpoint():
    steward_admin_port = request.json['steward_admin_port']
    cred = request.json['cred']
    result = issue_Cred(steward_admin_port, cred)
    return {'result': result}

@app.route('/send_cred_req', methods=['POST'])
def send_cred_req_endpoint():
    steward_admin_port = request.json['steward_admin_port']
    agent_did = request.json['agent_did']
    result = send_cred_req(steward_admin_port, agent_did)
    return {'result': result}

@app.route('/send_proof_req', methods=['POST'])
def send_proof_req_endpoint():
    steward_admin_port = request.json['steward_admin_port']
    proof = request.json['proof']
    result = send_proof_req(steward_admin_port, proof)
    return {'result': result}

@app.route('/send_presentation', methods=['POST'])
def send_presentation_endpoint():
    agent_admin_port = request.json['agent_admin_port']
    result = send_presentation(agent_admin_port)
    return {'result': result}