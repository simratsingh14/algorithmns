class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buying = -prices[0]
        profit = 0
        for i in range(1,len(prices)):
            #print(profit,buying)
            temp  = profit
            profit = max(profit,buying+prices[i]-fee)
            buying = max(buying,temp-prices[i])
        return profit
            
        