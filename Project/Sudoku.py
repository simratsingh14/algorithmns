class Sudoku:
    def __init__(self,*args) -> None:
        self.grid_value = [['.']*9]*9  # 2-D list holds all the value
        # self.grid_value = [[i for i in range(9)] for j in range(9)]
    def __traverse_row(self,x,y):
        for i in range(9):
            yield self.grid_value[x][i]
    def ___traverse_column(self,x,y):
        for i in range(9):
            yield self.grid_value[i][y]
    def __traverse_grid(self,x,y):
        x,y = x//3,y//3
        for i in range(3):
            for j in range(3):
                yield self.grid_value[x+i][y+j]
    def display(self):
        for i in range(0,9):
            if i in [0,3,6]:         # to make difference between grid
                print('-'*18)
            for j in range(0,9,3):
                print(self.grid_value[i][j],self.grid_value[i][j+1],self.grid_value[i][j+2],sep=',',end='|')
            print()

    def check_row(self):
        sar = {str(i) for i in range(1,10)}
        sar.add('.')
        for i in range(9):
            lar = set([i for i in self.__traverse_row(i,0)])
            if lar != sar:
                return False
        return True


            

        
            


s = Sudoku()
# s.display()
s.display()
print(s.check_row())



