class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        number = 1
        rowMin,rowMax,colMin,colMax = 0,n-1,0,n-1
        while number <= n**2:
            #print(number)
            for j in range(colMin,colMax+1):
                matrix[rowMin][j] = number
                number+=1 
            rowMin+=1
            for i in range(rowMin,rowMax+1):
                matrix[i][colMax] = number
                number+=1
            colMax-=1
            for j in range(colMax,colMin-1,-1):
                matrix[rowMax][j] = number
                number+=1
            rowMax-=1
            for i in range(rowMax,rowMin-1,-1):
                matrix[i][colMin] = number
                number+=1
            colMin+=1
        return matrix
                
            