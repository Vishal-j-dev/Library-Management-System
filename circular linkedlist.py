class node:
    def __init__(self,d):
        self.data=d
        self.add=None
class linkedlist:
        def __init__(self):
             self.head=None
        def append(self,data):
            newnode=node(data)
            if self.head is None:
                self.head=newnode
            
            else:
                temp=self.head
                while temp.add!=self.head:
                    temp=temp.add
                temp.add=newnode
            newnode.add=self.head
        def circulardisplay(self):
             temp=self.head
             r=3
             while r>1:
                  temp=temp.add
                  r-=1
                  ptr=temp
             while temp.add!=ptr:

                  print(temp.data,end="")
                  temp=temp.add

l1=linkedlist()
while True:
    data=int(input())
    if data>=0:
         l1.append(data)
    else:
         break
l1.circulardisplay()
