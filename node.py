class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Block:
    def __init__(self):
        pass

    def makeBlock(self, previousHash, timestamp, nonce, hash, transactions):
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = hash
        self.transactions = transactions
        #newBlock = str(self.previousHash) + str(self.timestamp) + str(self.nonce) + str(self.hash) + str(self.transactions)
        newBlock = [self.previousHash, self.timestamp, self.nonce, self.hash, self.transactions]
        return newBlock

class LinkedList():
    def __init__(self):
        # Head is start of chain, not end.
        self.head = None
    
    def insertAtBeginning(self, data):
        # Make new node
        new_node = Node(data)

        # Set next node as current start of list, since we are replacing it soon
        new_node.next = self.head

        # Update head with new node, which is at beginning
        self.head = new_node
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def insertAtIndex(self,data,index):
        # Create new node with data in the function
        new_node = Node(data)

        # Check if node will be first in list
        if self.head == None:
            self.head = new_node
            return
        
        # Define variables for loop
        current = self.head
        counter = 0 
        # while self.head is not equal to none and counter is not lower than index - 1
        while current is not None and counter < index -1:
            current = current.next
            counter += 1

        # Set new_node.next to found index
        new_node.next = current.next
        # Set current.next to the new node
        current.next = new_node
    
    def printList(self):
        current = self.head
        while current is not None:
            print(current.data,"\n")
            current = current.next
    
    def returnListAsTable(self):
        current = self.head
        table = []
        while current is not None:
            table.append(current.data)
            current = current.next
        return table

    def findNodeFromKey(self, key):
        current = self.head

        if current is not None and current.data == key:
            return current.data
        
        while current is not None and current.data != key:
            current = current.next
        if current is None:
            print("Did not find key")
            return

    def deleteNode(self, key):
        current = self.head

        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return
        
        while current is not None and current.data != key:
            current = current.next
        if current is None:
            print("Did not find key")
            return
    def deleteNodeAtIndex(self,index):
        current = self.head
        counter = 0
        if self.head is None:
            print("List is empty")
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        while current is not None and counter < index -1:
            current = current.next
            counter += 1
        
        if current is None or current.next is None:
            print("Index does not exist in list.")
            return

        current.next = current.next.next