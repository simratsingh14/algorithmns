class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying = -prices[0]
        profit = 0
        prev = 0
        for i in range(1,len(prices)):
            #print(prev,profit,buying)
            temp = profit
            profit = max(profit,buying+prices[i])
            buying = max(buying,prev-prices[i])
            prev = temp
        #print(profit,prev,buying)
        return max(prev,profit)
        