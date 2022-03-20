class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j,board,put):
            if not(0 <= i < len(board)):
               return
            if not(0 <= j < len(board[0])):
               return 
            if board[i][j] != 'O' :
                return 
                 
            
                   
            #print(i,j)
            board[i][j] = '@'
            dfs(i+1,j,board,put)
            dfs(i-1,j,board,put)
            dfs(i,j-1,board,put)
            dfs(i,j+1,board,put)
        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i,0,board,'@')
            if board[i][len(board[0])-1] == 'O':
                dfs(i,len(board[0])-1,board,'@')
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(0,j,board,'@')
            if board[len(board)-1][j]=='O':
                dfs(len(board)-1,j,board,'@')

                
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '@':
                    board[i][j] = 'O'
    
        