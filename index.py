## Import Libraries
import time
## Files
from generate import Generate
from node import LinkedList
from node import Block
## Variables
myList = LinkedList()
gen = Generate(myList)

transactionList = []
blockSize = 5

def addTransaction():
    global transactionList
    transaction = input("Enter Transaction Value: ")
    if transaction or transaction != "'":
        transactionList.append(transaction)
        if len(transactionList) == blockSize:
            blockData = gen.generateBlock(transactionList)
            tempHash = blockData[0]
            previousHash = blockData[1]
            timestamp = blockData[2]
            nonce = blockData[3]
            transactionTable = blockData[4]

            block = Block()
            newBlock = block.makeBlock(previousHash, timestamp, nonce, tempHash, transactionTable)
            print("New Block: ",newBlock)

            myList.insertAtEnd(newBlock)
            myList.printList()
            transactionList = []
        return

while True:
    addTransaction()