from fractions import Fraction

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1:
            return 0
        stockPrices.sort(key = lambda x:x[0])
        arr = []
        for i in range(1,len(stockPrices)):
            slope = Fraction((stockPrices[i][1]-stockPrices[i-1][1]),(stockPrices[i][0]-stockPrices[i-1][0]))
            arr.append(slope)
        #print(arr)
        count = 1
        for i in range(1,len(arr)):
            if arr[i-1]!=arr[i]:
                count+=1
        return count
        