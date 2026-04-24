from collections import defaultdict,deque
class graph:
    def __init__ (self):
        self.adjlist = defaultdict(list)
    def add_edge(self, src, dist,weight):
        self.adjlist[src].append(dist,weight)
        self.adjlist[dist].append(src)
    def display(self):
        for src,dist in sorted(self.adjlist.items()):
            print(src, "->", dist)
    
a=graph()
while True:
    src,dist,weight=map(int,input().split())
    if src >= 0 and dist >= 0:
        a.add_edge(src, dist,weight)
    else:
        break

a.bfs()
# You can print the adjacency list if needed
# print(dict(a.adjlist))