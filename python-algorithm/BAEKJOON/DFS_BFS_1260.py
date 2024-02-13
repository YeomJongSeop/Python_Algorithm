from collections import deque
# 정점 개수 N, 간선의 개수 M, 탐색 시작할 정점번호 V
n,m,v = map(int, input().split())

for k in range(n):
    graph = [[] for _ in range(n+1)] # 그래프를 인접 리스트로 표햔

visited = [False] * m

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 재귀적으로 방문
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, v, visited)