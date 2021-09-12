class Sudoku:
    def __init__(self,*args) -> None:
        # self.__grid_value = [['.']*9]*9  # 2-D list holds all the value
        self.__grid_value = [["5","3",".",".","7",".",".",".","."],
                           ["6",".",".","1","9","5",".",".","."],
                           [".","9","8",".",".",".",".","6","."],
                           ["8",".",".",".","6",".",".",".","3"],
                           ["4",".",".","8",".","3",".",".","1"],
                           ["7",".",".",".","2",".",".",".","6"],
                           [".","6",".",".",".",".","2","8","."],
                           [".",".",".","4","1","9",".",".","5"],
                           [".",".",".",".","8",".",".","7","9"]]
    def __traverse_row(self,x,y):
        for i in range(9):
            if self.__grid_value[x][i] == '.':
                yield self.__grid_value[x][i]
            else:    
                yield int(self.__grid_value[x][i])
    def __traverse_column(self,x,y):
        for i in range(9):
            if self.__grid_value[i][y] == '.':
                yield self.__grid_value[i][y]
            else:
                yield int(self.__grid_value[i][y])
    def __traverse_grid(self,x,y):
        x,y = 3*(x//3),3*(y//3)
        for i in range(3):
            for j in range(3):
                if self.__grid_value[x+i][y+j] == '.':
                    yield self.__grid_value[x+i][y+j]
                else:
                    yield int(self.__grid_value[x+i][y+j])
    def display(self):
        for i in range(0,9):
            if i in [0,3,6]:         # to make difference between grid
                print('-'*18)
            for j in range(0,9,3):
                print(self.__grid_value[i][j],self.__grid_value[i][j+1],self.__grid_value[i][j+2],sep=',',end='|')
            print()

    def check_row(self):
        compare_dict ={x:1 for x in range(1,10)}
        compare_dict['.'] = 9
        for i in range(9):
            dummy_compare = compare_dict.copy()
            for i in self.__traverse_row(i,0):
                if i not in dummy_compare.keys():
                    return False
                else:
                    dummy_compare[i] -= 1
                    if dummy_compare[i] < 0:
                        return False
        return True
    
    def check_columns(self):
        compare_dict ={x:1 for x in range(1,10)}
        compare_dict['.'] = 9
        for i in range(9):
            dummy_compare = compare_dict.copy()
            for i in self.__traverse_column(0,i):
                if i not in dummy_compare.keys():
                    return False
                else:
                    dummy_compare[i] -= 1
                    if dummy_compare[i] < 0:
                        return False
        return True

    def check_grid(self):
        compare_dict ={x:1 for x in range(1,10)}
        compare_dict['.'] = 9
        for i in range(9):
            dummy_compare = compare_dict.copy()
            for k in self.__traverse_grid(i//3,i%3):
                if k not in dummy_compare.keys():
                    return False
                else:
                    dummy_compare[k] -= 1
                    if dummy_compare[k] < 0:
                        return False
        return True
    def isvalid(self):
        return self.check_row() and self.check_columns() and self.check_grid()

    def isFilled(self):
        for i in range(9):
            if '.' in self.__grid_value[i]:
                return False
        return True
    def isSolved(self):
        return self.isFilled() and self.isvalid()
    def possibleSolution(self,x,y):
        list_reference = [i for i in range(1,10)] 
        number_taken = [i for i in self.__traverse_grid(x,y) if i != '.']
        number_taken += [i for i in self.__traverse_row(x,y) if i != '.']
        number_taken += [i for i in self.___traverse_column(x,y) if i != '.']
        
        for i in list(set(list_reference).difference(number_taken)):
            yield i 

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.__grid_value[i][j] == '.':
                    for k in self.possibleSolution(i,j):
                        self.__grid_value[i][j] = k
                        self.solve()    
                        self.__grid_value[i][j] = '.'
                    return
        
        if s.isSolved():
            print('\n\n')
            self.display()
            input('')
        return



    


s = Sudoku()
s.display()
print(s.isvalid())
s.solve()



