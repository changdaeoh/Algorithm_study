'''
가장 긴 팰린드롬 부분 문자열
Given a string s, return the longest palindromic substring in s.

# Examples:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"

# Constraints:

* 1 <= s.length <= 1000
* s consist of only digits and English letters (lower-case and/or upper-case),
'''

text1 = "eagasg00gsoa22"
text2 = "eagasg0ddaca0avasdncascgsoa22asvasvasvasvasvasasdaaddaaaacac35sfaw46qna9kr2301rjma22dmrnsd"

# Use 2 pointer expanded from center
def longestPalindrome(s: str) -> str:
    # 윈도우에서 매칭되면 확장시작
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1 : right -1]
    
    # 예외처리
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    # 슬라이딩
    for i in range(len(s)-1):
        result = max(result, 
                     expand(i, i+1),
                     expand(i, i+2),
                     key = len)
    
    return result

longestPalindrome(text2)


# inefficient solution
def longest_palindrome(text: str) -> str:
    result = ''; max_len = 0
    for i in range(len(text)-1):
        for j in range(i,len(text)):
            subtext = text[i:j+1]
            if (subtext == subtext[::-1]) and (len(subtext) > max_len):
                max_len = len(subtext)
                result = subtext

    return result
    
longest_palindrome(text2)


# -----------------------------------------------
import time

start1 = time.time() 
for i in range(10000):
    longest_palindrome(text2)
end1 = time.time()

start2 = time.time() 
for i in range(10000):
    longestPalindrome(text2)
end2 = time.time()

print(f'func1 running time : {end1 - start1}')  
print(f'func2 running time : {end2 - start2}')  