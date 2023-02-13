# 왕실의 나이트
    # 리스트를 이용하여 8가지 방향에 대한 델타를 정의하고 확인

#현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1   #ord(문자) : 하나의 문자를 인자로 받고, 문자에 해당하는 유니코드 정수 반환 [ex] ord('a') = 97

#나이트가 이동할 수 있는 8가지 방향 정의
    #di, dj로 1차원 배열을 두 개 만들거나, 그게 싫다면 한 번에 받아도 됨
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    nxt_row = row+step[0] # 이동하고자 하는 위치 확인
    nxt_column = column+step[1]

    #해당 위치로 이동이 가능하다면 카운트 증가
    if nxt_row >= 1 and nxt_column >= 1 and nxt_row <= 8 and nxt_column <= 8:
        result += 1

print(result)
