class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        prev = -1e9
        for i in range(len(prices)):
            temp = profit
            profit = max(profit,prev+prices[i])
            prev = max(prev,temp-prices[i]-fee)
        return profit
        