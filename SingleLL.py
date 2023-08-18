class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None


class SingleList:
    def __init__(self):
        self.headval = None

    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def add_at_beginning(self,newdata):
        newnode = Node(newdata)
        newnode.nextval = self.headval
        self.headval = newnode

    def at_end(self,newData):
        newNode =  Node(newData)
        if self.headval is None:
            self.headval = newNode
        else:
            current =  self.headval
            while current.nextval is not None:
                current = current.nextval
            
            current.nextval = newNode

    def remove_node(self,keyval):
        head =  self.headval
        found =  False
        if head is None:
            print('empty linklist')

        else:
            head =  self.headval
            while head is not None:
                if head.dataval == keyval:
                    found = True
                    break
                prev = head

                head =  head.nextval
        
            if found:
                if prev is None:
                    self.headval = head.nextval
                else:
                    prev.nextval = head.nextval
                print(f'Node with value {keyval} removed')
            else:
                print('Key not found')


                       

            
            

            

            
            
            



list = SingleList()



list.headval = Node('mon')
list.headval.nextval = Node('tues')
list.headval.nextval.nextval = Node('web')



list.at_end(5)
# list.printlist()

list.remove_node('web')


