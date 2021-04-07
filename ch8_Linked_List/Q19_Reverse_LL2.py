'''
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints
* The number of nodes in the list is n.
* 1 <= n <= 500
* -500 <= Node.val <= 500
* 1 <= left <= right <= n
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 예외처리
        if not head or left == right:
            return head
        # --------------------------------------------------------------------------
        root = start = ListNode(None)         # output으로 root.next를 반환할 것임
        root.next = head                      # root node가 전체 input된 LL을 잠조하도록 하였음
                                              # 그와 동시에 start는 root와 동일한 객체를 참조하므로 똑같이 처리됨
        # --------------------------------------------------------------------------
        # 포인팅 변경의 start와 end노드 설정. (이 노드들은 값이 변경되지 않으며 pointer를 변경하는 기준이된다.)
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # start노드와 end노드를 기준으로 pointing 반복변경
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        # start가 pointing하는 node가 한 단계씩 상승
        # end의 절대적 위치가 한 수준씩 상승

        return root.next
