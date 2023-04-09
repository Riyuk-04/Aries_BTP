sudo docker run -itd -p 9701-9708:9701-9708 ghoshbishakh/indy_pool

aca-py start -it http 0.0.0.0 8000 -ot http -e http://127.0.0.1:8000 --admin-insecure-mode --admin 0.0.0.0 8001 \
--genesis-file /home/ishan/pool1.txn --seed 000000000000000000000000Steward1 --wallet-type indy --wallet-name r6 --wallet-key r6 \
--log-level debug --replace-public-did --auto-provision --auto-store-credential --auto-accept-requests --auto-respond-presentation-proposal --auto-verify-presentation

aca-py start -it http 0.0.0.0 9000 -ot http -e http://127.0.0.1:9000 --admin-insecure-mode --admin 0.0.0.0 9001 \
--genesis-file /home/ishan/pool1.txn --wallet-type indy --wallet-name r7 --wallet-key r7 \
--log-level debug --replace-public-did --auto-provision --auto-store-credential --auto-accept-requests --auto-respond-presentation-proposal --auto-verify-presentation

aca-py start -it http 0.0.0.0 10000 -ot http -e http://127.0.0.1:10000 --admin-insecure-mode --admin 0.0.0.0 10001 \
--genesis-file /home/ishan/pool1.txn --seed 000000000000000000000000Steward2 --wallet-type indy --wallet-name r5 --wallet-key r5 \
--log-level debug --replace-public-did --auto-provision --auto-store-credential --auto-accept-requests --auto-respond-presentation-proposal --auto-verify-presentation

aca-py provision --wallet-type indy --seed 000000000000000000000000Steward1 -e 127.0.0.1:8000 --genesis-file /home/ishan/pool1.txn \
--wallet-name agent1 --wallet-key agent1

aca-py provision --wallet-type indy -e http://127.0.0.1:9000 --genesis-file /home/ishan/pool1.txn --wallet-name steward1 --wallet-key steward1

--public-invites --auto-ping-connection --auto-accept-invites --auto-accept-requests --auto-respond-presentation-proposal --auto-store-credential --auto-verify-presentation