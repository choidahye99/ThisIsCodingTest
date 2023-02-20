#이진탐색

#떡의 개수(n)과 요청한 떡의 길이(m)을 입력
n, m = map(int, input().split())
#각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

array.sort()

#이진탐색을 위한 시작점과 끝점 설정
left = 0
right = array[n-1]

#이진 탐색 수행
result = 0
while left <= right:
    mid = (left+right)//2

    sum_ = 0
    for i in array:
        if i >= mid:
            sum_ += i-mid

    if sum_ > m:
        left = mid+1
    else:
        right = mid-1

print(result)
