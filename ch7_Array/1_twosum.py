'''두 수의 합
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
* 2 <= nums.length <= 103
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* Only one valid answer exists.
'''
# input sample
nums = [2, 7, 11, 15]
target = 9
nums = [3, 3]
target = 6


# sol 1. Brute-Force
def twosum(nums:list, target:int) -> list:
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            

# sol 2. searching via "in" - - - best on leetcode
def twosum(nums:list, target:int) -> list:
    for i, n in enumerate(nums):
        complement = target - n
        
        if complement in nums[i + 1:]:
            return [i, nums[i+1:].index(complement) + (i+1)] 
            # 그냥 num.index하면 중복 원소채택될 수 있음
        

# sol 3. key inquire
def twosum(nums:list, target:int) -> list:
    nums_map = {}
    # 값을 key로 인덱스를 value로
    for i, num in enumerate(nums):
        nums_map[num] = i
    # dictionary의 key조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [nums.index(num), nums_map[target - num]]
    
