from hashlib import sha256
import json

class Block:
    def __init__(self, index:int, transactions:list, timestamp:float, previous_hash:str, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def generate_hash(self):
        block_string = json.dumps(self.__dict__,sort_keys=True)
        return sha256(block_string.encode()).hexdigest()