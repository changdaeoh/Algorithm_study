'''
가장 흔한 단어

Given a string paragraph and a string array of the banned words banned, 
return the most frequent word that is not banned. 
It is guaranteed there is at least one word that is not banned, 
and that the answer is unique.

금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력하기. (대소문자 구분 x, 구두점 무시)
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was his."
banned = ["hit"]
Output: "ball"

Input: paragraph = "a.", banned = []
Output: "a"

Constraints:
* 1 <= paragraph.length <= 1000
* paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
* 0 <= banned.length <= 100
* 1 <= banned[i].length <= 10
* banned[i] consists of only lowercase English letters.
'''
import re
import collections

def common_word(text : str, banned : list) -> str:
    text = text.lower()
    text = re.sub("[^a-z]"," ", text)
    words = text.split()
    words = [w for w in words if w not in banned]
    freqs = collections.Counter(words)
    
    return freqs.most_common(1)[0][0]


# ----
def common_word(paragraph : str, banned : list) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                if word not in banned]
                
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]
