class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        i = 0
        ans = 0
        costs.sort()
        while i < len(costs) and coins >= costs[i]:
            
            coins -=costs[i]
            i+=1
            ans+=1
        return ans
            
        
        