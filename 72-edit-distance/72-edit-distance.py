class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def recursive(s,t):
            #print(s,t)
            if s == 0 or t == 0:
                return max(s,t)
            if word1[s-1] == word2[t-1]:
                return recursive(s-1,t-1)
            else:
                return min(1+recursive(s-1,t-1),1+recursive(s-1,t),1+recursive(s,t-1))
        #return recursive(len(word1),len(word2))
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 or j == 0:
                    dp[i][j] = max(i,j)
                elif word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])
        return dp[-1][-1]
            
        