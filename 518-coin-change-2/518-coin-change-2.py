class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0]*amount
        for i in coins:
            #print(dp)
            for j in range(1,len(dp)):
                if j - i >= 0:
                    dp[j]+=dp[j-i]
        return dp[-1]
    
        