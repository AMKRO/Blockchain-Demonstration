## // Generate Block

# index = position in chain
# transactions = list of transactions inside of block
# timestamp = current time of block creation
# previous hash = 
# nonce (number used only once) = proof of work mechanism
# difficulty = number of zeros before hash


import hashlib
import time
from node import LinkedList

llist = LinkedList()
difficulty = 1
verbose = False

class Generate:
    def __init__(self, chain):
        self.chain = chain
    def calcHash(self, transactions, timestamp, previous_hash, nonce):
        
        block = str(transactions) + str(timestamp) + str(previous_hash) + str(nonce)
        if verbose: print("BLOCK: ", block)
        return hashlib.sha256(block.encode()).hexdigest()

    def generateBlock(self, transactionTable):
        if verbose: print(transactionTable)
        chain_data = self.chain.returnListAsTable()
        if len(chain_data) == 0:
            previous_hash = "0" * 64
        else:
            previous_hash = chain_data[-1]["hash"]

        self.nonce = 0
        while True:
            self.timestamp = time.time()
            print("PREVIOUS HASH:", previous_hash)
            tempHash = self.calcHash(transactionTable, self.timestamp, previous_hash, self.nonce)
            if verbose: print(tempHash, "NONCE:", self.nonce)
            if tempHash.startswith('0' * difficulty):
                if verbose: print("BLOCK SUCCESSFULLY MINED!\nHASH:", tempHash)
                return [tempHash, previous_hash, self.timestamp, self.nonce, transactionTable]
            else:
                self.nonce += 1