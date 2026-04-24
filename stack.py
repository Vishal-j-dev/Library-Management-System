class node:
    def __init__(self,d):
        self.data=d
        self.add=None
class linkedlist:
        def __init__(self):
             self.head=None
        def append(self,data):
            newnode=node(data)
            newnode.add=self.head
            self.head=newnode
        def display(self):
            temp=self.head
            while temp != None:
                 print(temp.data,end=" ")
                 temp=temp.add
l1=linkedlist()
while True:
    data=int(input())
    if data>=0:
         l1.append(data)
    else:
         break;
l1.display()
     