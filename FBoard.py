"""
Start time 06/01/2020 03:17AM CST
Python Assessment from S&P
IDE: Pycharm Professional
--Nagarjuna Thiyyagura
"""


class FBoard:
    def __init__(self):
        # Empty Board Initialized
        self.__board = [[' ' for i in range(8)] for j in range(8)]
        # Set o Pieces position
        self.__board[5][7] = self.__board[6][6] = self.__board[7][5] = self.__board[7][7] = 'o'
        '''for i in range(8):
            print(self.__board[i])'''
        # Set game state to unfinished
        self.__game_state = 'UNFINISHED'
        # x piece at 0,0
        self.__xpiece = [0, 0]

    # return game state
    def get_game_state(self):
        return self.__game_state

    # Check move and make it if it is valid or else return false
    def move_x(self, row, col):
        # check game state
        if self.__game_state == "UNFINISHED":
            # check valid row and column values 0,0-7,7
            if [0, 0] <= [row, col] <= [7, 7]:
                # check the move whether it is vaild or not
                if [self.__xpiece[0] - 1, self.__xpiece[1] - 1] == [row, col] or [self.__xpiece[0] + 1,
                                                                                  self.__xpiece[1] - 1] == [row,
                                                                                                            col] or [
                    self.__xpiece[0] - 1, self.__xpiece[1] + 1] == [row, col] or [self.__xpiece[0] + 1,
                                                                                  self.__xpiece[1] + 1] == [row, col]:
                    # check the given position is empty or not
                    if self.__board[row][col] == ' ':
                        # change position of x piece
                        self.__board[row][col] = 'x'
                        self.__board[self.__xpiece[0]][self.__xpiece[1]] = ' '
                        self.__xpiece = [row, col]  # assign new coordinated to private value
                        # if the piece is at 7,7 then declare X won and change game state
                        if self.__xpiece == [7, 7]:
                            self.__game_state = "X_WON"
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    # move o piece from x1,y1 to x2,y2
    def move_o(self, f_row, f_col, t_row, t_col):
        # check game sate
        if self.__game_state == "UNFINISHED":
            # check valid row and column values 0,0-7,7
            if ([0, 0] <= [f_row, f_col] < [8, 8]) and ([0, 0] <= [t_row, t_col] <= [8, 8]):
                # check the move whether it is vaild or not 'o' at x1,y1 and empty at x2,y2
                if self.__board[f_row][f_col] == 'o' and self.__board[t_row][t_col] == ' ':
                    '''
                        valid moves 
                        x1-1,y1-1 = x2,y2
                        x1+1,y1-1 = x2,y2
                        x1-1,y1+1 = x2,y2
                        
                        not valid
                        x1+1,x2+1 = x2,y2
                    '''
                    if ([f_row - 1, f_col - 1] == [t_row, t_col] or
                            [f_row + 1, f_col - 1] == [t_row, t_col] or
                            [f_row - 1, f_col + 1] == [t_row, t_col]):
                        # change o piece position
                        self.__board[f_row][f_col] = ' '
                        self.__board[t_row][t_col] = 'o'
                        # check for o piece win
                        row, col = self.__xpiece
                        # check at 1,1 and 6,1 for o piece
                        if row == 0:
                            if col == 0:
                                if self.__board[row + 1][col + 1] == 'o':
                                    self.__gameState = 'O_WON'
                            elif col == 7:
                                if self.__board[row + 1][col - 1] == 'o':
                                    self.__gameState = 'O_WON'
                            # check diagonal positions of when x piece is in 0 row.
                            else:
                                if (self.__board[row + 1][col - 1] == 'o' and
                                        self.__board[row + 1][col + 1] == 'o'):
                                    self.__gameState = 'O_WON'
                        # check at 6,1 for o piece
                        elif row == 7:
                            if col == 0:
                                if self.__board[row - 1][col + 1] == 'o':
                                    self.__gameState = 'O_WON'
                            # check diagonal positions when x piece is in row 7
                            else:
                                if (self.__board[row - 1][col + 1] == 'o' and
                                        self.__board[row - 1][col - 1] == 'o'):
                                    self.__gameState = 'O_WON'
                        else:
                            # check diagonal positions when x piece is in column 0 but not in 0,0
                            if col == 0:
                                if (self.__board[row - 1][col + 1] == 'o' and
                                        self.__board[row + 1][col + 1] == 'o'):
                                    self.__gameState = 'O_WON'
                            # check diagonal positions when x piece is in column 0 but not in 0,7
                            elif col == 7:  # for last column
                                if (self.__board[row - 1][col - 1] == 'o' and
                                        self.__board[row + 1][col - 1] == 'o'):
                                    self.__gameState = 'O_WON'
                            # check all other diagonal positions when x iece is not on the edges of the box
                            else:
                                if ((self.__board[row - 1][col - 1] == 'o') and (
                                        self.__board[row - 1][col + 1] == 'o') and (
                                        self.__board[row + 1][col - 1] == 'o') and (
                                        self.__board[row + 1][col + 1] == 'o')):
                                    self.__gameState = 'O_WON'
                        return True

    def display(self):
        print('')
        for i in range(8):
            print(self.__board[i])
        print('')

fb = FBoard()
fb.display()
fb.move_x(1, 1)
fb.display()
fb.move_x(2, 0)
fb.display()
fb.move_o(6, 6, 5, 5)
fb.display()
print(fb.get_game_state())
fb.move_x(3, 1)
fb.display()
fb.move_x(4, 2)
fb.display()
fb.move_x(5, 3)
fb.display()
fb.move_x(6, 5)
fb.display()
print(fb.get_game_state())

"""
    End time: 06/01/2020 6:01AM CST
"""
