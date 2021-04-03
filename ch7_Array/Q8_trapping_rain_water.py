'''빗물 트래핑
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
* n == height.length
* 0 <= n <= 3 * 104
* 0 <= height[i] <= 105
'''

# sol 1. global maximum으로 수렴하는 두 포인터 활용 활용
def trap(height:list) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        # 매번 포인터 이동 후 max값 갱신
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        # 좌 우 max값 비교 후 포인터 이동 
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


# sol 2. 스택 쌓기
def trap(height:list) -> int:
    stack = []
    volumne = 0
    
    for i in range(len(height)):
        # stack에 원소가 있고, stack의 가장 최근 원소보다 현재값의 높이가 더 큰경우높이가 더 큰경우
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if len(stack) == 0:
                break
            
            distance = i - stack[-1] -1                               # 가로
            waters = min(height[i], height[stack[-1]]) - height[top]  # 세로
            volume += distance * waters
        
        stack.append(i)                                               # 현재 idx는 항상 쌓임
    return volumn
            
