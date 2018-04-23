import board as b
import config as c
    
# -------------------------------------------------------------------
#|                           White King                              |                                          
# -------------------------------------------------------------------

class WHITE_KING(b.Chess_Board):
    def __init__(self):
        b.Chess_Board.__init__(self)
        self.position_x_WK = 7
        self.position_y_WK = 4
        self.symbol_WK = 'K'

    def move(self):
        while True:
            try:
                print ('Choisissez des coordonées X et Y pour WHITE KING')
                destination_x_WK = int(input())
                destination_y_WK = int(input())


                if self.board[destination_x_WK][destination_y_WK] == '.' :

                    if ( abs(self.position_x_WK-destination_x_WK) <2 and abs(self.position_y_WK-destination_y_WK) < 2 ):
                        self.board[self.position_x_WK][self.position_y_WK] = '.'
                        self.position_x_WK = destination_x_WK
                        self.position_y_WK = destination_y_WK
                        self.board[self.position_x_WK][self.position_y_WK] = self.symbol_WK

                        return self.board
                        break

                    else:
                        print ('Votre mouvement est invalide, essayez encore')
                        continue

            except:
                pass

# -------------------------------------------------------------------
#|                           White Queen                             |                                          
# -------------------------------------------------------------------


class WHITE_QUEEN(b.Chess_Board):
    def __init__(self):
        b.Chess_Board.__init__(self)
        self.position_x_WQ = 7
        self.position_y_WQ = 3
        self.symbol_WQ = 'Q'

    def move(self):
        while True:
            try:
                print ('Choisissez des coordonées X et Y pour WHITE QUEEN')
                destination_x_WQ = int(input())
                destination_y_WQ = int(input())


                if self.board[destination_x_WQ][destination_y_WQ] == '.' :

                    if (destination_x_WQ == self.position_x_WQ or destination_y_WQ==self.position_y_WQ or abs(self.position_x_WQ-destination_x_WQ) == abs(self.position_y_WQ-destination_y_WQ) ):
                        self.board[self.position_x_WQ][self.position_y_WQ] = '.'
                        self.position_x_WQ = destination_x_WQ
                        self.position_y_WQ = destination_y_WQ
                        self.board[self.position_x_WQ][self.position_y_WQ] = self.symbol_WQ

                        return self.board
                        break

                    else:
                        print ('Votre mouvement est invalide, essayez encore')
                        continue

            except:
                pass

# -------------------------------------------------------------------
#|                           White Rook                              |                                          
# -------------------------------------------------------------------

class WHITE_ROOK_LEFT(b.Chess_Board):

    def __init__(self):
        b.Chess_Board.__init__(self)
        self.position_x_WRL = 7
        self.position_y_WRL = 0
        self.symbol_WRL = 'R'

    def move(self):
        while True:
            try:
                print ('Choisissez des coordonées X et Y pour WHITE ROOK LEFT ')
                destination_x_WRL = int(input())
                destination_y_WRL = int(input())


                if self.board[destination_x_WRL][destination_y_WRL] == '.' : #Vérifie si les coordonées sont bien un endroit vide

                    if (destination_x_WRL == self.position_x_WRL or destination_y_WRL==self.position_y_WRL  ): #Vérifie si la pièce choisie est bien la bonne
                        self.board[self.position_x_WRL][self.position_y_WRL] = '.' #change l'anciienne position de la pièce par un "."
                        self.position_x_WRL = destination_x_WRL #bouge la pièce
                        self.position_y_WRL = destination_y_WRL #issou
                        self.board[self.position_x_WRL][self.position_y_WRL] = self.symbol_WRL

                        return self.board #renvoie le plateaau avec la pièce bougée
                        break

                    else:
                        print ('Votre mouvement est invalide, essayez encore')
                        continue

            except:
                pass
            
class WHITE_ROOK_RIGHT(b.Chess_Board):

    def __init__(self):
        b.Chess_Board.__init__(self)
        self.position_x_WRR = 7
        self.position_y_WRR = 7
        self.symbol_WRR = 'R'

    def move(self):
        while True:
            try:
                print ('Choisissez des coordonées X et Y pour WHITE ROOK RIGHT')
                destination_x_WRR = int(input())
                destination_y_WRR = int(input())


                if self.board[destination_x_WRR][destination_y_WRR] == '.' : 

                    if (destination_x_WRR == self.position_x_WRR or destination_y_WRR==self.position_y_WRR  ): 
                        self.board[self.position_x_WRR][self.position_y_WRR] = '.' 
                        self.position_x_WRR = destination_x_WRR 
                        self.position_y_WRR = destination_y_WRR 
                        self.board[self.position_x_WRR][self.position_y_WRR] = self.symbol_WRR 

                        return self.board 
                        break

                    else:
                        print ('Votre mouvement est invalide, essayez encore')
                        continue

            except:
                pass

# -------------------------------------------------------------------
#|                           White Bishop                            |  
# -------------------------------------------------------------------

