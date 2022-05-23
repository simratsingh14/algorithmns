class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        profit = [0]*(k+1)
        buy = [-float('inf')]*(k+1)
        for i in range(len(prices)):
            #print(profit,buy)
            profit_temp = profit[:]
            for j in range(1,k+1):
                profit[j] = max(profit[j],buy[j]+prices[i])
            for j in range(1,k+1):
                buy[j] = max(buy[j],profit_temp[j-1]-prices[i])
        return profit[-1]
        