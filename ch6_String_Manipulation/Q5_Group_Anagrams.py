'''
그룹 애너그램

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

Constraints:
* 1 <= strs.length <= 104
* 0 <= strs[i].length <= 100
* strs[i] consists of lower-case English letters.
'''

strs = ["eat","tea","tan","ate","nat","bat"]
strs2 = ["a"]
strs3 = [""]

# efficient solution
import collections

def groupAnagrams(strs : list) -> list:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())



print(groupAnagrams(strs))
print(groupAnagrams(strs2))
print(groupAnagrams(strs3))


# inefficient solution
def group_anagrams(strs : list) -> list:
    words = [ [w[i] for i in range(len(w))] for w in strs ]
    a = [ sorted(w) for w in words ]

    b = []
    for idx, values in enumerate(a):             
        temp = []
        temp.append(idx)
        b.append(temp + values)
    c = sorted(b, key = lambda x: x[1:])
    d = [ [w[0], ''.join(w[1:])] for w in c ]
    
    e = collections.defaultdict(list)
    for value, key in d:
        e[key] += [value]
    
    return [ [strs[j] for j in groups] for groups in e.values() ]


print(group_anagrams(strs))
print(group_anagrams(strs2))
print(group_anagrams(strs3))
