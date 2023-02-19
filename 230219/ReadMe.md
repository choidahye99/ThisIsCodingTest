### ▶▶▶ 이진 탐색 알고리즘
- 순차탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
- 이진탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
  - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색범위를 설정합니다

```python
#재귀함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid)
    else:
        return binary_search(array, target, mid, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)
```
```python
#반복문
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)
```

#### ✨ 파이썬 이진 탐색 라이브러리
- bisect_left(a, x)
  - 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a, x)
  - 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) #결과 : 2
print(bisect_right(a, x)) #결과 : 4
```
✔ (bisect_right(a, x)) - (bisect_left(a, y)) : 배열 a에서 x와 y 사이에 있는 값의 개수를 알 수 있음

```python
#값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4)) #값이 4인 데이터 개수 출력 (결과 : 2)
print(count_by_range(a, -1, 3)) #값이 -1에서 3 사이에 있는 데이터 개수 출력 (결과 : 6)
```

#### ✨ 파라메트릭 서치 Parametric Search
- 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
  - 예시 : 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결

