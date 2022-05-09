class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # @lru_cache(None)
        # def recursive(s,t):
        #     if s == 0 or  t == 0:
        #         return 0
        #     if text1[s-1] == text2[t-1]:
        #         return 1 + recursive(s-1,t-1)
        #     else:
        #         return max(recursive(s-1,t),recursive(s,t-1))
        # return recursive(len(text1),len(text2))
            
        n,m = len(text1),len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
        