import hashlib
import time

class Blockchain():
    def __init__(self):
        self.chain = [] #creating array of blocks

class Block():
    def __init__(self,index, transactions, time):
        self.index = index #this will be the index of each block
        self.transactions = transactions #transaction data here
        self.time = time #timestamp
        self.previous_hash = '' #hash of previous block
        self.hash = self.calculate_hash() #func to calculate a hash for each block

    def calculate_hash(self):
        hash_transactions = ''
        for transaction in self.transactions:
            hash_transactions += transaction.__hash__()
    #this func will calculate a hash for each block using sha256 encryption

class Transaction():
    def __init__(self):