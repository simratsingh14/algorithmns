class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = Counter(s)
        
        for k,i in enumerate(s):
            if h[i] == 1:
                return k
        return -1