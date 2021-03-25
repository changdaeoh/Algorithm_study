'''
뒤집어도 똑같은 문자열 식별하기 (숫자, 영어, 특수문자만 input된다고 가정 )

input_sample = "A man, a plan, a canal: Panama"
output_sample = True

input_sample2 = "race a car"
output_sample = False
'''
# sol 1. 정규표현식 이용
input_sample = "A man, a plan, a canal: Panama"

import re

def Panlindrome_discriminator_re(text : str ) -> bool:
    text = text.lower()
    text = re.sub('[^a-z0-9]', '',text)
    
    # if len(text) == 0:                   # 예외처리는 어느정도까지 해야되는가?
    #     return False
    
    return text == text[::-1]

print(Panlindrome_discriminator_re(input_sample))

# -------------------------------------------------------------------------------

# sol 2. 리스트로 변환

def isPalindrome(s : str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():                 # 숫자, 알파벳 식별하는 메서드 isalnum
            strs.append(char.lower())
        
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():      # 앞 뒤로 하나씩 순차적으로 꺼내 비교
            return False
    
    return True


# 3. 덱(Deque) 자료형을 이용한 최적화
import collections

def isPalindrome(s : str) -> bool:
    strs : Deque = collections.deque()      # 요런애도있네
        
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
            
    while len(strs) > 1:
        if strs.popleft() != strs.pop():    # pop(0)은 복잡도 O(n) popleft()는 O(1)
            return False
    
    return True