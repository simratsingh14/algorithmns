class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s) + [1]
        for i in range(len(dp)-2,-1,-1):
            if s[i] == '0':
                dp[i] == 0
                continue
            ans = dp[i+1]
            if i + 2 <= len(s) and 10 <= int(s[i:i+2]) <= 26:
                #print(s[i:i+2])
                ans+=dp[i+2]
            dp[i]+=ans
        #print(dp)
        return dp[0]
        