class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            #print(stack)
            if i in ['+','-','*','/']:
                num2 = stack.pop()
                num1 = stack.pop()
                if i == '+':
                    stack.append(num1+num2)
                elif i == '-':
                    stack.append(num1-num2)
                elif i == '*':
                    stack.append(num1*num2)
                elif i == '/':
                    stack.append(int(num1/num2))
            else:
                stack.append(int(i))
        return stack[0]
                
        