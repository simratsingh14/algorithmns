class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(minVal):
            if minVal == 0:
                return False
            ans = 0
            for i in quantities:
                ans += ceil(i/minVal)
                if ans > n:
                    return False
            return True
        #print(canDistribute(3))
        left,right = 1,max(quantities) 
        
        while left <= right:
            mid = (left+right)//2
            isPossible = canDistribute(mid)
            if not isPossible:
                left = mid+1
            else:
                right = mid-1
        return left
                    
                    
            
        