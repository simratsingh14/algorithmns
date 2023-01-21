class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initalColor = image[sr][sc]
        if initalColor == color:
            return image
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i=sr,j=sc):
            image[i][j] = color
            
            for d in dirs:
                x,y = i+d[0],j+d[1]
                if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == initalColor:
                    dfs(x,y)
        dfs()
        return image
                
        