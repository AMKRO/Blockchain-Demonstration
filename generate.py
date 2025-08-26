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

difficulty = 1
verbose = False

class Generate:
    def __init__(self):
        pass
    # Pass for now, don't need to initialise anything
    def calcHash(self, transactions, timestamp, previous_hash, nonce):
        
        block = str(transactions) + str(timestamp) + str(previous_hash) + str(nonce)
        if verbose: print("BLOCK: ", block)
        return hashlib.sha256(block.encode()).hexdigest()
    # Calculate the hash - mining function
    # Encrypt in SHA256, .encode() to convert string to bytes, and .hexdigest() to convert to hexadecimal string

    def generateBlock(self, transactionTable):
        if verbose: print(transactionTable)
        # If verbose flag, print debug logs
        llist = LinkedList()
        chain_data = llist.returnListAsTable()
        # Return data of entire chain as a table
        print("lenCD: ",len(chain_data))
        if len(chain_data) == 0:
            previous_hash = "0" * 64
            # If no previous hash due to start of chain, set previous hash as 0*64
        else:
            print("Chain Data: ",chain_data,"\nChain Data -1[0]: ",chain_data[-1][0])
            previous_hash = chain_data[len(chain_data)-1][0]
            # If chain is NOT starting, return previous hash as last node in chain data hash.

        print("PREVIOUS HASH:", previous_hash)
        self.nonce = 0
        while True:
            self.timestamp = time.time()
            # Get timestamp of block creation
            tempHash = self.calcHash(transactionTable, self.timestamp, previous_hash, self.nonce)
            # Calculate the temporary hash of the block
            if verbose: print(tempHash, "NONCE:", self.nonce)
            if tempHash.startswith('0' * difficulty):
                # If temporary hash begins with '0' multiplied by the difficulty rating then:
                if verbose: print("BLOCK SUCCESSFULLY MINED!\nHASH:", tempHash)
                #########return [tempHash, previous_hash, self.timestamp, self.nonce, transactionTable]
                return(previous_hash, self.timestamp, self.nonce, tempHash, transactionTable)
                # Return successful data
            else:
                self.nonce += 1
                # If not successful, increase the NONCE (number only used once)