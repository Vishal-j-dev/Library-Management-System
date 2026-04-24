from collections import deque
class Node:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class treeNode:
    def _init_(self):
        self.root=None
    
    def append(self,data):
        newNode = Node(data)
        temp=self.root
        if self.root ==None:
            self.root = newNode
        else:
            while True:
                if data<temp.data:
                    if temp.left!=None: 
                        temp=temp.left
                    else:
                        temp.left=newNode
                        break
                if data>temp.data:
                    if temp.right!=None:
                        temp=temp.right
                    else:
                        temp.right=newNode
                        break

    def inorderDisplay(self,root):
        if root is None:
            return
        self.inorderDisplay(root.left)
        print(root.data)
        self.inorderDisplay(root.right)

    def mirrorTree(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.reverseTree(root.left)
        self.reverseTree(root.right)

    def bfs(self,root):
        queue=deque()
        queue.append(self.root)
        while queue:
            temp=queue.popleft()
            print(temp.data,end=' ')
            if temp.left != None:
                queue.append(temp.left)
            if temp.right!=None:
                queue.append(temp.right)

    
        
a=treeNode()

i=1
while True:

    print (i,end=)
    value=int(input())
    if value <0:
        break
    a.append(value)
    i+=1
a.mirrorTree(a.root)
a.bfs(a.root)
