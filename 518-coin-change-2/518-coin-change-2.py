class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[1] + [0]*amount for _ in range(len(coins)+1)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if j - coins[i-1] >= 0:
                    #print(i,j-coins[i-1],dp[i][j - coins[i-1]])
                    dp[i][j]+=dp[i][j - coins[i-1]]
                dp[i][j] += dp[i-1][j]
        #print(dp)
        return dp[-1][-1]

        