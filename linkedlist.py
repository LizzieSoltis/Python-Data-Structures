#Python Data Structures
#Part 1/2 with Linked Lists: Covers basics of lists; Nodes, Prepending, Appending, Print, Remove first, and Remove last
#More concise coding covered in part 2; Insertion at certain index and Removal at certain index
'''
What is a linked list?
- A linked list is a dynamic data structure which is made of nodes.
- These nodes reference the next node in line, forming a list
'''

'''
What is a Node?
- A node has two attributes: 
    1. Data, this can be of any type
    2. Next, this references the next node within the list
'''
print("Part 1\n") #ignore this, just for breaking up terminal output
class Node: #helper class, Node
    def __init__(self, data):
        self.data = data #inizializing data attribute to data being passed in
        self.next = None #setting next attribute to None, symbolizing that this node is not referencing anything

#Typical usage of the node class:
n = Node(1) #instantiate a new node object passing in the argument 1, 
print(n.next) #and it doesn't reference any other node (this prints None)

#Linked list
'''
Linked list has to keep track of a couple things:
    1. the header ---> the node at the front of the list (most recently added node)
    2. the tail ---> the node at the back of the list (first node to go in empty list, last node of list as list builds)
    3. the size ---> how many nodes are within the list
- NOTE: In class we've only been tracking the front node but either works
'''
class LinkedList:
    def __init__(self):
        self.header = None #inizializing header
        self.tail = None #inizializing tail
        self.size = 0 #setting size to 0

    def prepend(self, data): #add node to front of list
        node = Node(data) #step 1) create new node
        #step 2:
        if (self.size == 0): #Case 1, checking to see if list is empty
            #if it is empty, set the header and tail of list to reference the created node, since it's the only one in the list
            self.header = node
            self.tail = node
        else: #Case 2, if list isn't empty
            node.next = self.header #make next attribute of new node reference the node the header is referencing(the node at the front of the list)
            self.header = node #set the header to reference the new first node of the list
        self.size += 1 #increment the size
    
    def append(self, data): #add node to back of list
        node = Node(data)
        if (self.size == 0): #Case 1, see if list is empty
            #if it is empty, set the header and tail of list to reference the created node
            self.header = node
            self.tail = node
        else: #Case 2, list isn't empty
            temp = self.tail #save the reference of our tail within a temporary variable
            self.tail = node #make the tail reference the new node
            temp.next = self.tail #make old tail next attribute reference the new node
        self.size += 1 #increment the size

    def printList(self):
        data = [] #where node data will be stored 
        current = self.header
        while current != None: #traversing the list, if current is None means were at end of list
            data.append(current.data)  #saving data
            current = current.next #moving on to next node
        return data
    
    def removeFirst(self): 
        if self.size == 0: #case 1, list is empty
            return None
        data = self.header.data  #whatever the case, need to return data so set data to header. Even if list is empty None should be returned
        if self.size == 1: #case 2, list has one element, clear list
            self.header = None 
            self.tail = None
        else: #case 3, list has more than one element, remove header
            self.header = self.header.next
        self.size -= 1
        return data
    
    def removeLast(self):
        if self.size == 0: #case 1, list is empty
            return None
        data = self.tail.data #whatever the case, need to return data so set data to tail. Even if list is empty None should be returned
        if self.size == 1: #case 2, list has one element, clear list
            self.header = None
            self.tail = None
        else:
            current = self.header
            while current.next.next != None: #trying to find node before the last node in the list
                current = current.next
            current.next = None #removing last node
            self.tail = current #setting new tail
        self.size -= 1
        return data
'''
Linked List: Prepending/Adding to front of list 
Prepending means you want to add a node to the front of the list
- So within our LinkedList class we will define a method called prepend or add that has two parameters:
    1. self
    2. data ---> this data will be given to the node that we want to insert within our list
- Steps of adding a node to a linked list:
    1. Create node containg the data to be inserted into the list
    2. Insert node BUT there are two cases to consider here:
        - What happens if the list is empty? (Case 1)
        - What happens if the list is not empty? (Case 2)
'''
print("\nPart 2")
#Typical Usage of the LinkedList class w/ prepend
list = LinkedList() #create an instance of a linked list, resulting in header and tail referencing None and size 0
print("=====Prepending 4=====")
list.prepend(4) #adding 4 to the list
print("Header: {}\nTail: {}\nSize: {}".format(list.header,list.tail,list.size))
#Notice how printing list.header and list.tail prints __main__.Node Object (the instance of the node), and not the node's data (4)
#This is because the node object is stored in these attributes, the actual data is within the node object

