#DFS : 음료수 얼려먹기

def dfs(x, y):
    #주어진 범위를 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 #해당 노드 방문처리
        #상하좌우 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True #들어갔다가 나오면(최상단 노드까지 돌아오면) 하나의 얼음이므로 True
    return False #마지막칸까지 갔다~~는 뜻

n, m = map(int, input().split())

# ice = [[0]*m for i in range(n)]
#
# for i in range(n):
#     str = list(input())
#     idx=0
#     for j in str:
#         ice[i][idx] = int(j)
#         idx += 1

#2차원 리스트의 맴 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs 수행
        if dfs(i, j) == True:
            result += 1

print(result)