class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        mat = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                for di in dirs:
                    x = i + di[0]
                    y = j + di[1]
                    if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and matrix[i][j] < matrix[x][y]:
                        mat[x][y]+=1
        q = collections.deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if not mat[i][j]:
                    q.append((i,j))
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i,j = q.popleft()
                for di in dirs:
                    x = i + di[0]
                    y = j + di[1]
                    if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and matrix[x][y] > matrix[i][j]:
                        mat[x][y]-=1
                        if not mat[x][y]:
                            q.append((x,y))
            level+=1
        return level
            