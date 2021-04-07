'''
Given the head of a singly linked list, 
group all the nodes with odd indices together followed by the nodes with even indices, 
and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints
* The number of nodes in the linked list is in the range [0, 104].
* -10^6 <= Node.val <= 10^6
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# input LL을 여러부분으로 복사하여 연결관계 원하는대로 바꾸기
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        odd = head # input된 head를 그대로 복사 -> 동일한 ListNode 객체를 2가지 이름으로 참조함
        even = even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next # 포인터 2보씩 전진
            odd, even = odd.next, even.next                     # 노드 이동

        odd.next = even_head
        # 참조하는 객체는 동일하나 odd에 대해서만 next를 호출했었음
        # 이어지는 모든 pointing 연결이 갱신된 최초 input head노드를 반환한다.
        return head 
