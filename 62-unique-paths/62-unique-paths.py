class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] + [0]*(n-1) for _ in range(m)]
        for i in range(n):
            grid[0][i] = 1
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[-1][-1]
        