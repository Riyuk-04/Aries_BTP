sudo docker run -itd -p 9701-9708:9701-9708 ghoshbishakh/indy_pool

aca-py start -it http 0.0.0.0 8000 -ot http -e http://127.0.0.1:8000 --admin-insecure-mode --admin 0.0.0.0 8001 \
--genesis-file /home/ishan/pool1.txn --seed 000000000000000000000000Steward1 --wallet-type indy --wallet-name agent1 \
--wallet-key agent1 --log-level debug --replace-public-did --auto-provision

aca-py start -it http 0.0.0.0 9000 -ot http -e http://127.0.0.1:9000 --admin-insecure-mode --admin 0.0.0.0 9001 \
--genesis-file /home/ishan/pool1.txn --wallet-type indy --wallet-name agent2 --wallet-key agent2 \
--log-level debug --replace-public-did --auto-provision

aca-py provision --wallet-type indy --seed 000000000000000000000000Steward1 -e 127.0.0.1:8000 --genesis-file /home/ishan/pool1.txn \
--wallet-name agent1 --wallet-key agent1

aca-py provision --wallet-type indy -e http://127.0.0.1:9000 --genesis-file /home/ishan/pool1.txn --wallet-name steward1 --wallet-key steward1

--public-invites --auto-ping-connection --auto-accept-invites --auto-accept-requests --auto-respond-presentation-proposal --auto-store-credential --auto-verify-presentation

{
  "auto_remove": true,
  "comment": "string",
  "cred_def_id": "Th7MpTaRZVRYnPiabds81Y:3:CL:16:default",
  "credential_proposal": {
    "@type": "issue-credential/1.0/credential-preview",
    "attributes": [
      {
        "weight": "70"
      }
    ]
  },
  "issuer_did": "Th7MpTaRZVRYnPiabds81Y",
  "schema_id": "Th7MpTaRZVRYnPiabds81Y:2:body_weight:1.0",
  "schema_issuer_did": "Th7MpTaRZVRYnPiabds81Y",
  "schema_name": "body_weight",
  "schema_version": "1.0",
  "trace": true
}

{
  "auto_remove": true,
  "comment": "string",
  "connection_id": "d1d273d9-f106-4ab0-b6d8-7fe8d1fdda7e",
  "credential_preview": {
    "@type": "issue-credential/2.0/credential-preview",
    "attributes": [
      {
        "score": "90"
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
    },
    "ld_proof": {
      "credential": {
        "@context": [
          "https://www.w3.org/2018/credentials/v1",
          "https://w3id.org/citizenship/v1"
        ],
        "credentialSubject": {
          "familyName": "SMITH",
          "gender": "Male",
          "givenName": "JOHN",
          "type": [
            "PermanentResident",
            "Person"
          ]
        },
        "description": "Government of Example Permanent Resident Card.",
        "identifier": "83627465",
        "issuanceDate": "2019-12-03T12:19:52Z",
        "issuer": "did:key:z6MkmjY8GnV5i9YTDtPETC2uUAW6ejw3nk5mXF5yci5ab7th",
        "name": "Permanent Resident Card",
        "type": [
          "VerifiableCredential",
          "PermanentResidentCard"
        ]
      },
      "options": {
        "proofType": "Ed25519Signature2018"
      }
    }
  },
  "trace": true
}
