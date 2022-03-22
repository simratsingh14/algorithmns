class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        self.c = grid[row][col]
        self.grid = grid
        def dfs(r,c):
            self.grid[r][c] = -1*self.grid[r][c]
            count = 0
            dirs = [(-1,0),(0,-1),(0,1),(1,0)]
            for di in dirs:
                x = r + di[0]
                y = c + di[1]
                if 0 <= x < len(self.grid) and 0 <= y <  len(self.grid[0]) and abs(self.grid[x][y]) == self.c:
                    count+=1
                    if self.grid[x][y] > 0:
                        dfs(x,y)
            
            if count == 4:
                self.grid[r][c] *= -1
        
        dfs(row,col)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] < 0:
                    self.grid[i][j] = color
        return self.grid
        
        