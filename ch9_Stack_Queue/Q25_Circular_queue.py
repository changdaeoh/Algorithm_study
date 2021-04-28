'''
Design your implementation of the circular queue. 
The circular queue is a linear data structure in which the operations 
are performed based on FIFO (First In First Out) principle and the last position is 
connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
In a normal queue, once the queue becomes full, 
we cannot insert the next element even if there is a space in front of the queue. 
But using the circular queue, we can use the space to store new values.

- Implementation the MyCircularQueue class -

MyCircularQueue(k) : Initializes the object with the size of the queue to be k.
int Front() : Gets the front item from the queue. If the queue is empty, return -1.
int Rear() : Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) : Inserts an element into the circular queue. 
    Return true if the operation is successful.
boolean deQueue() : Deletes an element from the circular queue. 
    Return true if the operation is successful.
boolean isEmpty() : Checks whether the circular queue is empty or not.
boolean isFull() : Checks whether the circular queue is full or not.
'''

class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.p_front = 0
        self.p_rear = 0
    
    # rear 포인터를 이동시키면서 값 삽입
    def enQueue(self, value: int) -> bool:
        if self.queue[self.p_rear] is None:
            self.queue[self.p_rear] = value
            self.p_rear = (self.p_rear + 1) % self.size
            return True
        # 삽입하려는데 값 있으면 오류
        else:
            return False
    
    # front 포인터를 이동시키면서 값 삭제
    def deQueue(self) -> bool:
        # 삭제하려는데 None이면 오류
        if self.queue[self.p_front] is None:
            return False
        else:
            self.queue[self.p_front] = None
            self.p_front = (self.p_front + 1) % self.size
            return True

    def Front(self) -> int:
        return -1 if self.queue[self.p_front] is None else self.queue[self.p_front]

    def Rear(self) -> int:
        return -1 if self.queue[self.p_rear - 1] is None else self.queue[self.p_rear - 1]

    def isEmpty(self) -> bool:
        return self.p_front == self.p_rear and self.queue[self.p_front] is None

    def isFull(self) -> bool:
        return self.p_front == self.p_rear and self.queue[self.p_front] is not None