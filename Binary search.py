from collections import deque
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
        if self.root is None:
            self.root=newnode
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left is not None:
                        temp = temp.left
                    else:
                        temp.left = newnode
                        break
                else:
                    if temp.right is not None:
                        temp = temp.right
                    else:
                        temp.right = newnode
                        break
    
    def bfs(self):

        que=deque()
        que.append(self.root)
        while que:
            temp=que.popleft()
            print(temp.data,end=" ")
            if temp.left!=None:
                que.append(temp.left)
            if temp.right!=None:
                que.append(temp.right)
a=treee()

while True:
    value=int(input())
    if value<0:
        break
    a.append(value)
if a.root is not None:
    a.bfs()
else:
    print("Tree is empty.")