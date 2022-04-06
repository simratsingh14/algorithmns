class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for d in dirs:
                    x = i + d[0]
                    y = j + d[1]
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and (board[x][y] == 2 or board[x][y] == 1):
                        count+=1
                if board[i][j]:
                    if count < 2 or count > 3:
                        board[i][j] = 2
                else:
                    if count == 3:
                        board[i][j] = 3
        
        # 2 -> 1 to 0 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 3:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0
        
        