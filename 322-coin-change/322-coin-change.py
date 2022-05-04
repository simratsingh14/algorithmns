class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0] +[10001]*amount for _ in range(len(coins)+1)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if j >= coins[i-1]:
                    dp[i][j] = min(1+dp[i][j-coins[i-1]],dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1] if dp[-1][-1]!= 10001 else -1
        
        
        