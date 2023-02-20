#파이썬 라이브러리 사용 이진탐색

from bisect import bisect_left, bisect_right

#값이 [left_value, right_value]인 데이터 개수를 반환하는 하무
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)