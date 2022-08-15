class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        lfl = [-1]*len(heights)
        stack = deque()
        stack.append(0)
        
        for i in range(1,len(heights)):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            lfl[i] = stack[-1] if len(stack)!=0 else -1
            stack.append(i)
        #print(lfl)
        lfr = [len(heights)]*len(heights)
        stack = deque()
        stack.append(len(heights)-1)
        for i in range(len(heights)-2,-1,-1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            lfr[i] = stack[-1] if len(stack)!=0 else len(heights)
            stack.append(i)
        ans = 0
        for i in range(len(heights)):
            ans = max(ans,heights[i]*(lfr[i]-lfl[i]-1))
        #print(lfl,lfr)
        return ans
            