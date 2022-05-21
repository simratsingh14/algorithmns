class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = -1e4 -1
        profit = 0
        for i in range(len(prices)):
            profit = max(profit,prices[i]+minprice)
            minprice = max(minprice,-1*prices[i])
        return profit