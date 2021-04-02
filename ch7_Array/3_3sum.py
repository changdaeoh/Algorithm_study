''' 세 수의 합
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []

Input: nums = [0]
Output: []

Constraints:
* 0 <= nums.length <= 3000
* -105 <= nums[i] <= 105
'''

# sol - two pointers
from typing import List

def threeSum(nums:List[int]) -> List[List[int]]:
    results = []
    nums.sort()  # 정렬이 핵심
    
    for i in range(len(nums) - 2):
        # 중복값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # i를 제외한 나머지 수열에서 간격 좁히며 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0 :
                left += 1
            elif sum > 0 :
                right -= 1
            else:
                # 정답 처리
                results.append([nums[i], nums[left], nums[right]])
                
                # 중복 쭈욱 건너뛰기
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    left += 1
                left += 1
                right -= 1
    return results

# -----------------------------------------------------------------------
# 옳지만 시간초과 솔루션 

import copy

# 2개 합이 target인 경우를 식별하는 함수
def twosum(nums:list, target:int) -> list:
    res = []
    for i, n in enumerate(nums):
        complement = target - n
        
        if complement in nums[i + 1:]:
            res.append([n, complement])
    return res

# 2개 합 식별함수 이용하여 열심히 끄적이기
def threesum(nums:list) -> list:
    res = []
    for i in range(len(nums)):
        nums_copy = copy.deepcopy(nums)
        del nums_copy[i]
        
        if len(twosum(nums_copy, -nums[i])):
            matches = [[nums[i]] + x for x in twosum(nums_copy, -nums[i])]
            for x in matches:
                if sorted(x) not in res:
                    res.append(sorted(x))
    return res

# -----------------------------------------------------------------------
# 옳지만 시간초과 솔루션 2

# 브루트 포스
def thrsum(nums:list) -> list:
    results = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:   
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]: 
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]: 
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])
        
    return results

