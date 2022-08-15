class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minstack = deque()
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or val <= self.getMin():
            self.minstack.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.top() == self.getMin():
            self.minstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        #print(self.stack,self.minstack)
        return self.stack[-1]
        

    def getMin(self) -> int:
        #print(self.stack,self.minstack)
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()