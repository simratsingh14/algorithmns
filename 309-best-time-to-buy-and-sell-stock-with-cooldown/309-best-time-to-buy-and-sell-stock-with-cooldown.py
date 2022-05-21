class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        s1 = -prices[0]     # profit after buying
        s2 = 0              # profit after selling
        s0 = [0, 0]         # cooldown profit using a queue
        for p in prices:
            s1 = max(s1, s0[1] - p)
            s2 = max(s2, s1 + p)
            s0 = [s2, s0[0]]
        return s2