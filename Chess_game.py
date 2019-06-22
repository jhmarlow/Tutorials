# Import modules
import numpy as np
import pandas as pd 


class init_board():
    """Initliase dataframe to be used as board in the chess game.

    Returns:
        [dataframe] -- [the chess board]

    """

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def create_board(self):
        """[Create board from size specified].

        Returns:
            [df] -- [board]
        """
        np_array = np.zeros((self.rows, self.columns), dtype=np.int16)
        df_array = pd.DataFrame(np_array)
        return df_array

    def rename_rows(self, dataframe):
        """[rename columns tp letters].

        Arguments:
            dataframe {[pd.Dataframe]} -- [board/dataframe to be renamed]

        Returns:
            [type] -- [description]
        """
        renamed_board = dataframe.rename(columns={0: 'a', 1: 'b', 2: 'c',
                                                  3: 'd', 4: 'e', 5: 'f', 
                                                  6: 'g', 7: 'h'})
        return renamed_board


class init_pieces():
    """[summary]
    
    Returns:
        [type] -- [description]
    """

    def __init__(self, board_in):
        self.board_in = board_in

    def initiate_white(self):
        self.board_in[0:2] = 1
        return self.board_in

    def initiate_black(self):
        self.board_in[-2:] = 2
        return self.board_in


class make_move():
    """Move the pieces using the coordinate system
    
    Returns:
        [DataFrame] -- Update dataframe
    """

    def __init__(self, Board, x1, y1, x2, y2):
        self.Board = Board
        self.x1 = x1 
        self.y1 = y1
        self.x2 = x2 
        self.y2 = y2

    def clear_position(self):
        self.Board[self.x1][self.y1] = 0
        return init_board

    def move_position(self):
        self.Board[self.x2][self.y2] = 2
        return init_board


class terminal_input():
    
    def __init__():
        pass
    
    def position_to_start(self):
        var_row = input("Please enter row: ")
        var_col = input("Please enter column: ")
        print("You entered:({},{}) to start".format(var_row, var_col))

        position_to_start = [var_row, var_col]
        return position_to_start

    def position_to_finish(self):
        var_row = input("Please enter row: ")
        var_col = input("Please enter column: ")
        print("You entered:({},{}) to finish".format(var_row, var_col))

        position_to_finish = [var_row, var_col]
        return position_to_finish


# Create board
brd = init_board(8, 8)
init_board = brd.create_board()
init_board = brd.rename_rows(init_board)

# Create pieces
pcs = init_pieces(init_board)
init_board = pcs.initiate_white()
init_board = pcs.initiate_black()

# Make moves
mk_mv = make_move(init_board, 'g', 6, 'g', 5)
init_board = mk_mv.clear_position()
init_board = mk_mv.move_position()

print(init_board) 
