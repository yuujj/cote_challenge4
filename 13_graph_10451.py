t = int(input())

def dfs(graph, v, visited):
    if visited[v]:
        return None
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return 'Done'

for _ in range(t):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)

    graph = [[] for _ in range(n+1)]
    for u, v in enumerate(nums):
        graph[u].append(v)
        graph[v].append(u)

    result = 0
    for num in range(1, n+1):
        if dfs(graph, num, visited) != None:
            result += 1
    print(result)