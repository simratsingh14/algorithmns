class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.ans = 0
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    border = 0
                    for d in dirs:
                        x,y = i+d[0],j+d[1]
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]:
                            border+=1
                    #print(i,j,border)
                
                    self.ans += (4 - border)
        return self.ans
        