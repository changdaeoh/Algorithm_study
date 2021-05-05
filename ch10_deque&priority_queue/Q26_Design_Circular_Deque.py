# double linked list를 이용한 원형큐 구현

class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class MyCircularDeque:
    # head와 tail에는 값이 안담겨있음(None node임). 단지 이중리스트 양끝을 명시하는 단방향 연결노드
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
    
    # node : 기존에 존재하던 노드
    # new : 새로 추가하고자 하는 노드
    def _add(self, node:ListNode, new:ListNode):
        n = node.right                 # n : 기존에 존재하던 노드 우측에 있는 노드 instance
        node.right = new               # node의 우측 포인터에 신규추가노드 new를 할당
        new.left, new.right = node, n  # new의 left 포인터에는 node, right포인터에는 n을 할당
        n.left = new                   # n의 left 포인터에 new node 할당 
    
    def _del(self, node:ListNode):
        n = node.right.right           # node -> something -> n(노드의 옆옆 노드 instance)
        node.right = n                 # node -> n 
        n.left = node                  # node <- n

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True
        
    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1
        
    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1
        
    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()