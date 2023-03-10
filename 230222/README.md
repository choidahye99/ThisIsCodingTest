### ❤ 다이나믹 프로그래밍
- 메모리를 적절히 사용하여 수행시간 효율성을 비약적으로 향상
- 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 함
- 다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식(탑다운, 바텀업)으로 구성

다이나믹 프로그램은 동적계획법이라고도 부릅니다.
다이나믹 프로그래밍은 다음 조건을 만족할 때 사용할 수 있습니다.<br>
<br>
(1) 최적 부분 구조 <br>
: 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있습니다.
<br>
<br>
(2) 중복되는 부분 문제 <br>
: 동일한 작은 문제를 반복적으로 해결해야 합니다.

#### Example ) 피보나치 수열

#### 탑다운 vs 바텀업
- 탑타운(메모이제이션) : 하향식 
<br>
✅ 메모이제이션 Memoization
<br> : 한 번 계산한 결과를 메모리 공간에 메모하는 기법
  - 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옴
  - 값을 기록해놓는다는 점에서 캐싱(Caching)이라고 함
  - 엄밀히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해놓은 넓은 개념
  - 따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아님
  - 한 번 계산된 결과를 담아놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있음
<br>
<br>
- 바텀업 : 상향식
  - 다이나믹 프로그래밍의 전형적 형태
  - 결과 저장용 리스트는 DP 테이블이라고 함

```python
#피보나치 수열 : 탑다운
d = [0] * 100 #한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화

def fibo(x):
    if x == 1 or x == 2: #종료 조건
        return 1

    #이미 계산한 적 있는 문제는 그대로 반환
    if d[x] != 0:
        return d[x]
    #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
```

```python
#피보나치 수열 : 바텀업
d = [0]*100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
```

