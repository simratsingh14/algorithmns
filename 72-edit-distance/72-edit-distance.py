class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def recursive(s,t):
            #print(s,t)
            if s == 0  and t == 0:
                return 0
            elif s == 0 or t == 0:
                return max(s,t)
            if word1[s-1] == word2[t-1]:
                return recursive(s-1,t-1)
            else:
                return min(1+recursive(s-1,t-1),1+recursive(s-1,t),1+recursive(s,t-1))
        return recursive(len(word1),len(word2))
            
        