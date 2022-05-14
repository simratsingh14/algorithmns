class Solution:
    def numDistinct(self, s: str, t: str) -> int:
#         @lru_cache(None)
#         def subsequence(inx,l):
#             if l == 0:
#                 return 1
#             if inx == 0:
#                 return 0
#             if s[inx-1] == t[l-1]:
#                 return subsequence(inx-1,l-1) + subsequence(inx-1,l)
#             else:
#                 return subsequence(inx-1,l)
#         return subsequence(len(s),len(t))

        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
        for l in range(len(dp)):
            for inx in range(len(dp[0])):
                if l == 0:
                    dp[l][inx] = 1
                    continue
                if inx == 0:
                    dp[l][inx] = 0
                    continue
                    
                
                if s[inx-1] == t[l-1]:
                    dp[l][inx] = dp[l-1][inx-1] + dp[l][inx-1]
                else:
                    dp[l][inx] = dp[l][inx-1]
        #print(dp)
        return dp[-1][-1]
                
        
            
        