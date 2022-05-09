class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def recursive(s,t):
            if s == 0 or  t == 0:
                return 0
            if text1[s-1] == text2[t-1]:
                return 1 + recursive(s-1,t-1)
            else:
                return max(recursive(s-1,t),recursive(s,t-1))
        return recursive(len(text1),len(text2))
            
        