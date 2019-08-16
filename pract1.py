graph1={
    'A': set(['B','C']),
    'B': set(['A','D','E']),
    'C': set(['A','F']),
    'D': set(['B']),
    'E': set(['B','F']),
    'F': set(['c','E'])
}
def bfs_path(graph,start,goal):
 queue=[(start,[start])]
 while queue:
       (vertex,path)=queue.pop(0)
       for next in graph[vertex]-set(path):
          if next == goal:
             yield path+[next]
          else:
              queue.append((next,path+[next]))
result=list(bfs_path(graph1,'A','F'))
print(result)
