class MedianFinder:

    def __init__(self):
        self.left = []    # max heap
        self.right = []   # min heap
        

    def addNum(self, num: int) -> None:
        if len(self.right) == 0:
            heapq.heappush(self.right,num)
            return
            
        if num < self.right[0]:
            heapq.heappush(self.left,-1*num)
        else:
            heapq.heappush(self.right,num)
        #print(self.left,self.right)
        if len(self.left) - len(self.right) == 2:         # balancing
            val = heapq.heappop(self.left)
            heapq.heappush(self.right,-1*val)
        elif len(self.right) - len(self.left) == 2:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left,-1*val)
        #print(self.left,self.right,num)
            
    def findMedian(self) -> float:
        #print(self.left,self.right)
        if len(self.left) > len(self.right):
            return -1*self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (self.right[0] - self.left[0])/2 
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()