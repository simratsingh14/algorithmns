class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row,col,grid):
            if row < 0 or row >= len(grid):
                return 0
            if col <0 or col >= len(grid[0]):
                return 0
            if grid[row][col]==0:
                return 0
            grid[row][col] = 0
            return dfs(row+1,col,grid)+dfs(row,col+1,grid)+dfs(row-1,col,grid)+dfs(row,col-1,grid)+1
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    area = max(area,dfs(i,j,grid))
        #print(grid)
        return area
        
        
        