class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dirs = [(1,-1),(1,0),(1,1)]
        for i in range(len(matrix)-2,-1,-1):
            for j in range(len(matrix[0])):
                ans = 1000001
                for d in dirs:
                    x = i + d[0]
                    y = j + d[1]
                    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                        ans = min(ans,matrix[x][y])
                matrix[i][j]+=ans
        #print(matrix)
        return min(matrix[0])
        
        
        