#그리디

n, k = map(int, input().split())

result = 0
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k  # n이 k로 나누어 떨어지는 수 중에 가장 가까운 수
    result += (n - target)  # 1로 빼야하는만큼 결과에 추가
    n = target

    if n < k:  # 반복문 탈출 조건
        break;  # N이 K보다 작을 때 (더이상 나눌 수 없을 때 반복문 탈출)

    result += 1
    n //= k  # k로 나누기
    # 1이상 k미만의 수가 return

# n이 1보다 크니 남은 수에 대해서 1을 빼준만큼 더해줘야 합니다람쥐
result += (n - 1)

print(result)