# N(세로), M(가로) 입력받기
n, m = map(int(input().split()))

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# DFS로 특정 노드 방문 뒤 연결된 모든 노드 방문
def dfs(x, y):
    # 주어진 범위 벗어나면 즉시 종료( x,y는 N M 의 좌표 )
    if x <= -1 or x >= n  or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 모두 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드(위치)에 대해 음료 채우기
count = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            count += 1

print(count) # 정답 출력
