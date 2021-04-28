'''Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

- Implement the MyQueue class -

void push(int x) : Pushes element x to the back of the queue.
int pop() : Removes the element from the front of the queue and returns it.
int peek() : Returns the element at the front of the queue.
boolean empty() : Returns true if the queue is empty, false otherwise.

* You must use only standard operations of a stack, which means only push to top,
 peek/pop from top, size, and is empty operations are valid.

* Depending on your language, the stack may not be supported natively. 
You may simulate a stack using a list or deque (double-ended queue) as long as 
you use only a stack's standard operations.

'''
# solution
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []    
        
    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        # output stack이 비었으면 input stack의 위에서부터 뽑아 채움
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []
    
# 전체 요소들을 굳이 하나의 개체에 보관할 필요없음. 
# => input, output 리스트에 나누어 보관