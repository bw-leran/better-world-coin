from Block import Block

import time

class Blockchain:
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0,[],time.time(),'0')
        genesis_block.hash = genesis_block.generate_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    difficulty = 2 #testing difficulty level for proof of work

    #would like to replace this with a "proof of stake" algorithm instead of "proof of work"
    def proof_of_work(self,block):
        #block.nonce = 0 #pretty sure I dont need this part
        generated_hash = block.generate_hash()
        while not generated_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            generated_hash = block.generate_hash()
        return generated_hash

    def proof_of_stake(self,block):
        pass
    #implementing "proof of stake" algorithm to replace "proof of work". Func is incomplete rn.

    def add_block(self,block,proof):
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block,proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self,block,block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.generate_hash())

    def add_new_transaction(self,transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block,proof)
        self.unconfirmed_transactions = []
        return new_block.index