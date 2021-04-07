''' 두 정렬된 연결리스트 병합
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Constraints:
* The number of nodes in both lists is in the range [0, 50].
* -100 <= Node.val <= 100
* Both l1 and l2 are sorted in non-decreasing order.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# sol1. recursive
def merge_LL(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.merge_LL(l1.next, l2)

    return l1


# sol2. iterative
class Solution:
    # input되는 l1, l2는 linked list의 "Head" Node임을 명시하자
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # -------------------------------------------------------------- STEP 1 : 노드 인스턴스 생성
        # 2개의 노드 초기화. - tail을 head가 참조하도록
        # head는 return용으로다가 포인터를 이동시키기않고 놔둘것임.
        # tail은 지속적으로 전진시키며 trace를 만들것임.
        merged_head = merged_tail = ListNode(None)

        # -------------------------------------------------------------- STEP 2 : 루프 생성
        # While l1 and l2 both have nodes to be traversed
        # 둘 중 하나가 완전히 순회되면 루프 종료
        while l1 and l2:
            # ---------------------------------------------------------- STEP 2.1 : 대소비교
            # 각 리스트 노드의 value를 꺼내서 대소 비교
            # If the node in l1 has the smaller value
            if l1.val <= l2.val:
                # ------------------------------------------------------ STEP 2.2 : tail 노드 확장 (주소 붙이기)
                # tail 노드 인스턴스의 포인터변수(next)에 l1의 현재노드를 할당
                # Add the node from l1 to the merged linked list
                merged_tail.next = l1
                # ------------------------------------------------------ STEP 2.3 : 대상 리스트 node 이동시키기
                # Move to the next node in l1
                l1 = l1.next
            # If the node in l2 has the smaller value
            else:
                # Add the node from l2 to the merged linked list
                merged_tail.next = l2
                # Move to the next node in l2
                l2 = l2.next
            # ---------------------------------------------------------- STEP 3 : tail 노드 포인팅 갱신 (next)
            # Update tail the tail reference to the new last node in the list
            merged_tail = merged_tail.next

        # -------------------------------------------------------------- STEP 4 : 남은값들 통채로 append
        # At this point one of the lists has been completely traversed
        # so attach the other one to the end of the merged linked list
        merged_tail.next = l1 or l2

        # -------------------------------------------------------------- STEP 5 : tail을 참조하는 head 반환
        # Return the head to the merged linked list (처음값은 None이라서 하나 next한 객체를 반환)
        return merged_head.next



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged_head = merged_tail = ListNode(None)

        # While l1 and l2 both have nodes to be traversed

        while l1 and l2:
            # If the node in l1 has the smaller value
            if l1.val <= l2.val:
                # Add the node from l1 to the merged linked list
                merged_tail.next = l1
                # Move to the next node in l1
                l1 = l1.next
            # If the node in l2 has the smaller value
            else:
                # Add the node from l2 to the merged linked list
                merged_tail.next = l2
                # Move to the next node in l2
                l2 = l2.next

            # Update tail the tail reference to the new last node in the list
            merged_tail = merged_tail.next
        
        # At this point one of the lists has been completely traversed 
        # so attach the other one to the end of the merged linked list
        merged_tail.next = l1 or l2
        

        # Return the head to the merged linked list
        return merged_head.next