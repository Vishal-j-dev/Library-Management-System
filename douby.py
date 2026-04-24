class node:
    def __init__(self,d):
        self.data=d
        self.right=None
        self.left=None
class linkedlist:
        def __init__(self):
             self.head=None
             self.tail=None
        def append(self,data):
            newnode=node(data)
            if self.head is None:
                self.head=newnode
            else:
                temp=self.head
                while temp.right!=None:
                    temp=temp.right
                temp.right=newnode
        def forwarddisplay(self):
             temp=self.head
             while temp!=None:
                  print(temp.data,end=" ")
                  temp=temp.right
            print()
        def reversedisplay(self):
             temp=self.tail
             print("reverse")
             while temp!=None:
                  print(temp,data,end=" ")
                  temp=temp.left


l1=linkedlist()
while True:
    data=int(input()) 
    if data>=0:
         l1.append(data)
    else:
         break
l1.forwarddisplay()
l1.reversedisplay()