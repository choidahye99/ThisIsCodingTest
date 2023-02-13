## 💠스택 with Python

- 선입선출 (먼저 들어 온 데이터가 나중에 나가는 형식)
- 리스트로 구현

```python
stack = []
#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()

print(stack)
#결과 [5, 2, 3] : 최하단 원소부터 출력
#선입선출로 출력하고 싶다면
    #print(stack[::-1])
    #결과 [3, 2, 5]
```

## 💠큐 with Python
- 선입선출 (먼저 들어 온 데이터가 먼저 나가는 형식)
- deque 라이브러리 사용
  - 리스트로 큐를 구현할 수 있지만, 시간복잡도를 고려했을 때 좋지 않은 선택

```python
from collections import deque
#QUEUE 큐 구현을 위해 deque 라이브러리 사용
queue = deque()
#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제()
queue.append(5) #가장 오른쪽 위치에 원소 추가 #시간복잡도 O(1)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #원소가 왼쪽으로 나감

#print(queue) : 먼저 들어온 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue)
#결과 [2, 3, 7]
```