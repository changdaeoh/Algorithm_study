'''
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.


Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1,2], k = 2
Output: [1,2]
'''

# -------------------------------------------------
# sol1. priority queue 이용
# -------------------------------------------------
from typing import List
import collections
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    # 빈도수에 (-)를 붙인값을 키로써 힙에 저장 (-빈도, 해당 숫자)
    # 파이썬의 heapq 모듈은 최소힙(Min-Heap)만 지원하기 때문
    for key in freqs:
        heapq.heappush(freqs_heap, (-freqs[key], key))
    
    print(type(heapq))
    
    topk = list()
    # k번 추출. -> 최소힙이므로 가장작은음수(가장빈도가큰수) 순으로 추출
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1]) # 1로 인덱싱하여 숫자에 접근
    
    return topk

# -------------------------------------------------
# sol2. python style solution
# -------------------------------------------------
def topKFrequent(nums: List[int], k: int) -> List[int]:
    cnt = collections.Counter(nums)
    return [ key for key, _ in cnt.most_common(k) ]




# 가독성 별로지만 한줄컷 가능
def topKFrequent(nums: List[int], k: int) -> List[int]:
    return [ key for key, _ in collections.Counter(nums).most_common(k) ]