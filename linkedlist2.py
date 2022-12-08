#Python Data Structures
#Part 2/2 for linked lists: Covers Insertion and Removal at chosen/certain indicies, getters and setters
#Note: For inserting/removing at certain positions, you can use the methods defined in part 1, but here I'll take advantage of getters and setters

class Node: 
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.header = None #inizializing header
        self.tail = None #inizializing tail
        self.size = 0
    
    def printList(self): #from part 1
        data = [] 
        current = self.header
        while current != None: 
            data.append(current.data)  
            current = current.next 
        return data
    
    def set_data(self, index, data):
        if index >= self.get_length() or index < 0: #Checking if index is invalid
            print("Index is invalid")
        if index == 0: #setting data at index of first node:
            self.header.data = data
        if index == self.get_length()-1: #setting data at index of last node
            self.tail.data = data
        else: #index is valid but target index is not first or last node
            target = self.get_node(index)
            target.data = data

    def get_data(self, index):
        data = self.get_node(index).data #grabbing the node at index and returning the data of it
        return data

    def get_node(self, index): #getter for node at certain index
        if (index >= 0) and (index <= self.get_length()): #checking the validity of the index given, if less than 0 or greater than the size, it's invalid
            jumper = self.header #initializing the header as our 'jumper' variable that may change till we find node at index
            if index == 0: #meaning get the first node
                return jumper #return the first node
            if index == self.get_length() - 1: #meaning index wants to grab the last node
                return self.tail #return last node
            else: #index is not first or last node's index
                for i in range(index): #looping through the range of the index 
                    jumper = jumper.next #by the end of loop, jumper will be at the given position
                return jumper
        else: #index isnt valid
            print("Index is Invalid") 

    def get_length(self): #getter for list length
        return self.size #returns the size of the list
    
    def is_empty(self): #helper method to see if list is empty
        return self.header == None #returns True if empty, False if not

    def insertAt(self,index,data):
        new_node = Node(data) #make new node of data

        if index >= 0 and index <= self.get_length(): #check if index is valid
            if self.is_empty(): #case 1, list is empty, set header and tail to new node/only node now in list
                self.header = new_node 
                self.tail = new_node 

            elif index == 0: #case 2, insert at first position in list
                #self.prepend(data) ---> if using methods from part 1
                new_node.next = self.header #set new nodes next to the current header  
                self.header = new_node #adjust header to be new node

            elif index == self.get_length(): #case 3, insert at end of list
                #self.append(data) ----> if using methods from part 1
                self.tail.next = new_node #setting tail's next to be new_node and not None
                self.tail = new_node #adjusting tail to be new node

            else: #case 4, insert somewhere in list
                current = self.get_node(index) #grabbing current node at index given
                prev = self.get_node(index-1) #grabbing node previous to the current
                prev.next = new_node #making previous node to point to the new_node (inserting it at the current's index)
                new_node.next = current #making new node point to the node stored in current to 'reconnect' the list

            self.size += 1 #incrementing size
        else: #invalid index
            print("Invalid Index")
        
    def remove(self, index):
        if index >= 0 and index <= self.size: #checking validity of index passed through
            if self.is_empty(): #case 1, list is empty, can't remove
                print("Error, list is empty")
            else:
                if index == 0: #case 2, remove first node
                    #return self.removeFirst() ----> if using methods from part 1
                    self.header = self.header.next #remove first node by making header the next node after

                elif index == self.get_length()-1: #case 3, remove the last node
                    #return self.removeLast() ----> if using methods from part 1
                    target = self.get_node(index-1) #grab the node before the last node in list
                    self.tail = target #adjusting tail to be the new last node 
                    target.next = None #setting last nodes next to be None bc were at end of list

                else: #case 4, remove somewhere within the list
                    prev = self.get_node(index-1) #grab node previous to the target index
                    post = self.get_node(index+1) #grab node after the target index
                    prev.next = post #deleting node at given index by connecting it's prev and post nodes

                self.size -= 1 #decrement size
        else: #invalid index
            print("Invalid Index") 
'''
Linked Lists: Inserting Node at certain position
- Takes in 3 parameters (self, index, and data) and doesn't return anything
    - Index is where you want the new node at in your list
    - Data is the entry going into that node
1. Make new node of data
2. Check if index passed through to insert node at is valid (invalid would be indicies less than 0 or greater than the size)
3. Insert node at index:
    - Case 1, list is empty, make header and tail point to the inserted node
    If list isnt empty:
    - Case 2, index is 0 so insert node to be the first in the list by making the new node's next point to the header and then readjust header
    - Case 3, index at the end of list so make the current tail's next reference the new node and then adjust the tail
    - Case 4, index is within the list, store current node in a variable, grab current's previous node and set previous next to the new node, adjust new node's next to be current
4. Increment size
'''
print("==========Part 1==========") #ignore, for breaking up terminal output
list = LinkedList()
print("Inserting 4 at index 0")
list.insertAt(0, 4)
data1 = list.printList()
print("List --> {}".format(data1))

print("Inserting 10 at index 1")
list.insertAt(1, 10)
data2 = list.printList()
print("List --> {}".format(data2))

print("Inserting 'hi' at index 2")
list.insertAt(2, 'hi')
data3 = list.printList()
print("List --> {}".format(data3))

print("Inserting 50 at index 1")
list.insertAt(1, 50)
data4 = list.printList()
print("List --> {}".format(data4))

'''
Linked Lists: Getters and Setters
Why are they useful?
- Useful to use in certain class methods so an attribute of an object's instance can be easily grabbed (getters) or changed (setters)
- For the continuation of linked lists, I defined set_data(), get_data(), get_node(), and get_length()
- These getters and setters are described more in the code
'''
#Ex of how getters can work from outside the class (to visualize return of getters)
print("==========Part 2==========") #ignore
size = list.get_length()
print("\nGetting size")
print("Size of list: {}".format(size))

index3 = list.get_data(3)
print("\nGetting data at index 3")
print("Data: {}".format(index3))

'''
Linked Lists: Helper methods
Why are they useful?
- Useful to obtain info about the list in a less repeditive way
- Instead of constantly manually seeing if the list is empty, define an is_empty() helper method
- Helper method is described more in the code
'''

#Ex of using helper methods outside the class (to visualize return of helpers)
empty = list.is_empty()
print("\nThe list is empty, true or false?: {}".format(empty))

'''
Linked Lists: Remove node at certain point
To do this, declare method called remove with 2 parameters; self, index
1. Check if index is valid
2. Remove node at index:
    - Case 1: List is empty, raise error, cant remove from empty list
    - Case 2: Index of node to be removed is 0, adjust header to be the headers next node
    - Case 3: Index of node to be removed is the last node, grab node at the index before last (called target), adjust tail to be the target and target's next to be none
    - Case 4: Index is within list, grab prev and post node of the given index, set prev node's next to point to the post node
3. Decrement Size by 1
'''
print("==========Part 3==========") #ignore
info = list.printList()
print("Current List ---> {}".format(info))

print("\nRemoving node at index 2")
list.remove(2)
info0 = list.printList()
print("New List ---> {}".format(info0))

print("\nRemoving node at index 0")
list.remove(0)
info1 = list.printList()
print("New List ---> {}".format(info1))
