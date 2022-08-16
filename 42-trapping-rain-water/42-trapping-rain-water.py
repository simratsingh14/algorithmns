class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = []
        maxright = [0]*len(height)
        
        maxl = 0
        for h in height:
            maxl = max(maxl,h)
            maxleft.append(maxl)
        maxr = 0
        for i in range(len(height)-1,-1,-1):
            maxr = max(maxr,height[i])
            maxright[i] = maxr
        #print(maxleft,maxright)
        ans = 0
        for i in range(len(height)):
            ans += min(maxleft[i],maxright[i]) - height[i]
        return ans
            
            
            
            
        