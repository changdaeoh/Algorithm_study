'''
Given a linked list, swap every two adjacent nodes and return its head.

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = [1]
Output: [1]

Constraints
* The number of nodes in the list is in the range [0, 100].
* 0 <= Node.val <= 100
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# sol1. 연속한 노드간 값만 변경하기
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val # 값교환
            cur = cur.next.next # 2칸 이동

        return head

# sol2. iterative
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            
            prev.next = b
            
            head = head.next
            prev = prev.next.next
        return root.next

# sol3. recursive
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head


# 시간초과 풀이. 왜..?
def swapLL(head:ListNode) -> ListNode:
    head_copy = head
    
    cnt = 0; prev = None
    while head:
        cnt = cnt + 1
        if (cnt%2):                       # 홀수
            prev = head
            head.next = head.next.next
        else:                             # 짝수
            head.next = prev      
        head = head.next                    
    
    return head_copy