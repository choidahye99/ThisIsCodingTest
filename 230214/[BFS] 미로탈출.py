#BFS는 간선의 비용이 모두 같을 때 사용할 수 있는 최단거리 알고리즘
#BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색
#상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일
#따라서 (1, 1)지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있음

from collections import deque

#BFS 코드 구현
def bfs(x, y):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    #queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:  # 처음 방문하는 노드일때만 기록
                graph[nx][ny] = graph[x][y] + 1  # 다음 노드는 이전 노드보다 비용 증가
                queue.append((nx, ny))
    #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]


#N, M을 공백 기준으로 구분하여 입력받기
n, m = map(int, input().split())
#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS를 수행한 결과 출력
print(bfs(0, 0))
