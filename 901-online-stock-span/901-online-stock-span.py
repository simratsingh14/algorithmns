class StockSpanner:

    def __init__(self):
        self.stack = deque() #price,index
        self.count = 1
        

    def next(self, price: int) -> int:
        #print(self.stack)
        while len(self.stack) > 0 and self.stack[-1][0] <= price:
            self.stack.pop()
        
        top = self.count - self.stack[-1][1] if len(self.stack)!=0 else self.count
        self.stack.append((price,self.count))
        self.count+=1
        return top
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)