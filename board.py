import config as c

class Chess_Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board_x=[]

        for x in range(8):
            board_y =[]
            for y in range(8):

                board_y.append('.')

            board_x.append(board_y)
        board_x[7][7] = 'R'
        board_x[7][6] = 'N'
        board_x[7][5] = 'B'
        board_x[7][4] = 'K'
        board_x[7][3] = 'Q'
        board_x[7][2] = 'B'
        board_x[7][1] = 'N'
        board_x[7][0] = 'R'
        for i in range(8):
            board_x[6][i] = 'P'
        #board_x[6][0] = 'P'
        return board_x


    def pawn_number(self):
        print('quel numéro? 0 gauche 7 droite')
        c.num_pion=str(input())
        return c.num_pion
