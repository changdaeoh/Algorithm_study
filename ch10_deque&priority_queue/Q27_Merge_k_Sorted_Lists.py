'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''
# -----------------------------------------------
# solution 1 (more efficient)
# -----------------------------------------------
# 최소힙 자료형 
import heapq 
from typing import List

# 우선순위 큐를 이용한(heap을 통해) 리스트 병합
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode :
        root = result = ListNode(None)
        heap = []
        
        # 각 연결 리스트 루트를 최소힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                
        while heap:
            # 최소힙으로부터 원소 추출 (최소 val를 갖는 노드의 튜플이 추출됨)
            node = heapq.heappop(heap)   # (val, idx, node)의 튜플이 node 인스턴스에 담김
            idx = node[1]
            result.next = node[2]

            # 추출한 노드(최솟값을 갖는 노드) 한칸 전진 시키고 다시 힙에 추가
            result = result.next         
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        
        return root.next


# -----------------------------------------------
# solution 2 (40배 느린풀이)
# -----------------------------------------------
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode :
        root = merged = ListNode(None)

        lists = [node for node in lists if node] # delete None
        while lists:
            # 매 단계마다 각 ListNode의 value 순회
            idx = 0
            min_v = lists[idx].val
            for i in range(len(lists)):
                if lists[i].val < min_v:
                    min_v = lists[i].val
                    idx = i
            # 결과 연결리스트 노드에 값추가
            merged.next = ListNode(min_v)
            merged = merged.next
            # 최소값 뽑아낸 리스트 노드 한칸 전진
            lists[idx] = lists[idx].next
            # None이 된 node 제거
            if lists[idx] is None: lists.remove(None)

        return root.next