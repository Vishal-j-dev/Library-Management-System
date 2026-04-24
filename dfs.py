class node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None
class treee:
    def __init__(self):
        self.root=None
    def append(self,data):
        newnode=node(data)
        if temp is None:
            self.root=newnode
        else:
            temp=self.root
            while true:
                if data<temp.data:
                    if temp.left!=None:
                        temp=temp.left
                    else:
                        temp.left=newnode
                else:
                    if temp.right!=None:
                        temp=temp.right
                    else:
                        temp.right=newnode

def inordertraversal(self,root):
    if root == None:
        return
    self.inordertraversal(root.left)
    print(root.data,end=" ")
    self.inordertraversal(root.right)

l1=treee()
while True:
    data=int(input())
    if data>=0: 
         l1.append(data)
    else:
         break``
l1.inordertraversal
    