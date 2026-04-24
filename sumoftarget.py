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
                if data > temp.data:
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
        listvalue=[]
        while que:
            temp=que.popleft()
            listvalue.append(temp.data)
            if temp.left!=None:
                que.append(temp.left)
            if temp.right!=None:
                que.append(temp.right)
        return listvalue
    def add(self):
        k=130

a=treee()
while True:
    data=int(input())
    if data>=0:
        a.append(data)
    else:
        break
a.bfs()
print(sorted(a.bfs()))