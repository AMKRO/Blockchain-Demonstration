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
    if transaction or transaction != "'":
        transactionList.append(transaction)
        if len(transactionList) == blockSize:
            blockData = gen.generateBlock(transactionList)
            previousHash = blockData[0]
            timestamp = blockData[1]
            nonce = blockData[2]
            tempHash = blockData[3]
            transactionTable = blockData[4]

            block = Block()
            newBlock = block.makeBlock(previousHash, timestamp, nonce, tempHash, transactionTable)
            print("New Block: ",newBlock)
            print(myList.returnListAsTable())
            myList.insertAtEnd(newBlock)
            transactionList = []
            print(myList.returnListAsTable())
        return

while True:
    addTransaction()