import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    if visited[v]:
        return None
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return 'Done'

result = 0
for num in range(1, n+1):
    if dfs(graph, num, visited) != None:
        result += 1
print(result)