#한 마을에 모험가가 n명 있습니다.
#모험가 길드에서는 n명의 모험가를 대상으로 공포도를 측정했는데, 공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
#모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
#동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다.
#n명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최대값을 구하는 프로그램을 작성하시오.

n = map(int, input())
arr = list(map(int, input().split()))

arr.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함되는 모험가의 수

for i in arr:
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면
        result += 1 #그룹 결정
        count = 0 #현재 그룹에 포함된 모험가의 수 초기화


print(result) #총 그룹의 수 출력