
import sys
class Node:
    def __init__(self, next=None, prev=None, data=None):
        
        self.prev = prev
        self.data = data
        self.next = next



class Linkedlist:
    def __init__(self):
        self.headval = None

    
    def push_at_beg(self, newData):
        new_node = Node(newData)
        new_node.next = self.headval
        self.headval = new_node
        print('Node Inserted Successfully at the beginning')


# Now Created Doubly linklist

doubly_linklist =  Linkedlist()


node1 =  Node(1)
node2 =  Node(2)
node3 =  Node(3)
node4 =  Node(4)
node5 =  Node(5)


node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

doubly_linklist.headval = node1

doubly_linklist.push_at_beg(12)



# empty node prev in the head node & empty next of the last node 
