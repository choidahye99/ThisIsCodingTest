#효율적인 화폐 구성
#N가지 종류의 화폐가 있는데, 그 가치의 합이 M원이 되도록 하기 위한 최소한으로 사용해야 하는 화폐 개수는?

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001]*(m+1)

d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])