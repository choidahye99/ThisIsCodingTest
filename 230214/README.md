## ๐ฐ DFS
๊น์ด ์ฐ์  ํ์ Depth First Search

- ๊ทธ๋ํ์์ ๊น์ ๋ถ๋ถ์ ์ฐ์ ์ ์ผ๋ก ํ์ํ๋ ์๊ณ ๋ฆฌ์ฆ
- ์คํ ์๋ฃ๊ตฌ์กฐ(์ฌ๊ทํจ์)๋ฅผ ์ด์ฉํ๋ฉฐ, ๊ตฌ์ฒด์ ์ธ ๋์ ๊ณผ์ ์ ๋ค์๊ณผ ๊ฐ์
  - ํ์ ์์ ๋ธ๋๋ฅผ ์คํ์ ์ฝ์ํ๊ณ  ๋ฐฉ๋ฌธ ์ฒ๋ฆฌ
  - ์คํ์ ์ต์๋จ ๋ธ๋์ ๋ฐฉ๋ฌธํ์ง ์์ ์ธ์ ํ ๋ธ๋๊ฐ ํ๋๋ผ๋ ์์ผ๋ฉด ๊ทธ ๋ธ๋๋ฅผ ์คํ์ ๋ฃ๊ณ  ๋ฐฉ๋ฌธ ์ฒ๋ฆฌ
  - ๋ฐฉ๋ฌธํ์ง ์์ ์ธ์ ๋ธ๋๊ฐ ์์ผ๋ฉด ์คํ์์ ์ต์๋จ ๋ธ๋ค๋ฅผ ๊บผ๋
  - ๋์ด์ ์ ๊ณผ์ ์ ์ํํ  ์ ์์ ๋๊น์ง ๋ฐ๋ณต
```python
#DFS ๋ฉ์๋ ์ ์
def dfs(graph, v, visited):
    #ํ์ฌ ๋ธ๋๋ฅผ ๋ฐฉ๋ฌธ์ฒ๋ฆฌ
    visited[v] = True
    print(v, end=' ')
    for i in graph:
        if not visited[i]:
            dfs(graph, i, visited)

#์ธ์  ๋ฆฌ์คํธ ๋ฐฉ์์ผ๋ก ๊ทธ๋ํ ํํ
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

#๊ฐ ๋ธ๋๊ฐ ๋ฐฉ๋ฌธ๋ ์ ๋ณด๋ฅผ ํํ (1์ฐจ์ ๋ฆฌ์คํธ)
visited = [False] * 9 #์ธ๋ฑ์ค 0์ ์ฌ์ฉํ์ง ์๊ธฐ ๋๋ฌธ์ ๋ธ๋๋ณด๋ค +1 ํฌ๊ธฐ๋ก ๋ฐฉ๋ฌธ ๋ฐฐ์ด ํฌ๊ธฐ ์ง์ 

#์ ์๋ dfs ํจ์ ํธ์ถ
dfs(graph, 1, visited)
```

## ๐ฐ BFS
๋๋น ์ฐ์  ํ์ Breadth-First Search

- ๊ทธ๋ํ์์ ๊ฐ๊น์ด ๋ธ๋๋ถํฐ ์ฐ์ ์ ์ผ๋ก ํ์ํ๋ ์๊ณ ๋ฆฌ์ฆ
- BFS๋ ํ ์๋ฃ๊ตฌ์กฐ๋ฅผ ์ด์ฉํ๋ฉฐ, ๊ตฌ์ฒด์ ์ธ ๋์ ๊ณผ์ ์ ๋ค์๊ณผ ๊ฐ์
  - ํ์ ์์ ๋ธ๋๋ฅผ ํ์ ์ฝ์ํ๊ณ  ๋ฐฉ๋ฌธ ์ฒ๋ฆฌ๋ฅผ ํจ
  - ํ์์ ๋ธ๋๋ฅผ ๊บผ๋ธ ๋ค์ ํด๋น ๋ธ๋์ ์ธ์  ๋ธ๋ ์ค์์ ๋ฐฉ๋ฌธํ์ง ์์ ๋ธ๋๋ฅผ ๋ชจ๋ ํ์ ์ฝ์ํ๊ณ  ๋ฐฉ๋ฌธ์ฒ๋ฆฌ
  - ๋์ด์ ์์ ๊ณผ์ ์ ์ํํ  ์ ์์ ๋๊น์ง ๋ฐ๋ณต

```python
from collections import deque

#BFS ๋ฉ์๋ ์ ์
def bfs(graph, start, visited):
    #ํ ๊ตฌํ์ ์ํด deque ๋ผ์ด๋ธ๋ฌ๋ฆฌ ์ฌ์ฉ
    queue = deque()
    #ํ์ฌ ๋ธ๋ ๋ฐฉ๋ฌธ์ฒ๋ฆฌ
    visited[start] = True
    #ํ๊ฐ ๋น ๋๊น์ง ๋ฐ๋ณต
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]: #v์ ์ฐ๊ฒฐ๋ ๋ธ๋๋ค์ ๋๋ฉด์
            if not visited[v]: #๋ฐฉ๋ฌธํ์ง ์์ ๋ธ๋๊ฐ ์๋ค๋ฉด
                queue.append(i) #ํ์ ๋ธ๋ ์ฝ์
                visited[i] = True #๋ฐฉ๋ฌธ์ฒ๋ฆฌ


#์ธ์  ๋ฆฌ์คํธ ๋ฐฉ์์ผ๋ก ๊ทธ๋ํ ํํ
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

#๊ฐ ๋ธ๋๊ฐ ๋ฐฉ๋ฌธ๋ ์ ๋ณด๋ฅผ ํํ (1์ฐจ์ ๋ฆฌ์คํธ)
visited = [False] * 9 #์ธ๋ฑ์ค 0์ ์ฌ์ฉํ์ง ์๊ธฐ ๋๋ฌธ์ ๋ธ๋๋ณด๋ค +1 ํฌ๊ธฐ๋ก ๋ฐฉ๋ฌธ ๋ฐฐ์ด ํฌ๊ธฐ ์ง์ 

#์ ์๋ dfs ํจ์ ํธ์ถ
bfs(graph, 1, visited)
```


