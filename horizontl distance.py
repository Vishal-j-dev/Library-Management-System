from collections import deque,defaultdict
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class treeNode:
    def __init__(self):
        self.root=None
    
    def append(self,data):
        newnode=Node(data)
        
        if self.root==None:
            self.root=newnode
        else:
            temp=self.root
            while True:
                if data<temp.data:
                    if temp.left!=None: 
                        temp=temp.left
                    else:
                        temp.left=newnode
                        break
                if data>temp.data:
                    if temp.right!=None:
                        temp=temp.right
                    else:
                        temp.right=newnode
                        break
    
    def vs(self):
        q=deque()
        q.append((self.root,0))
        res=defaultdict(list)
        while q:
            cn,hd=q.popleft()
            if cn.left!=None:
                q.append((cn.left,hd-1))
            if cn.right!=None:
                q.append((cn.right,hd+1))
            res[hd].append(cn.data)

        for hd, node in sorted(res.items()):
            print(hd,"->",node)


a=treeNode()
while True:
    data=int(input())
    if data>0:
        a.append(data)
    else:
        break

a.vs()