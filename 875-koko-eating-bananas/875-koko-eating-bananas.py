class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeTaken(amount):
            ans = 0 
            for i in piles:
                ans += math.ceil(i/amount)
            return ans
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left+right)//2
            time = timeTaken(mid)
            if time > h:
                left = mid +1
            else:
                right = mid - 1
        return left
            
        