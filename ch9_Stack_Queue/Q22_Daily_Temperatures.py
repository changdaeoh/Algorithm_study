''' 따뜻한 날씨 찾기 
Given a list of daily temperatures T, return a list such that, 
for each day in the input, tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: 
* The length of temperatures will be in the range [1, 30000]. 
* Each temperature will be an integer in the range [30, 100].
'''

# 인덱스 스택을 쌓아가며 매시점 기온비교
def warmdays(T:list) -> list:
    answer = [0] * len(T)                    # 디폴트값을 0 으로 미리 채워둠 
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]] : # stack의 마지막 인덱스에서의 온도보다 현재온도가 높으면
            last = stack.pop()               
            answer[last] = i - last          # 더 따뜻한 날과 해당 날의 일수 차 
        stack.append(i)
    return answer
# stack에서 pop되지 못한(보다 높은 기온이 없는경우) index부분의 answer는 0이 됨.

# 1개의 루프와 STACK을 이용한 조건부 순회로 시간복잡도 줄이기 
# 특정시점 이후 모든 요소들에 접근하지 않고 1번의 비교로 해결되는 경우가 있으므로 
# 시간을 단축할 수 있는 것.



# 시간 초과 풀이 (브루트포스)
def warmdays(T:list) -> list:
    res = []
    
    for i in range(len(T) - 1):
        day = 0
        for j in range(i+1,len(T)):
            if T[i] < T[j]:
                day = j - i
                break 
        res.append(day)
    res.append(0)
    return res