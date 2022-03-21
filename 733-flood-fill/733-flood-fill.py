class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.val = self.image[sr][sc]
        if self.val == newColor:
            return self.image
        def dfs(sr,sc,newColor):
            #print('here')
            self.image[sr][sc] = newColor
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]
            for di in dirs:
                x = sr + di[0]
                y = sc + di[1]
                if 0 <= x < len(self.image) and 0 <= y < len(self.image[0]) and self.val == self.image[x][y]:
                    dfs(x,y,newColor)
        dfs(sr,sc,newColor)
        return self.image
        
        