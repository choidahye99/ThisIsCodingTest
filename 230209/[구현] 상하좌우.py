#구현

n = int(input())

travel_map = [[0]*n for i in range(n)]

x, y = 0, 0

dir = list(input().split())

for i in dir:
    if i == 'R':
        if y+1 < n:
            y += 1
    elif i == 'L':
        if y-1 >= 0:
            y -= 1
    elif i == 'U':
        if x-1 >= 0:
            x -= 1
    else:
        if x+1 < n:
            x += 1

print(x+1, y+1)
