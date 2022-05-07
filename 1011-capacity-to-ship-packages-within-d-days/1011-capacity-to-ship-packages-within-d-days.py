class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysTaken(cap):
            ans = 0 
            currCap = 0
            for i in weights:
                if currCap + i > cap:
                    ans += 1
                    currCap = i
                else:
                    currCap += i
            if currCap!=0:
                ans+=1
            return ans
        left,right = max(weights),sum(weights)
        while left <= right:
            mid = (left+right)//2
            daystaken = daysTaken(mid)
            if daystaken > days:
                left = mid+1
            else:
                right = mid -1
        return left
        
        
                    