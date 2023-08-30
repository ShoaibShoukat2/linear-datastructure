
import sys
class Node:
    def __init__(self,data):    
        
        self.prev =None
        self.data = data
        self.next =None



class Linkedlist:
    def __init__(self):
        self.headval = None

    
    def push_at_beg(self, newData):
        new_node = Node(newData)
        new_node.next = self.headval
        self.headval = new_node
        print('Node Inserted Successfully at the beginning')

    def print_linklist(self):
        if self.headval:
            current = self.headval

            while current:
                print(current.data)
                current = current.next

    
    def delete_node(self, node):
        if self.headval:
            prev = None
            current = self.headval

            while current:
                if current.data == node:
                    print("Node to be deleted:", current.data)
                    
                    if prev:  # If the node to be deleted is not the head node
                        prev.next = current.next
                    else:  # If the node to be deleted is the head node
                        self.headval = current.next
                        
                    print("Node deleted:", current.data)
                    return
                    
                prev = current
                current = current.next

            print("Node not found in the linked list.")
            
        else:
            print('Linked list is empty')

   
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


doubly_linklist.print_linklist()

print("Below deleted node ")
