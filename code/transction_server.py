from flask import Flask
from web3 import Web3
from flask import request
import jsonpickle
app = Flask(__name__)


ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
user_key_mappings = {'rahul':'0x16917ed7838B6C349aCbF093F26D7c2f2F028447',
                     'raghu': '0x6D1445e7d2474f0c7B35A8b63510603DD44f6b66'
                    }

account_1 = '0x59BE4373Dd222188872d310f32eb5E3eC16a22D9' # Fill me in
private_key = 'd9adb6d02502dcf666d7527ea47bdeab6ed384e51d4fd07f6a87ace392fb9b2a' # Fill me in

def send_money(receiver):
    nonce = web3.eth.getTransactionCount(account_1)
    account_2 =  user_key_mappings[receiver] #'0xc2771610D1E8d873838d6E758e86A0735C6566dA' # Fill me in
    tx = {
        'nonce': nonce,
        'to': account_2,
        'value': web3.toWei(2, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
    }

    signed_tx = web3.eth.account.signTransaction(tx, private_key)

    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return 'success'
    
@app.route('/sendmoney', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = jsonpickle.decode(request.data)
    print(req_data)
    receivers = req_data['receivers']
    for receiver in receivers:
        #if receiver in user_key_mappings:
        send_money(str(receiver))
    return "Money sent successfully !"
       

if __name__ == "__main__":
    app.run()
