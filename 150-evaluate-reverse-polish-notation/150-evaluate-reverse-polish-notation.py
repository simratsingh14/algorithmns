class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            #print(stack)
            if i in ['+','-','*','/']:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == '+':
                    stack.append(str(num1+num2))
                elif i == '-':
                    stack.append(str(num1-num2))
                elif i == '*':
                    stack.append(str(num1*num2))
                elif i == '/':
                    stack.append(str(int(num1/num2)))
            else:
                stack.append(i)
        return int(stack[0])
                
        