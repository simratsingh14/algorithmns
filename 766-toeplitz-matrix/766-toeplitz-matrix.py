class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j-i in d and matrix[i][j]!=d[j-i]:
                    return False
                else:
                    d[j-i] = matrix[i][j]
        #print(d)
        return True
                    
        