print("\nHeader: {}\nTail: {}\nSize: {}".format(list.header.data, list.tail.data ,list.size))
#Printing list.header.data and list.tail.data gets the data within the header and tail node object
print("\n=====Prepending 8=====")
list.prepend(8)
print("Header: {}\nTail: {}\nSize: {}".format(list.header.data, list.tail.data ,list.size)) #header is now 8, tail is 4, size is 2

print("\n=====Prepending 'Hello World'=====")
list.prepend("Hello World")
print("Header: {}\nTail: {}\nSize: {}".format(list.header.data, list.tail.data ,list.size)) #header is now 'hello world', tail is 4, size is 3

'''
Linked List: Appending/Adding to back of list
Appending means you want to add a node to the back of a list
- To do this, we declare method append in our linked list class (line 49)
Steps for insertion:
    1. Create a node to insert
    2. Insert node BUT consider these two cases:
        - What happens if the list is empty? (Case 1)
        - What happens if the list isn't empty? (Case 2)
'''
print("\nPart 3")
#Typical Usage of the LinkedList class w/ append
list2 = LinkedList()
print("======Appending 3=====")
list2.append(3)
print("Header: {}\nTail: {}\nSize: {}".format(list2.header.data, list2.tail.data, list2.size)) #header is 3, tail is 3, size is 1

print("\n======Appending 9=====")
list2.append(9)
print("Header: {}\nTail: {}\nSize: {}".format(list2.header.data, list2.tail.data, list2.size)) #header is 3, tail is 9, size is 2

print("\n======Appending 18=====")
list2.append(18)
print("Header: {}\nTail: {}\nSize: {}".format(list2.header.data, list2.tail.data, list2.size)) #header is 3, tail is 18, size is 3

'''
NOTE: Not every Linked List needs both a prepend and append method:
- If you just need to add things to your list, you can have one method called add() and have the nodes be inserted the prepend way or the append way, whatever achieves your desired list
- In class, we use instert(self, index, entry) and insert entry based off index, method is defined later in part 2
'''

'''
Linked List: Printing  List
- To print out our list, we define a method called printList() (line 61)
1. Create empty string/list to save data thats stored within nodes, this string/list will be returned at the end of the method
2. Start at the beggining of the list. So we grab header node and call it current 
3. Traverse the list using a while loop NOTE: in class we printed in different traversal orders, but this is just a general print
4. One method is to save the data while traversing by appending it to a string, I'm going to append it to a list for better printing to terminal
'''
print("\nPart 4") #ignore
print("=====PRINTING LIST 1=====")
data1 = list.printList()
print(data1)

print("\n=====PRINTING LIST 2=====")
data2 = list2.printList()
print(data2)

'''
Linked List: Removing first node from list
- To remove the first node, declare method called removeFirst() (line 70)
1. Check size
    - Case 1: List is empty, return None
    If not empty, set data to be the header's data before case 2 and three since we'll be removing node shortly
    - Case 2: List only has one element, set header and tail to None
    - Case 3: List has more than one element, set header to the next node in list
2. Remove node based on cases above
3. Decrement Size
4. Return Data
'''
print("\n Part 5")
print("=====Remove First Node from List 1=====")
removed = list.removeFirst()
print("Node removed: {}".format(removed))

print("\n=====Remove First Node from List 2=====")
removed = list2.removeFirst()
print("Node removed: {}".format(removed))


'''
Linked Lists: Remove last node from list
- To remove the last node, declare method called removeLast() (line 82)
1. Check size
    - Case 1: List is empty, return None
    If not empty, save data of node you want to remove
    - Case 2: List has one element, remove node by setting header and tail to None
    - Case 3: List has more than one element, find node before tail and change it's reference pointer to None, set new tail as current
2. Remove node based on cases above
3. Decrement the size
4. Return the data
'''
list.prepend(10) #adding elements to show removal
list.prepend("hi")
list2.prepend(4)
list2.prepend(200)

print("\nRemoving last node from list 1 --> {}".format(list.printList()))
removed = list.removeLast()
print("Node removed: {}".format(removed))
print("New list 1: {}".format(list.printList()))

print("\nRemoving last node from list 2 --> {}".format(list2.printList()))
removed = list2.removeLast()
print("Node removed: {}".format(removed))
print("New list 2: {}".format(list2.printList()))