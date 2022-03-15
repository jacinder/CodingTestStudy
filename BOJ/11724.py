import sys

sys.setrecursionlimit(10000000)

temp = sys.stdin.readline()
node, edge = map(int, temp.split())

visited = [False]*(node+1)
graph = [[]*(node+1) for _ in range(node+1)]
for _ in range(edge):
  i,j = map(int, sys.stdin.readline().split())
  graph[i].append(j)
  graph[j].append(i)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

answer = 0
for v in range(1, node+1):
    if not visited[v]:
        answer += 1  
        dfs(v)

print(answer)
