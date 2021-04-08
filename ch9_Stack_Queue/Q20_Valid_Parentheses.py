'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Input: s = "{[]}"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "([)]"
Output: false

Constraint
* 1 <= s.length <= 10^4
* s consists of parentheses only '()[]{}'.
'''
# 교재풀이
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0


# my solution
def isvalid(s:str)->bool:
    # keys : open, values : close
    dic = {'(':')', "[":"]", "{":"}"}
    
    buffer = []
    for char in s:
        if char in dic.keys():
            buffer.append(char)
        elif (len(buffer) == 0) or (dic[buffer.pop()] != char) : 
            return False
            
    return len(buffer) == 0