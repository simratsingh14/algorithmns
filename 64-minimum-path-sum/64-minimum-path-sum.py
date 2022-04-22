class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        pathSum = 0
        for i in range(len(grid)):
            pathSum+=grid[i][0]
            grid[i][0] = pathSum
        pathSum = 0
        for j in range(len(grid[0])):
            pathSum+=grid[0][j]
            grid[0][j] = pathSum
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j] += min(grid[i][j-1],grid[i-1][j])
        return grid[-1][-1]
            
                
        