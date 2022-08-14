class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cl=[{} for sub in range(9)]
        rw=[{} for sub in range(9)]
        grid1=[{} for sub in range(9)]
        for row in range(0,len(board)):
            for col in range(0,len(board)):
                digit=board[row][col]
                if(digit=="."):
                    continue
                if(rw[row].get(digit)!=None):
                    return False    
                else:
                    rw[row][digit]=1
                    
                if(cl[col].get(digit)!=None):
                    return False    
                else:
                    cl[col][digit]=1
                    
                grid_r=row//3
                grid_c=col//3
                grid_number=grid_r*3+grid_c
               # print(row,col,grid_r,grid_c,grid_number)
                if(grid1[grid_number].get(digit)!=None):
                    return False
                else:
                    grid1[grid_number][digit]=1
               
        return True
        