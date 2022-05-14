class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def subsequence(inx,l):
            if l == len(t):
                return 1
            if inx == len(s):
                return 0
            if s[inx] == t[l]:
                return subsequence(inx+1,l+1) + subsequence(inx+1,l)
            else:
                return subsequence(inx+1,l)
        return subsequence(0,0)
                
        
            
        