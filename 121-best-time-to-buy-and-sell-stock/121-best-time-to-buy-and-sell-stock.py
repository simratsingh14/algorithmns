class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,profit = -1*prices[0],0
        for i in range(1,len(prices)):
            profit = max(profit,prices[i]+buy)
            buy = max(buy,-1*prices[i])
        return profit
            
        