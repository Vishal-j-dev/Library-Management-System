Remove nodes from start to end
class Node:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None
class LinkedList:
   def __init__(self):
       self.head = None
   def append(self, data):
       newnode = Node(data)
       if self.head is None:
           self.head = newnode
       else:
           temp = self.head
           while temp.right!=None:
               temp = temp.right
           temp.right = newnode
           newnode.left = temp
   def display(self,head):
       temp = self.head
       while temp:
           print(temp.data, end=" ")
           temp = temp.right
       print()
   def delete(self,start,end):
       temp = self.head
       diff=end-start
       while start>1:
           temp=temp.right
           start=start-1
       p1=temp.left
       ptr=temp
       while diff>=1:
           ptr=ptr.right
           diff-=1
       p2=ptr.right
       p1.right=p2
       p2.left=p1
if __name__ == "__main__":
   list=LinkedList()
   while True:
       data=int(input())
       if data>=0:
           list.append(data)
       else:
           break
   print("List values before deletion:")
   list.display()
   start=2
   end=5
   list.delete(start,end)
   print("List values after deletion:")
   list.display()

