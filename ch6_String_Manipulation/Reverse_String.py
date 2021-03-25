'''
문자열 뒤집는 함수만들기. 
제약조건 : 바꾼 객체를 리턴하지말고 리스트 내부를 직접바꾸게끔. (리스트는 가변객체)
input_sample1 = ['h','e','l','l','o']
input_sample2 = ['H','a','n','n','a','h']
'''

# sol 1. 리스트 메서드 reverse 이용
def str_reversing(text : list) -> None:
    text.reverse()

# sol 2. 슬라이싱 이용
def str_reversing(text : list) -> None:
    text[:] = text[::-1]  
    
# sol 3. 두 개의 포인터를 이용한 스왑 
def str_reversing(text : list) -> None:
    front, back = 0, len(text)-1
    while front < back:
        text[front], text[back] = text[back], text[front]
        front += 1; back -= 1


'''
sol 2. 와 같이 풀이할 때
text = text[::-1]는 안되는데, 
이는 함수내에서 새로운 지역변수 text를 정의하는 것이기에 
원래의 input된 전역변수 text의 값을 수정하는 것이 아니다.

text[:]는 input된 전역변수 text의 원소값들을 의미하는 것.
'''