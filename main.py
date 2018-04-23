import pieces as p
import board as b
import config as c


# -------------------------------------------------------------------
#|                             Engine                                |                                          
# -------------------------------------------------------------------

class Engine(b.Chess_Board):

    def __init__(self):
        p.WHITE_KING.__init__(self)
        p.WHITE_QUEEN.__init__(self)
        p.WHITE_ROOK_LEFT.__init__(self)
        p.WHITE_ROOK_RIGHT.__init__(self)
        p.WHITE_BISHOP_LEFT.__init__(self)
        p.WHITE_BISHOP_RIGHT.__init__(self)
        p.WHITE_KNIGHT_LEFT.__init__(self)
        p.WHITE_KNIGHT_RIGHT.__init__(self)
        p.WHITE_PAWNS.__init__(self)
        b.Chess_Board.__init__(self)

    def play(self):
        print('Choississez quel pièce bouger: white_king, white_queen, white_rook_left/right, white_bishop_left/right'
              ' white knight_left/right ou white_pawn')

        while True:
                choice=str(input())
                if  choice == 'white_king':
                    p.WHITE_KING.move(self)
                    break
                elif  choice == 'white_queen':
                    p.WHITE_QUEEN.move(self)
                    break
                elif  choice == 'white_bishop_left':
                    p.WHITE_BISHOP_LEFT.move(self)
                    break
                elif  choice == 'white_bishop_right':
                    p.WHITE_BISHOP_RIGHT.move(self)
                    break
                elif  choice == 'white_knight_left':
                    p.WHITE_KNIGHT_LEFT.move(self)
                    break
                elif  choice == 'white_knight_right':
                    p.WHITE_KNIGHT_RIGHT.move(self)
                    break
                elif  choice == 'white_rook_left':
                    p.WHITE_ROOK_LEFT.move(self)
                    break
                elif  choice == 'white_rook_right':
                    p.WHITE_ROOK_RIGHT.move(self)
                    break
                elif  choice == 'white_pawn':
                    b.Chess_Board.pawn_number(self)
                    p.WHITE_PAWNS.move(self)
                    break
                else:
                    print ('Choisissez encore')
                


    def display(self):
        for i in range (8):
            for j in range (8):
                print (self.board[i][j], end=' ')
            print ()
    


c_engine = Engine()
c_engine.display()
while True:
    c_engine.play()
    c_engine.display()

