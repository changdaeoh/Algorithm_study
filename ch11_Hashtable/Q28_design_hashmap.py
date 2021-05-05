'''
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:
* MyHashMap() : initializes the object with an empty map.
* void put(int key, int value) : inserts a (key, value) pair into the HashMap. 
If the key already exists in the map, update the corresponding value.
* int get(int key) : returns the value to which the specified key is mapped, 
or -1 if this map contains no mapping for the key.
* void remove(key) : removes the key and its corresponding value if the map contains the mapping for the key.

''' 

# -----------------------------------------------
# solution 1 연결리스트를 이용한 구현
# -----------------------------------------------

class ListNode:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = None

import collections
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
    
    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size # hashing
        # 테이블에 없는 새로운 해쉬라면 해당 해쉬에 대응되는 노드 추가
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return 
        # 이미 값이할당된 해쉬라면 연결리스트 잇기
        p = self.table[index] # 존재하던 노드 p에 저장
        while p:
            if p.key == key: # 이미 값이할당된 해쉬의 노드들 중 "key가 이미있는 key라면"
                p.value = value # value 업데이트 진행
                return # 종료
            if p.next is None:
                break
            p = p.next # 노드 포인터 전진
        # 이미 할당된 해쉬인데, 해당공간에 호출된 key는 없을 경우 새로 연결
        p.next = ListNode(key, value)
            
    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None: # 존재하지 않는 키->해쉬
            return -1
        
        # 존재하는 해쉬일 경우 연결되어있는 모든 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
    
    # 삭제
    def remove(self, key:int) -> None:
        index = key % self.size
        # 존재하지 않는 해쉬일때의 처리
        if self.table[index].value is None:
            return
        
        # 존재하는 해쉬일때의 처리
        p = self.table[index]
        # 일치하는 key 탐색
        if p.key == key: # 바로 일치할 경우 - 유일노드인지 아닌지에 따라 다른처리
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next # prev, current 노드 포인터 동시에 전진


# -----------------------------------------------
# solution 2 이중리스트 구현 
# - 풀리긴하는데 해쉬테이블 구현이라고 할 수없음 (충돌처리 못해서)
# - 충돌도 처리하게끔 이중리스트로 구현할 수 있긴 할듯함
# -----------------------------------------------

class MyHashMap:
    def __init__(self):
        self.hash_table = []
        self.keys = []

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:                   # 추가
            self.keys.append(key)
            self.hash_table.append([key, value])
        else:                                      # 갱신 
            idx = self.keys.index(key)
            self.hash_table[idx][1] = value

    def get(self, key: int) -> int:
        if key in self.keys:                   
            return self.hash_table[self.keys.index(key)][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.keys:                   
            self.hash_table.pop(self.keys.index(key))
            self.keys.remove(key)