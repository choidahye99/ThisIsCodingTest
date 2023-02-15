# 🔢정렬
- 데이터를 특정한 기준에 따라 순서대로 나열하는 것
- 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됨

### 💠 선택정렬
- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i] #스와프
```
    🕐 시간복잡도
       - 선택정렬은 N번만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 합니다
       - 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 N^2+N-2
       - 빅오 표기법 : O(N^2)

<br>

### 💠 삽입정렬
- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
- 선택 정렬에 비해 구현 난이도가 높은 편이지만 선택 정렬에 비해 빠르게 정렬
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): #i부터 출발해서 1까지 1씩 감소하는 문법
        if array[j] < array[j-1]: #현재 위치보다 왼쪽에 있는 데이터가 더 크면
            array[j], array[j-1] = array[j-1], array[j] #스와핑
        else: #현재 위치보다 왼쪽에 있는 데이터가 작으면
            break #그 위치에서 멈춤

print(array)
```
    🕐 시간복잡도
       - 삽입 정렬의 시간복잡도는 O(N^2)  => 반복문 두 번 중첩
       - 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
       - 최선의 경우 O(N)만큼의 시간 복잡도

<br>

### 💠 퀵정렬
- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리 근간이 되는 알고리즘
- 가장 기본적인 퀵 정렬은 첫번째 데이터를 기준 데이터(Pivot)로 설정
- 피벗을 기준으로 왼쪽에 있는 값들은 모두 피벗보다 작은 값이 되고, 오른쪽에 있는 데이터들은 모두 피벗보다 큰 데이터들이 됨
- 피벗을 기준으로 데이터 묶음을 나누는 작업을 분할(Divide)이라고 함


    퀵정렬이 빠른 이유 :
    이상적인 경우 분할이 절반씩 일어난다면, 전체 연산 횟수로 O(NlogN)을 기대할 수 있음


```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫번째 원소
    left = start+1
    right = end
    while(left <= right): #교차하기 전까지
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
```
    🕐 시간복잡도
       - 평균의 경우 O(NlogN)의 시간 복잡도를 가짐
       - 하지만 최악의 경우 O(N^2)의 시간 복잡도를 가짐



<br>

### 💠 계수 정렬 Counting Sort
- 특정한 조건이 부합할 때 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
- 계수 정렬은 데이터의 크기 범위가 제한 되어 정수 형태로 표현할 수 있을 때 사용 가능
- 데이터의 개수가 N, 데이터(양수) 중 최대값이 K일 때 최악의 경우에도 수행시간 O(N+K)를 보장
- 상대적으로 공간복잡도는 높음
```python
#모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(array)):
    for j in range(count[i]):
       print(i, end=' ')
```
    🕐 시간복잡도
       - 시간복잡도와 공간복잡도 모두 O(N+K)
       - 0과 999999999로 단 2개만의 데이터가 존재하는 경우 등 때에 따라서 심각한 비효율성 초래
       - 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용 가능

