#두 배열의 원소 교체

n, k = map(int, input().split())

arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA.sort() #오름차순 정렬
arrayB = sorted(arrayB, reverse=True) #내림차순 정렬 arrayB.sort(reverse=True)

for i in range(k):
    if arrayA[i] < arrayB[i]: #[주의]A배열의 값이 B배열의 값보다 작을때에만 교차 수행
        arrayA[i] = arrayB[i]
    else:
        break #쓸데없는 연산을 줄여주는 key

answer = sum(arrayA)

print(answer)


