class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(1,len(dp[0])):
            dp[0][i] = 100001
            
        for inx in range(1,len(dp)):
            for amt in range(1,len(dp[0])):
                if amt >= coins[inx-1]:
                    dp[inx][amt] = min(1+dp[inx][amt - coins[inx-1]],dp[inx-1][amt])
                else:
                    dp[inx][amt] = dp[inx-1][amt]
        if dp[-1][-1] == 100001:
            return -1
        return dp[-1][-1]
        
            
            
        