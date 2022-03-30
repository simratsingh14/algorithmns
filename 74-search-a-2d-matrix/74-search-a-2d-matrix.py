class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = 0 ,len(matrix[0]) -1
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            #print(row,col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -=1
            else:
                row+=1
        return False
        