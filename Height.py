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

    def height(self,root):
        if root==None:
            return 0
        lheight=self.height(root.left)
        rheight=self.height(root.right)
        return max(lheight,rheight)+1
    

    def lca(self,n1,n2):
        temp=self.root
        if temp is None:
            return -1
        while True:
            if n1<temp.data and n2<temp.data:
                temp-temp.left
            elif n1>temp.data and n2>temp.data:
                temp=temp.right
            elif n1<temp.data and n2>temp.data:
                return temp.data
            elif (n1>temp.data and n2<temp.data) or (n1==temp.data or n2==temp.data):
                return temp.data
            else:
                return -1
    
    def add(self):
        
        que=deque()
        sum=0
        que.append(self.root)
        while que:
            temp=que.popleft()
            if (temp.left!=None and temp.right==None) or (temp.left==None and temp.right!=None):
                sum+=temp.data
            if temp.left!=None:
                que.append(temp.left)
            if temp.right!=None:
                que.append(temp.right)
        return sum

    def deleteSingleChild(self):
        que = deque()
        que.append([self.root, None])
        while que:
            curr, parent = que.popleft()
            if (curr.left and curr.right is None) or (curr.right and curr.left is None):
                if curr.left:
                    child = curr.left
                else:
                    child = curr.right
                if parent is None:
                    self.root = child
                else:
                    if curr == parent.left:
                        parent.left = child
                    else:
                        parent.right = child
            if curr.left:
                que.append([curr.left, curr])
            if curr.right:
                que.append([curr.right, curr])
  
a=treee()
while True:
    data=int(input())
    if data>=0:
        a.append(data)
    else:
        break
a.bfs()