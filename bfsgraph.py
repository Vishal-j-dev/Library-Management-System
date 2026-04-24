from collections import defaultdict,deque
from queue import PriorityQueue
class graph:
    def __init__ (self):
        self.adjlist = defaultdict(list)
    def add_edge(self, src, dist,w):
        self.adjlist[src].append((dist,w))
    def display(self):
        for src,dist in sorted(self.adjlist.items()):
            print(src,"=>",dist)
    def bfs(self,src):
        visited=set()
        que=deque()
        que.append(src)
        visited.add(src)
        while que:
            src=que.popleft()
            for dist in self.adjlist[src]:
                if dist not in visited:
                    visited.add(dist)
                    que.append(dist)

        for node in visited:
            print(node,end=" ")

    def dfs(self,src,visited=None):
        if visited is None:
            visited=set()
        visited.add(src)
        print(src,end=" ")
        for dist in self.adjlist[src]:
            if dist not in visited:
                self.dfs(dist,visited)

    def dijkstra(self,src):
        pque=PriorityQueue()
        node=set(self.adjlist.keys())
        for u in self.adjlist:
            for v,_ in self.adjlist[u]:
                node.add(v)
            dist={}
            for u in node:
                dist[u]=float('inf')
            dist[src]=0
            pque.put((0,src))
            while not pque.empty():
                d,u=pque.get()
                for v,w in self.adjlist[u]:
                    if dist[u]+w<dist[v]:
                        dist[v]=dist[u]+w
                        pque.put((dist[v],v))
            for node in dist.items:
                print(node)        

a=graph()
while True:
    src,dist,w=map(int,input().split())
    if src >= 0 and dist >= 0:
        a.add_edge(src, dist,w)
    else:
        break
a.dijkstra(1)