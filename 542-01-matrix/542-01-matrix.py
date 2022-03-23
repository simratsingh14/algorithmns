class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if not mat[i][j]:
                    queue.append((i,j))
                    
        level = 0
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                i,j = queue.pop(0)
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                mat[i][j] = level
                for di in dirs:
                    x = i + di[0] 
                    y = j + di[1]
                    if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == 1:
                        queue.append((x,y))
                
            
            level+=1
        return mat
                    
        
        