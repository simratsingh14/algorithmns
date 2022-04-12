class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                minCost = 2000000
                if i == j == 0:
                    continue
                if i > 0:
                    minCost = min(minCost,grid[i-1][j])
                if j > 0:
                    minCost = min(minCost,grid[i][j-1])
                grid[i][j] += minCost
        return grid[-1][-1]
                    
                
        