class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit1 = 0
        profit2 = 0
        buy1 = -prices[0]
        buy2 = -prices[0]
        for i in range(1,len(prices)):
            profit_temp = profit1
            profit2 = max(profit2,buy2+prices[i])
            profit1 = max(profit1,buy1+prices[i])
            buy2 = max(buy2,profit_temp-prices[i])
            buy1 = max(buy1,-prices[i])
        return profit2
            