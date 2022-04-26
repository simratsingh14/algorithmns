class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def helper(inx,amount):
            if amount == 0:
                return 0
            
            if inx == len(coins):
                return 100000
            
            ans = 0
            if amount >= coins[inx]:
                ans = min(1+helper(inx,amount-coins[inx]),helper(inx+1,amount))
            else:
                ans = helper(inx+1,amount)
            return ans
        
        if helper(0,amount) == 100000:
            return -1
        else:
            return helper(0,amount)
            
            
        