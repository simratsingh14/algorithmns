class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            #print(stack)
            if len(stack) > 0 and stack[-1][0] == i:
                elem,count = stack.pop()
                if count+1!=k:
                    stack.append((elem,count+1))
            else:
                stack.append((i,1))
        #print(stack)
        ans = ''
        for i in stack:
            ans += i[0]*i[1]
        return ans
                
                
        