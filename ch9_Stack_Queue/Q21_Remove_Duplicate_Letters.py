'''
Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Input: s = "bcabc"
Output: "abc"

Input: s = "cbacdcbc"
Output: "acdb"

Constraint
* 1 <= s.length <= 10^4
* s consists of lowercase English letters.
'''

# solution 1 - 재귀구조 이용
def remover(s:str)->str:
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # 전체집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + remover(suffix.replace(char, ''))
    return ''

'''
unique 문자들을 오름차순으로 저장하고 하나씩 원 문자열에서 검색
해당 unique 문자 인덱스부터 시작하여 문자열 끝까지를 대상으로 모든 다른 unique 문자 포함하면 check it
그 문자를 output에 추가. 나머지(뒤에나오는 동일문자) 전부제거
-반복-
(재귀 호출시 조건을 만족할때마다 하나의 문자는 전부 제거되므로 
input되는 문자열에 포함되어있는 unique 문자수도 하나씩 줄어듬)
'''


# solution 2
def remover(s:str) -> str:
    counter, seen, stack = collections.Counter(s), set(), []
    
    for char in s:
        counter[char] -= 1             # 순회될 때마다 count 1씩 감소
        if char in seen:               # 한번이라도 순회한 문자 만나면 일단 다음인덱스로 건너뜀
            continue
        # 조건 : stack에 문자가 있고, 새로 조회한 문자가 stack의 가장 위 문자보다 더 빠르며,
        #       그 stack 가장 위의 문자가 뒤에 또 나온다면. 제거 쌉가능이다 이말이야
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())   # 해당 문자를 stack에서도 꺼내고 seen에서도 제거해버림
        stack.append(char)             # 별 일 없으면 문자 stack에 추가
        seen.add(char)                 # 고유한 문자 seen 집합에 추가
    
    return ''.join(stack)    


''' 
필요한 객체들
- cnt 사전 -> 순회시마다 횟수 (-). 남은 출현횟수 확인용
- seen -> stack에 고유한 문자만 저장하고, 불필요한 조건확인 줄이기 위해 집합자료형 만들기
- stack 순차적으로 쌓아가며 range 1범위 내에서 넣다뺐다가능. 최종출력 문자목록으로 사용

stack 업데이트 발동 조건 3개
- stack이 비어있지 않음
- stack에 쌓여있는 가장 마지막 문자보다 현재 순회중인 문자가 더 빨라야함
- stack에 쌓여있는 가장 마지막 문자가 남은 문자열에 또 있어야함 (cnt로 알 수 있음)
'''