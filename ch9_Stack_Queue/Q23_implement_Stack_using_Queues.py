'''
Implement a last in first out (LIFO) stack using only two queues. 
The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means only push to back, 
peek/pop from front, size, and is empty operations are valid.

Depending on your language, the queue may not be supported natively. 
You may simulate a queue using a list or deque (double-ended queue), 
as long as you use only a queue's standard operations.
'''

# sol 1 - 2개의 큐 사용
class MyStack:
    def __init__(self):
        self.queue1=[]
        self.queue2=[]

    def push(self, x: int) -> None:
        self.queue1.append(x)
        
    def pop(self) -> int:
        while len(self.queue1) > 1:                   
            self.queue2.append(self.queue1.pop(0)) # 첫 원소 뽑아(FIFO) 다른 큐에 넣음 (마지막원소만 남기까지)
        temp = self.queue1.pop()                   # 마지막 추가원소 임시저장
        # queue 1은 마지막 추가원소가 제거된 상태가 되고
        # queue 2는 비어있는 queue로 초기화됨.
        self.queue1, self.queue2 = self.queue2, self.queue1 
        return temp

    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        return len(self.queue1) == 0


# sol 2 - 덱 자료형 이용, queue 연산만 사용
import collections

class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # 원소 추가시마다 추가한 원소가 가장 앞으로 가도록 FIFO 반복
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
    def pop(self) -> int:
        return q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# sol 3 취지에 안맞음 요렇게 풀기 ㄴ ㄴ
class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0