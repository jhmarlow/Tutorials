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

    def __init__(self, Board, start_row=None, finish_row=None,
                 start_col=None, finish_col=None, marker=None):
        self.Board = Board
        self.start_row = start_row
        self.start_col = start_col
        self.finish_row = finish_row
        self.finish_col = finish_col
        self.marker = marker
    
    def position_to_start(self):
        self.start_row = input("Please enter row: ")
        self.start_col = input("Please enter column: ")
        print("You entered:({},{}) to start".format(self.start_row,
                                                    self.start_col))

    def position_to_finish(self):
        self.finish_row = input("Please enter row: ")
        self.finish_col = input("Please enter column: ")
        print("You entered:({},{}) to finish".format(self.finish_row,
                                                     self.finish_col))

    def move_position(self):
        self.marker = self.Board[self.start_col][int(self.start_row)]
        # don't replace pieces with zeros
        if self.marker == 0:
            self.marker = self.Board[self.finish_col][int(self.finish_row)]
            print(" \n No piece selected \n ")
        self.Board[self.start_col][int(self.start_row)] = 0
        # detect piece type being moved
        self.Board[self.finish_col][int(self.finish_row)] = self.marker
        return board


# Create board
brd = init_board(8, 8)
board = brd.create_board()
board = brd.rename_rows(board)

# Create pieces
pcs = init_pieces(board)
board = pcs.initiate_white()
board = pcs.initiate_black()
print(board)

for x in range(0, 5):
    # Make moves
    mk_mv = make_move(board)
    mk_mv.position_to_start()
    mk_mv.position_to_finish()
    # Update board
    try:
        mk_mv.move_position()
    except Exception:
        print("\n Msg: Coordinates do not exist please try again \n")

    print(board)
