'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# ---------------------------------------------------
# sol1. two pointers with implicit sliding window
# ---------------------------------------------------
def lengthOfLongestSubstring(self, s: str) -> int:
    used = {}                                    
    max_length = start = 0                       # 최대길이, 인덱스 포인터
    for index, char in enumerate(s):
        if char in used and start <= used[char]: # 윈도우 내 본적있는 문자라면
            start = used[char] + 1               # 인덱스 포인터 갱신
        else:                                    # 윈도우 내 본적없는 문자라면
            max_length = max(max_length, index - start + 1)
        
        # key : 문자, value : 현재 인덱스로 갖는 dictionary
        used[char] = index                       
    
    return max_length


# ---------------------------------------------------
# sol2. one pointer with explicit sliding window
# ---------------------------------------------------
def lengthOfLongestSubstring(self, s: str) -> int:
    max_length = left_p = 0
    window = set()
    for i in range(len(s)):
            # remove all chars from window until curr (s[r])
            while s[i] in window:
                window.remove(s[left_p])
                left_p += 1
            # add curr char (s[r]) and update maxLen if needed
            window.add(s[i])
            max_length=max(max_length,len(window))
        
    return max_length