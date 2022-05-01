class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]
        count = 0
        for i in range(len(dp)):
            dp[i][i] = True
            count+=1
            if i + 1 < len(dp):
                dp[i][i+1] = s[i] == s[i+1]
                if dp[i][i+1]:
                    count+=1
        for l in range(2,len(s)):
            i = 0
            while i+l < len(s):
                dp[i][i+l] = s[i] == s[i+l]  and dp[i+1][i+l-1]
                if dp[i][i+l]:
                    count+=1
                i+=1
        #print(dp)
        return count
            
        