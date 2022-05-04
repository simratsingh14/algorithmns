class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]+[10001]*amount
        for i in coins:
            for j in range(1,amount+1):
                if j >= i:
                    dp[j] = min(dp[j],1+dp[j-i])
        return dp[-1] if dp[-1] != 10001 else -1
        
        