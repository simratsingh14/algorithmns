class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sumMatrix = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                self.sumMatrix[i][j] = self.sumMatrix[i-1][j] + self.sumMatrix[i][j-1] + matrix[i-1][j-1] - self.sumMatrix[i-1][j-1]
        #print(self.sumMatrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        col1+=1
        row2+=1
        col2+=1
        a = self.sumMatrix[row1-1][col1-1]
        b = self.sumMatrix[row1-1][col2]
        c = self.sumMatrix[row2][col1-1]
        d = self.sumMatrix[row2][col2]
        return a + d - (c+b)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)