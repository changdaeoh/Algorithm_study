''' 자신을 제외한 배열의 곱
Given an integer array nums, return an array answer 
such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
* 2 <= nums.length <= 105
* -30 <= nums[i] <= 30
* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''
from typing import List


def productExceptSelf(nums:List[int]) -> List[int]
    out = []
    # 왼쪽 곰셈
    left_p = 1
    for i in range(0, len(nums)):
        out.append(left_p)
        left_p = left_p * nums[i]
    # 오른쪽 곱셈진행하면서 왼쪽 곰셈 결과들 차례로 곱하기
    right_p = 1
    for i in range(len(nums)-1, -1, -1):
        out[i] = out[i] * right_p
        right_p = right_p * nums[i]
    return out


# 시간초과 솔루션
from functools import reduce

def product_except_self(nums:list) -> list:
    res = []
    for i in range(len(nums)):
        nums_excep = [val for j,val in enumerate(nums) if j!=i]
        res.append(reduce(lambda x, y : x * y, nums_excep))
    return res