class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [-1]
        left,right = 0,0
        while left < len(pushed) or right < len(popped):
            if right < len(popped) and stack[-1] == popped[right]:
                stack.pop()
                right+=1
            elif left < len(pushed):
                stack.append(pushed[left])
                left+=1
            elif left == len(pushed):
                return False
        return True
                
        
        
        
        