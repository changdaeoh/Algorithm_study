'''연결리스트 뒤집기
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# my solution
def reverselist(head: ListNode) -> ListNode:
    rev: ListNode = None
    while head:
        rev, rev.next, head = head, rev, head.next
    return rev

# sol2. recursive
def reverselist2(head: ListNode) -> ListNode:
    def reverse(node:ListNode, prev:ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    return reverse(head)

# sol3. iterative
def reverselist3(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    return prev