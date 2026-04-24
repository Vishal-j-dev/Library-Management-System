from queue import PriorityQueue
from collections import defaultdict, deque


class Graph:
  def __init__(self):
      self.adj_list = defaultdict(list)
  def addEdge(self, src, dest,weight):
      self.adj_list[src].append((dest,weight))
  def dijkstra(self,src):
      pqueue = PriorityQueue()
      nodes=set(self.adj_list.keys())
      for u in self.adj_list:
          for v,_ in self.adj_list[u]:
              nodes.add(v)
      dist={}
      for u in nodes:
          dist[u]=float('inf')
      dist[src] = 0
      pqueue.put((0, src))
      while not pqueue.empty():
          d,u=pqueue.get()
          for v,weight in self.adj_list[u]:
              if dist[u]+weight < dist[v]:
                  dist[v]=dist[u]+weight
                  pqueue.put((dist[v],v))
      for node in dist.items():
          print(node)


if __name__ == '__main__':
  g=Graph()
  while True:
      src,dest,weight=map(int,input().split())
      if src>=0 and dest>=0:
          g.addEdge(src,dest,weight)
      else:
          break
  g.dijkstra(1)
