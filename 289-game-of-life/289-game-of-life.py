class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()
        d = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]:
                    q.append((i,j))
        #print(q)
        dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        while q:
            i,j = q.popleft()
            for di in dirs:
                x = i + di[0]
                y = j + di[1]
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    d[(x,y)]+=1
        #print(d)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]:
                    if not(d[(i,j)] == 2 or d[(i,j)] == 3):
                        board[i][j] = 0
                else:
                    if d[(i,j)] == 3:
                        board[i][j] = 1
            
        
        