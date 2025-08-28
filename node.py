# Node.py

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
        # Get the current node
        while current is not None:
            print(current.data,"\n")
            # Print current node data
            current = current.next
            # Set current to current.next to retrieve next node, until current equals None.
    
    def returnListAsTable(self):
        current = self.head
        # Set current to start of list
        table = []
        # Create table to return as list
        while current is not None:
            table.append(current.data)
            current = current.next
            # Add current.data to table and set current to next in node, until current equals None.
        ##print("CHAIN DATA TABLE:\n",table)
        return table

    def findNodeFromKey(self, key):
        current = self.head
        # Set current to beginning of chain
        if current is not None and current.data == key:
            return current.data
            # Return data of current if key is found
        
        while current is not None and current.data != key:
            current = current.next
            # If current is not None and current.data does not equal key, then change current to the next in the chain.
        if current is None:
            print("Did not find key")
            # If key not found, print.
            return

    def deleteNode(self, key):
        current = self.head

        if current is not None and current.data == key:
            # If current is not none and current.data equals key provided, then:
            self.head = current.next
            # Remove node from list by changing head to current.next
            current = None
            return
        
        while current is not None and current.data != key:
            current = current.next
            # If node does not match key, move to next node in chain.
        if current is None:
            print("Did not find key")
            # If node not found, print.
            return
        
    def deleteNodeAtIndex(self,index):
        current = self.head
        counter = 0
        # Set iteration variable to 0
        if self.head is None:
            print("List is empty")
            # If list does not exist yet, print.
            return
        
        if index == 0:
            self.head = self.head.next
            # If index = 0, set head of chain to next node in chain; removing the first.
            return
        
        while current is not None and counter < index -1:
            # While current is not equal to None and the counter variable is less than the index variable minus 1, then:
            current = current.next
            counter += 1
            # Node = next node in chain, counter + 1 to its value.
        
        if current is None or current.next is None:
            # If current is None or current next node is None then:
            print("Index does not exist in list.")
            # Print
            return

        current.next = current.next.next
        # Set current next node to current next node next node