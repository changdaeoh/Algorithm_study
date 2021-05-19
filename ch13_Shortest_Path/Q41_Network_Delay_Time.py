'''
You are given a network of n nodes, labeled from 1 to n. You are also given times,
a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node,
and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k.
Return the time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.
'''

import collections
import heapq
from typing import List


def networkDelayTime(times: List[List[int]], N: int, K: int) -> int:
    graph = collections.defaultdict(list)
    # 그래프 생성
    for u, v, w in times:
        graph[u].append((v, w))

    # 큐 변수: [(소요 시간, 정점)] - 각 node별 도달하기까지 소요시간 저장
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
    while Q:
        # 우선순위 큐에서 가장 우선순위가 높은(최소소요시간)을 갖는 (시간, 노드) 쌍을 추출
        # 파이썬의 heapq는 최소힙이기 떄문에 항상 소요시간이 최소인 노드가 상단에 올라와있음.
        time, node = heapq.heappop(Q)
        # 추출한 노드가 다이엑스트라값 사전에 존재하지 않는다면 아래의 과정을 거쳐 추가시킴
        if node not in dist:
            dist[node] = time
            # 그 노드의 하위노드들에 접근.
            for v, w in graph[node]:
                # 현재 노드에서 트래킹중인 시간에 다음노드로 전이함에 따라 추가로 소요되는 시간을 더함.
                alt = time + w
                # 큐에 소요시간을 중요도로 설정하여 노드를 삽입 ((시간, 노드) 쌍)
                # 삽입되는 과정에서 힙의 모든 노드의 우선순위를 고려하여 적절히 재배치가 이루어짐
                heapq.heappush(Q, (alt, v))

    # 모든 노드 도달가능여부를 if로 체크하고 필요한 소요시간 반환
    if len(dist) == N:
        return max(dist.values())
    return -1

times = [[3,1,5],[3,2,2],[2,1,2],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,1,1]]
n = 8
k = 3
print(networkDelayTime(times, n, k))
