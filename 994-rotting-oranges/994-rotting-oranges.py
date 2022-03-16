class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    count+=1
        if count == 0:
            return 0
        direction = [(-1,0),(0,-1),(0,1),(1,0)]
        level = 0
        while q:
            size = len(q)
            #print(q)
            for _ in range(size):
                i,j = q.pop(0)
                if grid[i][j] == 1:
                    count-=1
                grid[i][j] = 2
                if count == 0:
                    return level
                for d in direction:
                    x = i + d[0]
                    y = j + d[1]
                    #print(x,y)
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]==1:
                        #grid[x][y] = 2
                        q.append((x,y))
                        #count-=1
            level+=1
        return -1
                
        
        