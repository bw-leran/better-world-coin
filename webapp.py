from flask import Flask, request
from Blockchain import Blockchain
import requests
import json

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/chain',methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({'length':len(chain_data),
                       'chain':chain_data})

app.run(debug=True,port=5000)

'''
Coin is currently centralized to this server.  In the beginning (during the testing phase) I will be "beta'ing" the coin
meaning that I'll let people add coins for free. But they'll be deleted if the server goes down or something. Will probably do
the webhosting stuff maybe. Or possibly just host it on my local machine for testing purposes? Will see.

Next Steps:
    -Implement "Proof of Stake" algorithm
    -Write up simple web app that can
        -login
        -"buy" coin
        -trade coin
        -mine coin
    -Release Alpha version
    -See where we at at this point
'''
