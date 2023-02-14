## 🔰 DFS
깊이 우선 탐색 Depth First Search

- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 자료구조(재귀함수)를 이용하며, 구체적인 동작 과정은 다음과 같음
  - 탐색 시작 노드를 스택에 삽입하고 방문 처리
  - 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리
  - 방문하지 않은 인접노드가 없으면 스택에서 최상단 노들를 꺼냄
  - 더이상 위 과정을 수행할 수 없을 때까지 반복
```python
#DFS 메서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    for i in graph:
        if not visited[i]:
            dfs(graph, i, visited)

#인접 리스트 방식으로 그래프 표현
graph = [
    [],
    [2, 3, 7],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9 #인덱스 0은 사용하지 않기 때문에 노드보다 +1 크기로 방문 배열 크기 지정

#정의된 dfs 함수 호출
dfs(graph, 1, visited)
```

## 🔰 BFS
너비 우선 탐색 Breadth-First Search

- 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
- BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같음
  - 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
  - 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
  - 더이상 위의 과정을 수행할 수 없을 때까지 반복

```python
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    #현재 노드 방문처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]: #v와 연결된 노드들을 돌면서
            if not visited[v]: #방문하지 않은 노드가 있다면
                queue.append(i) #큐에 노드 삽입
                visited[i] = True #방문처리


#인접 리스트 방식으로 그래프 표현
graph = [
    [],
    [2, 3, 7],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9 #인덱스 0은 사용하지 않기 때문에 노드보다 +1 크기로 방문 배열 크기 지정

#정의된 dfs 함수 호출
bfs(graph, 1, visited)
```