class WHITE_BISHOP_LEFT(b.Chess_Board):
    def __init__(self):
        b.Chess_Board.__init__(self)
        self.position_x_WBL = 7
        self.position_y_WBL = 2
        self.symbol_WBL = 'B'

    def move(self):
        while True:
            try:
                print ('Choisissez des coordonées X et Y pour WHITE BISHOP A ')
                destination_x_WBL = int(input())
                destination_y_WBL= int(input())


                if self.board[destination_x_WBL][destination_y_WBL] == '.' :

                    if  abs(self.position_x_WBL-destination_x_WBL) == abs(self.position_y_WBL-destination_y_WBL) :
                        self.board[self.position_x_WBL][self.position_y_WBL] = '.'
                        self.position_x_WBL = destination_x_WBL
                        self.position_y_WBL = destination_y_WBL
                        self.board[self.position_x_WBL][self.position_y_WBL] = self.symbol_WBL

                        return self.board
                        break

                    else:
                        print ('Votre mouvement est invalide, essayez encore')
                        continue

            except:
                pass

class WHITE_BISHOP_RIGHT(b.Chess_Board):
    def __init__(self):
        b.Chess_Board.__init__(self)
        self.position_x_WBR = 7
        self.position_y_WBR = 5
        self.symbol_WBR = 'B'

    def move(self):
        while True:
            try:
                print ('Choisissez des coordonées X et Y pour WHITE BISHOP B')
                destination_x_WBR = int(input())
                destination_y_WBR = int(input())


                if self.board[destination_x_WBR][destination_y_WBR] == '.' :

                    if  abs(self.position_x_WBR-destination_x_WBR) == abs(self.position_y_WBR-destination_y_WBR) :
                        self.board[self.position_x_WBR][self.position_y_WBR] = '.'
                        self.position_x_WBR = destination_x_WBR
                        self.position_y_WBR = destination_y_WBR
                        self.board[self.position_x_WBR][self.position_y_WBR] = self.symbol_WBR

                        return self.board
                        break

                    else:
                        print ('Votre mouvement est invalide, essayez encore')
                        continue

            except:
                pass

# -------------------------------------------------------------------
#|                           White Knight                            |                                          
# -------------------------------------------------------------------


class WHITE_KNIGHT_LEFT(b.Chess_Board):
    def __init__(self):
        b.Chess_Board.__init__(self)
        self.position_x_WKNL = 7
        self.position_y_WKNL = 1
        self.symbol_WKNL = 'N'

    def move(self):
        while True:
            try:
                print ('Choisissez des coordonées X et Y pour WHITE KNIGHT A')
                destination_x_WKNL = int(input())
                destination_y_WKNL = int(input())


                if self.board[destination_x_WKNL][destination_y_WKNL] == '.' :

                    if abs(self.position_x_WKNL-destination_x_WKNL)**2 + abs(self.position_y_WKNL-destination_y_WKNL)**2 == 5 :
                        self.board[self.position_x_WKNL][self.position_y_WKNL] = '.'
                        self.position_x_WKNL = destination_x_WKNL
                        self.position_y_WKNL = destination_y_WKNL
                        self.board[self.position_x_WKNL][self.position_y_WKNL] = self.symbol_WKNL

                        return self.board
                        break

                    else:
                        print ('Votre mouvement est invalide, essayez encore')
                        continue

            except:
                pass

class WHITE_KNIGHT_RIGHT(b.Chess_Board):
    def __init__(self):
        b.Chess_Board.__init__(self)
        self.position_x_WKNR = 7
        self.position_y_WKNR = 6
        self.symbol_WKNR = 'N'

    def move(self):
        while True:
            try:
                print ('Choisissez des coordonées X et Y pour WHITE KNIGHT B')
                destination_x_WKNR = int(input())
                destination_y_WKNR = int(input())


                if self.board[destination_x_WKNR][destination_y_WKNR] == '.' :

                    if abs(self.position_x_WKNR-destination_x_WKNR)**2 + abs(self.position_y_WKNR-destination_y_WKNR)**2 == 5 :
                        self.board[self.position_x_WKNR][self.position_y_WKNR] = '.'
                        self.position_x_WKNR = destination_x_WKNR
                        self.position_y_WKNR = destination_y_WKNR
                        self.board[self.position_x_WKNR][self.position_y_WKNR] = self.symbol_WKNR

                        return self.board
                        break

                    else:
                        print ('Votre mouvement est invalide, essayez encore')
                        continue

            except:
                pass

# -------------------------------------------------------------------
#|                           White Pawns                             |  
# -------------------------------------------------------------------

class WHITE_PAWNS(b.Chess_Board):
    def __init__(self):
        b.Chess_Board.__init__(self)
        self.position_x_WP0 = 6
        self.position_y_WP0 = c.num_pion
        self.symbol_WP0 = 'P'
        
    def move(self):
        while True:
            try:
                print ('Choisissez des coordonées X et Y pour WHITE PAWN '+str(c.num_pion))
                destination_x_WP0 = int(input())
                destination_y_WP0 = int(input())


                if self.board[destination_x_WP0][destination_y_WP0] == '.' :

                    if (destination_x_WP0 == (self.position_x_WP0)-1):
                        print("condition validée")
                        self.board[self.position_x_WP0][self.position_y_WP0] = '.'
                        self.position_x_WP0 = destination_x_WP0
                        self.position_y_WP0 = destination_y_WP0 
                        self.board[self.position_x_WP0][self.position_y_WP0] = self.symbol_WP0
                        

                        return self.board
                        break

                    else:
                        print ('Votre mouvement est invalide, essayez encore')
                        continue

            except:
                pass

#------------------------------------------------------------------------------


