''' 팰린드롬 연결리스트 판별
Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true
Input: head = [1,2]
Output: false

Constraints:
* The number of nodes in the list is in the range [1, 105].
* 0 <= Node.val <= 9
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# transform to python list
def palindrome_LL(head: ListNode) -> bool:
    q: list = []

    if not head:
        return True

    node = head
    # 연결리스트를 파이썬 리스트로 변환
    while node is not None:
        q.append(node.val)
        node = node.next
    # 팰린드롬 판별
    return q == q[::-1]


# use Runner
def isPalindrome(head:ListNode) -> bool:
    rev = None
    slow = fast = head
    # 2개의 러너, 다중할당 테크닉으로 역순 sub list 만들기
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    # 요소 개수가 홀수일 때
    if fast:
        slow = slow.next
    # 팰린드롬 판별
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev