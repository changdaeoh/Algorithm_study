''' add two numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constrain
* The number of nodes in each linked list is in the range [1, 100].
* 0 <= Node.val <= 9
* It is guaranteed that the list represents a number that does not have leading zeros.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# my solution
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_str, l2_str = '', ''
        res_head = res_tail = ListNode(None)

        # 연결리스트를 파이썬 문자열로 변환
        while l1 is not None:
            l1_str += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            l2_str += str(l2.val)
            l2 = l2.next

        # 역순으로 뒤집에서 덧셈 계산.
        res_str = str( int(l1_str[::-1]) + int(l2_str[::-1]) )
        # 결과 연결리스트도 역순으로 생성해야함
        for char in res_str[::-1]:
            res_tail.next = ListNode(int(char))
            res_tail = res_tail.next

        return res_head.next

# full adder
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next