class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        buying = -1e4-1
        profit = 0
        for i in range(len(prices)):
            profit = max(profit,prices[i]+buying)
            if profit > 0:
                total+=profit
                buying = -1e4-1
                profit = 0
            buying = max(buying,-1*prices[i])
        return total+profit
            
                
            
            