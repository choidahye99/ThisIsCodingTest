n = input()

lst = list(map(int, n))

result = 0
for i in lst:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i

print(result)

