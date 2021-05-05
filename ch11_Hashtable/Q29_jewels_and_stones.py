'''
You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".


Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Input: jewels = "z", stones = "ZZ"
Output: 0

Constraint
* 1 <= jewels.length, stones.length <= 50
* jewels and stones consist of only English letters.
* All the characters of jewels are unique.
'''

# sol1. Counter 이용한 풀이
import collections
def jewels_cnt(J:str, S:str) -> int:

    cnt = collections.Counter(S)
    return sum(cnt[j] for j in J)


# sol2.1 파이썬 리스트 이용 풀이 1
def jewels_cnt(jewels:str, stones:str) -> int:
    return len([ s for s in stones if s in jewels ])

# sol2.2 파이썬 리스트 이용 풀이 2
def jewels_cnt(jewels:str, stones:str) -> int:
    return sum(s in jewels for s in stones)


# sol3. 해쉬테이블 이용
import collections

def jewels_cnt(J:str, S:str) -> int:
    freqs = collections.defaultdict(int)
    count = 0
    
    # 돌에 포함된 원석별 빈도수 계산
    for char in S:
        freqs[char] += 1
    
    # 돌에 박힌 보석들 개수 카운팅
    for char in J:
        if char in freqs:
            count += freqs[char]
    
    return count