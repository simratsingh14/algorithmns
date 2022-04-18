class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['[','(','{']:
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif i == ']':
                if not (stack[-1] == '['):
                    return False
                else:
                    stack.pop()
            elif i == '}':
                if not (stack[-1] == '{'):
                    return False
                else:
                    stack.pop()
            elif i == ')':
                if not (stack[-1] == '('):
                    return False
                else:
                    stack.pop()
        #print(stack)
        return len(stack) == 0
             
        