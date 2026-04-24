Remove nodes from start to end
class Node:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None
class LinkedList:
   def __init__(self):
       self.head1 = None
       self.head2=None
   def append(self, data,head):
       newnode = Node(data)
       if self.head is None:
           self.head = newnode
       else:
           temp = self.head
           while temp.right!=None:
               temp = temp.right
           temp.right = newnode
           newnode.left = temp
   def display(self):
       temp = self.head
       while temp:
           print(temp.data, end=" ")
           temp = temp.right
       print()
    def merge(self)
