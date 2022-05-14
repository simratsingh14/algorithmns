class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def helper(l1,l2):
            if l1 == 0 and l2 == 0:
                return True
            elif l2 == 0:
                return False
            elif l1 == 0 and p[l2-1] != '*':
                return False
            
            if p[l2-1] == '*':
                if l1 == 0:
                    return helper(l1,l2-1)
                return helper(l1-1,l2) or helper(l1-1,l2-1) or helper(l1,l2-1)
            elif p[l2-1] == '?':
                return helper(l1-1,l2-1)
            else:
                return s[l1-1] == p[l2-1] and helper(l1-1,l2-1)
        #return helper(len(s),len(p))
        # dp = [[False]*(len(s)+1) for _ in range(len(p)+1)]
        # dp[0][0] = True
        # for i in range(1,len(dp)):
        #      if p[i-1] == '*':
        #         dp[i][0] = dp[i-1][0]
        # for i in range(1,len(dp)):
        #     for j in range(1,len(dp[0])):
        #         if p[i-1] == '*':
        #             dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
        #         elif p[i-1] == '?':
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = p[i-1] == s[j-1] and dp[i-1][j-1]
        # return dp[-1][-1]
        prev = [True] +[False]*(len(s))
        curr = prev[:]
        for i in range(1,len(p)+1):
            #print(prev)
            for j in range(len(prev)):
                if j == 0:
                    if p[i-1] == '*':
                        curr[j] = prev[j]
                    else:
                        curr[j] = False
                    continue
                if p[i-1] == '*':
                    curr[j] = prev[j-1] or prev[j] or curr[j-1]
                elif p[i-1] == '?':
                    curr[j] = prev[j-1]
                else:
                    curr[j] = p[i-1] == s[j-1] and prev[j-1]
            prev = curr[:]
        return prev[-1]
        
        
                
        
            
            
        