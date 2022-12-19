class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack= [(temperatures[-1],len(temperatures)-1)]
        ans = [0]*len(temperatures)
        if len(temperatures) == 1:
            return [0]
        
        for i in range(len(temperatures)-2,-1,-1):
            curr = temperatures[i]
            while len(stack)!=0 and curr >= stack[-1][0]:
                stack.pop()
            
            if len(stack)!=0:
                ans[i] = stack[-1][1] - i
            else:
                ans[i] = 0
            stack.append((curr,i))
        return ans
                
            
        