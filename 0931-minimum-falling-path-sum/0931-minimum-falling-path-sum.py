class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                a = matrix[i-1][j-1] if j >= 1 else 10e6
                b = matrix[i-1][j+1] if j+1 < len(matrix[0]) else 10e6
                matrix[i][j] += min(a,b,matrix[i-1][j])
                
        return min(matrix[-1])
        