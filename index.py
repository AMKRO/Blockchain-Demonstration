# Index.py
## Import Libraries
import time
## Files
from generate import Generate
from node import LinkedList
from node import Block
## Variables
myList = LinkedList()
gen = Generate()

transactionList = []
blockSize = 5

def addTransaction():
    global transactionList
    transaction = input("Enter Transaction Value: ")
    # Define transactionList as global variable so it can be accessed - maybe remove (?)
    if transaction or transaction != "":
        transactionList.append(transaction)
        if len(transactionList) == blockSize:
            # Confirm transaction provided is of valid type
            blockData = gen.generateBlock(transactionList, myList)
            previousHash = blockData[0]
            timestamp = blockData[1]
            nonce = blockData[2]
            tempHash = blockData[3]
            transactionTable = blockData[4]
            # Create variables based off block data table IF amount of transactions meets blockSize

            block = Block()
            # Create block object

            newBlock = block.makeBlock(previousHash, timestamp, nonce, tempHash, transactionTable)
            # Create block with variables defined earlier
            #print("New Block: ",newBlock)
            #print(myList.returnListAsTable())
            myList.insertAtEnd(newBlock)
            # Add block to chain
            transactionList = []
            print(myList.returnListAsTable())
        return

while True:
    addTransaction()
    # Repeat add transaction until block size threshold is reached.