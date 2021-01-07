
def isLeft(position):
	"""
	Tells us if the position is on the far left of the chess board
	"""
        if (position%8==0):
                return True
        else:
                return False

def isRight(position):
	"""
	Tells us if the position is on the far right of the chess board
	"""
        if ((position+1)%8==0):
                return True
        else:
                return False

def GetPlayerPositions(board,player):
	"""
	Returns a list of all of the player's current positions on the board
	"""
        accum = []
        if (player == 20):
                for i in range(0,len(board)):
                        if (board[i] >= 20):
                                accum = accum + [i]
                return accum
        elif (player == 10):
                for i in range(0,len(board)):
                        if (board[i] >= 10 and board[i] < 20):
                                accum = accum + [i]
                return accum
        else:
                print("ERROR")
                return accum

def isWhite(board,position):
	"""
	Tells us if the particular position on the board is being occupied by white
	"""
        if (board[position]>=10 and board[position]<20):
                return True
        else:
                return False

def isBlack(board,position):
	"""
	Tells us if the particular position on the board is being occupied by black
	"""
        if (board[position]>=20):
                return True
        else:
                return False

def PawnLegalMoves(board,position):
	"""
	Returns all the legal moves of the Pawn located at 'position' based on the state of the board
	"""
        accum = []
        if (isWhite(board,position) == True):
                if (position+8<=63 and board[position+8]==0):
                        accum = accum + [position+8]
                if (isLeft(position)==False and position+7<=63 and isBlack(board,position+7)==True):
                        accum = accum + [position+7]
                if (isRight(position)==False and position+9<=63 and isBlack(board,position+9)==True):
                        accum = accum + [position+9]
                return accum
        elif (isBlack(board,position) == True):
                if (position-8>=0 and board[position-8]==0):
                        accum = accum + [position-8]
                if (isLeft(position)==False and position-9>=0 and isWhite(board,position-9)==True):
                        accum = accum + [position-9]
                if (isRight(position)==False and position-7>=0 and isWhite(board,position-7)==True):
                        accum = accum + [position-7]
                return accum

def KnightLegalMoves(board,position):
	"""
	Returns all the legal moves of the knight located at 'position' based on the state of the board
	"""
        accum = []
        if (isWhite(board,position)==True):
                if (isLeft(position)==False and position+15<=63):
                        if (isWhite(board,position+15)==False):
                                accum = accum + [position+15]
                if (isRight(position)==False and position+17<=63):
                        if (isWhite(board,position+17)==False):
                                accum = accum + [position+17]
                if (isLeft(position-1)==False and position+6<=63):
                        if (isWhite(board,position+6)==False):
                                accum = accum + [position+6]
                if (isRight(position+1)==False and position+10<=63):
                        if (isWhite(board,position+10)==False):
                                accum = accum + [position+1]
                if (isLeft(position-1)==False and position-10>=0):
                        if (isWhite(board,position-10)==False):
                                accum = accum + [position-10]
                if (isLeft(position)==False and position-17>=0):
                        if (isWhite(board,position-17)==False):
                                accum = accum + [position-17]
                if (isRight(position+1)==False and position-6>=0):
                        if (isWhite(board,position-6)==False):
                                accum = accum + [position-6]
                if (isRight(position)==False and position-15>=0):
                        if(isWhite(board,position-15)==False):
                                accum = accum + [position-15]
                return accum
	elif (isBlack(board,position)==True):
                if (isLeft(position)==False and position+15<=63):
                        if (isBlack(board,position+15)==False):
                                accum = accum + [position+15]
                if (isRight(position)==False and position+17<=63):
                        if (isBlack(board,position+17)==False):
                                accum = accum + [position+17]
                if (isLeft(position-1)==False and position+6<=63):
                        if (isBlack(board,position+6)==False):
                                accum = accum + [position+6]
                if (isRight(position+1)==False and position+10<=63):
                        if(isBlack(board,position+10)==False):
                                accum = accum + [position+1]
                if (isLeft(position-1)==False and position-10>=0):
                        if(isBlack(board,position-10)==False):
                                accum = accum + [position-10]
                if (isLeft(position)==False and position-17>=0):
                        if(isBlack(board,position-17)==False):
                                accum = accum + [position-17]
                if (isRight(position+1)==False and position-6>=0):
                        if(isBlack(board,position-6)==False):
                                accum = accum + [position-6]
                if (isRight(position)==False and position-15>=0):
                        if(isBlack(board,position-15)==False):
                                accum = accum + [position-15]
                return accum
        else:
                return accum

def diagDR(board,position):
	"""
	Returns a list of all legal moves in the down-right direction 
	"""
        accum = []
        n = position
        if (isWhite(board,position)==True):
                while True:
                        if (n-7<0 or n-7>63):
                                break
                        if(isRight(n)==True):
                                break
                        if (isWhite(board,n-7)==True):
                                break
                        if (isBlack(board,n-7)==True):
                                n = n - 7
                                accum = accum + [n]
                                break
                        else:
                                n = n - 7
                                accum = accum + [n]
                return accum
        elif(isBlack(board,position)==True):
                while True:
                        if (n-7<0 or n-7>63):
                                break
                        if(isRight(n)==True):
                                break
                        if (isBlack(board,n-7)==True):
                                break
                        if (isWhite(board,n-7)==True):
                                n = n - 7
                                accum = accum + [n]
                                break
                        else:
                                n = n - 7
                                accum = accum + [n]
                return accum

def diagDL(board,position):
	"""
	Returns a list of all legal moves in the down-left direction 
	"""
        accum = []
        n = position
        if (isWhite(board,position)==True):
                while True:
                        if (n-9<0 or n-9>63):
                                break
                        if (isLeft(n)==True):
                                break
                        if (isWhite(board,n-9)==True):
                                break
                        if (isBlack(board,n-9)==True):
                                n = n - 9
                                accum = accum + [n]
                                break
                        else:
                                n = n - 9
                                accum = accum + [n]
                return accum
        elif(isBlack(board,position)==True):
                while True:
                        if (n-9<0 or n-9>63):
                                break
                        if (isLeft(n)==True):
                                break
                        if (isBlack(board,n-9)==True):
                                break
                        if (isWhite(board,n-9)==True):
                                n = n - 9
                                accum = accum + [n]
                                break
                        else:
                                n = n - 9
                                accum = accum + [n]
                return accum

def diagUR(board,position):
	"""
	Returns a list of all legal moves in the up-right direction 
	"""
        accum = []
        n = position
        if (isWhite(board,position)==True):
                while True:
                        if (n+9<0 or n+9>63):
                                break
                        if (isRight(n)==True):
                                break
                        if (isWhite(board,n+9)==True):
                                break
                        if (isBlack(board,n+9)==True):
                                n = n + 9
                                accum = accum + [n]
                                break
                        else:
                                n = n + 9
                                accum = accum + [n]
                return accum

        elif(isBlack(board,position)==True):
                while True:
                        if (n+9<0 or n+9>63):
                                break
                        if (isRight(n)==True):
                                break
                        if (isBlack(board,n+9)==True):
                                break
                        if (isWhite(board,n+9)==True):
                                n = n + 9
                                accum = accum + [n]
                                break
                        else:
                                n = n + 9
                                accum = accum + [n]
                return accum

def diagUL(board,position):
	"""
	Returns a list of all legal moves in the up-left direction 
	"""
        accum = []
        n = position
        if (isWhite(board,position)==True):
                while True:
                        if (n+7<0 or n+7>63):
                                break
                        if (isLeft(n)==True):
                                break
                        if (isWhite(board,n+7)==True):
                                break
                        if (isBlack(board,n+7)==True):
                                n = n + 7
                                accum = accum + [n]
                                break
                        else:
                                n = n + 7
                                accum = accum + [n]
                return accum
        elif(isBlack(board,position)==True):
                while True:
                        if (n+7<0 or n+7>63):
                                break
                        if (isLeft(n)==True):
                                break
                        if (isBlack(board,n)==True):
                                break
                        if (isWhite(board,n)==True):
                                n = n + 7
                                accum = accum + [n]
                                break
                        else:
                                n = n + 7
                                accum = accum + [n]
                return accum

def BishopLegalMoves(board,position):
	"""
	Returns all the legal moves of the bishop located at 'position' based on the state of the board
	"""
        accum = []
        accum = accum + diagUR(board,position)
        accum = accum + diagUL(board,position)
        accum = accum + diagDR(board,position)
        accum = accum + diagDL(board,position)
        return accum

def Up(board,position):
	"""
	Returns a list of all legal moves in the upward direction 
	"""
        accum = []
        n = position
        if (isWhite(board,position)==True):
                while True:
                        if (n+8<0 or n+8>63):
                                break
                        if (isWhite(board,n+8)==True):
                                break
                        if (isBlack(board,n+8)==True):
                                n = n + 8
                                accum = accum + [n]
                                break
                        else:
                                n = n + 8
                                accum = accum + [n]
                return accum
        elif(isBlack(board,position)==True):
                while True:
                        if (n+8<0 or n+8>63):
                                break
                        if (isBlack(board,n+8)==True):
                                break
                        if (isWhite(board,n+8)==True):
                                n = n + 8
                                accum = accum + [n]
                                break
                        else:
                                n = n + 8
                                accum = accum + [n]
                return accum
def Down(board,position):
	"""
	Returns a list of all legal moves in the downward direction 
	"""
        accum = []
        n = position
        if (isWhite(board,position)==True):
                while True:
                        if (n-8<0 or n-8>63):
                                break
                        if (isWhite(board,n-8)==True):
                                break
                        if (isBlack(board,n-8)==True):
                                n = n - 8
                                accum = accum + [n]
                                break
                        else:
                                n = n - 8
                                accum = accum + [n]
                return accum
        elif(isBlack(board,position)==True):
                while True:
                        if (n-8<0 or n-8>63):
                                break
                        if (isBlack(board,n-8)==True):
                                break
                        if (isWhite(board,n-8)==True):
                                n = n - 8
                                accum = accum + [n]
                                break
                        else:
                                n = n - 8
                                accum = accum + [n]
                return accum

def Right(board,position):
	"""
	Returns a list of all legal moves in the rightward direction 
	"""
        accum = []
        n = position
        if (isWhite(board,position)==True):
                while True:
                        if (n+1<0 or n+1>63):
                                break
                        if(isRight(n)==True):
                                break
                        if (isWhite(board,n+1)==True):
                                break
                        if (isBlack(board,n+1)==True):
                                n = n + 1
                                accum = accum + [n]
                                break
                        else:
                                n = n + 1
                                accum = accum + [n]
                return accum
        elif(isBlack(board,position)==True):
                while True:
                        if (n+1<0 or n+1>63):
                                break
                        if (isRight(n)==True):
                                break
                        if (isBlack(board,n+1)==True):
                                break
                        if (isWhite(board,n+1)==True):
                                n = n + 1
                                accum = accum + [n]
                                break
                        else:
                                n = n + 1
                                accum = accum + [n]
                return accum

def Left(board,position):
	"""
	Returns a list of all legal moves in the leftward direction 
	"""
        accum = []
        n = position
        if (isWhite(board,position)==True):
                while True:
                        if (n-1<0 or n-1>63):
                                break
                        if (isLeft(n)==True):
                                break
                        if (isWhite(board,n)==True):
                                break
                        if (isBlack(board,n)==True):
                                n = n - 1
                                accum = accum + [n]
                                break
                        else:
                                n = n - 1
                                accum = accum + [n]
                return accum
        elif(isBlack(board,position)==True):
                while True:
                        if (n-1<0 or n-1>63):
                                break
                        if (isLeft(n)==True):
                                break
                        if (isBlack(board,n)==True):
                                break
                        if (isWhite(board,n)==True):
                                n = n - 1
                                accum = accum + [n]
                                break
                        else:
                                n = n - 1
                                accum = accum + [n]
                return accum

def RookLegalMoves(board,position):
	"""
	Returns all the legal moves of the Rook located at 'position' based on the state of the board
	"""
        accum = []
        accum = accum + Up(board,position)
        accum = accum + Down(board,position)
        accum = accum + Left(board, position)
        accum = accum + Right(board,position)
        return accum

def QueenLegalMoves(board,position):
	"""
	Returns all the legal moves of the Queen located at 'position' based on the state of the board
	"""
        accum = []
        accum = accum + Up(board,position)
        accum = accum + Down(board,position)
        accum = accum + Left(board, position)
        accum = accum + Right(board,position)
        accum = accum + diagUR(board,position)
        accum = accum + diagUL(board,position)
        accum = accum + diagDR(board,position)
        accum = accum + diagDL(board,position)
        return accum

def KingLegalMoves(board,position):
	"""
	Returns all the legal moves of the King located at 'position' based on the state of the board
	"""
        accum = []
        n = position
        if (isWhite(board,position)==True):
                if (n-7>=0 and isRight(n)==False):
                        if(isWhite(board,n-7)==False):
                                accum = accum + [n-7]
                if (n+7<=63 and isLeft(n)==False):
                        if(isWhite(board,n+7)==False):
                                accum = accum + [n-7]
                if (n-9>=0 and isLeft(n)==False):
                        if(isWhite(board,n-9)==False):
                                accum = accum + [n-9]
                if (n+9<=63 and isRight(n)==False):
                        if(isWhite(board,n+9)==False):
                                accum = accum + [n+9]
                if (n-8>=0):
                        if(isWhite(board,n-8)==False):
                                accum = accum + [n-8]
                if (n+8<=63):
                        if(isWhite(board,n+8)==False):
                                accum = accum + [n+8]
                if (n-1>=0 and isLeft(n)==False):
                        if(isWhite(board,n-1)==False):
                                accum = accum + [n-1]
                if (n+1<=63 and isRight(n)==False):
                        if(isWhite(board,n+1)==False):
                                accum = accum + [n+1]
                return accum
 	elif (isBlack(board,position)==True):
                if (n-7>=0 and isRight(n)==False):
                        if isBlack(board,n-7)==False:
                                accum = accum + [n-7]
                if (n+7<=63 and isLeft(n)==False):
                        if (isBlack(board,n+7)==False):
                                accum = accum + [n-7]
                if (n-9>=0 and isLeft(n)==False):
                        if (isBlack(board,n-9)==False):
                                accum = accum + [n-9]
                if (n+9<=63 and isRight(n)==False):
                        if(isBlack(board,n+9)==False):
                                accum = accum + [n+9]
                if (n-8>=0):
                        if(isBlack(board,n-8)==False):
                                accum = accum + [n-8]
                if (n+8<=63):
                        if(isBlack(board,n+8)==False):
                                accum = accum + [n+8]
                if (n-1>=0 and isLeft(n)==False):
                        if(isBlack(board,n-1)==False):
                                accum = accum + [n-1]
                if (n+1<=63 and isRight(n)==False):
                        if(isBlack(board,n+1)==False):
                                accum = accum + [n+1]
                return accum

def originalGetPieceLegalMoves(board,position):
	"""
	Returns all the legal moves of the piece located at 'position' based on the state of the board
	"""
        if(board[position]%10 == 0 and board[position]<>0):
                return PawnLegalMoves(board,position)
        elif(board[position]%10 == 1):
                return KnightLegalMoves(board,position)
        elif(board[position]%10 == 2):
                return BishopLegalMoves(board,position)
        elif(board[position]%10 == 3):
                return RookLegalMoves(board,position)
        elif(board[position]%10 == 4):
                return QueenLegalMoves(board,position)
        elif(board[position]%10 == 5):
                return KingLegalMoves(board,position)


def MovePlayerCopy(board,pos1,pos2):
	"""
	Moves player from pos1 to pos2
	Note - doesn't check if move is legal
	"""
	board[pos2] = board[pos1]
	board[pos1] = 0
	return True

def isPlayerKingDead(board,player):
	"""
	Tells us if player's king is dead
	Args: player (White = 10, Black=20) 
	"""
	if (player == 10):
		dead = 0
		for i in board:
			if (i==15):
				dead = dead - 1
		if (dead == -1):
			return False
		elif (dead == 0):
			return True
	elif (player == 20):
		dead = 0
		for i in board:
			if (i==25):
				dead = dead - 1
		if (dead == -1):
			return False
		elif (dead == 0):
			return True
	
def WillMoveKillKing(board,position1,position2):
	"""
	Tells us if moving from position1 to position2 will kill player's own King
	The player is determined by first identifying whether the piece at position1 is black or white
	"""

	# find dout who is playing
	piece = board[position1]
	if (piece>=10 and piece<20):
		player = 10
	elif (piece>=20):
		player = 20

	# find out if the move will kill the King
	bcopy = list(board)
	MovePlayerCopy(bcopy,position1,position2)	
	KingsDeath = isPlayerKingDead(bcopy,player)	
	if (KingsDeath == True):
		return True
	elif (KingsDeath == False):
		return False	


def GetPieceLegalMoves(board,position): 
	"""
	Returns a list of all moves for the piece in 'position', where
	moves are the final positions the piece can legally move towards
	"""

        if(board[position]%10 == 0 and board[position]<>0):
                origList = PawnLegalMoves(board,position)
		rList = []
		for i in origList:	# i is pos2
			if (WillMoveKillKing(board,position,i)==False):
				rList = rList + [i]	
		return rList
        elif(board[position]%10 == 1):
                origList = KnightLegalMoves(board,position)
		rList = []	
		for i in origList:
			if (WillMoveKillKing(board,position,i)==False):
				rList = rList + [i]
		return rList
        elif(board[position]%10 == 2):
                origList = BishopLegalMoves(board,position)
		rList = []
		for i in origList:
			if (WillMoveKillKing(board,position,i)==False):
				rList = rList + [i]
		return rList
        elif(board[position]%10 == 3):
                origList = RookLegalMoves(board,position)
		rList = []
		for i in origList:
			if (WillMoveKillKing(board,position,i)==False):
				rList = rList + [i]
		return rList
        elif(board[position]%10 == 4):
                origList = QueenLegalMoves(board,position)
		rList = []
		for i in origList:
			if(WillMoveKillKing(board,position,i)==False):
				rList = rList + [i]
		return rList
        elif(board[position]%10 == 5):
                origList = KingLegalMoves(board,position)
		rList = []	
		for i in origList:
			if(WillMoveKillKing(board,position,i)==False):
				rList = rList + [i]
		return rList

def isMoveLegal(board,position1,position2):
	"""
	Tells us if the move from position1 to position2 is legal based on the state of the board
	and the piece currently on position1
	"""
        x = list(GetPieceLegalMoves(board,position1))
        goodness = 0
        for i in range (0,len(x)):
                if (x[i] == position2):
                        goodness = goodness + 1
        if (goodness == 1):
                return True
        else:
                return False

def IsPositionUnderThreat(board,position,player):
	"""
	Tells us if the piece on 'position' is under threat by the opponent
	i.e. it can be captured on the next play
	"""
        breaktime = False
        Threat = False
        if (player>=10 and player<20):
                n = 0
                while (breaktime == False):
                        if (n==63):
                                if (isBlack(board,n)==True):
                                        moves = GetPieceLegalMoves(board,n)
                                        dangerscore = 0
                                        for i in moves:
                                                if (i==position):
                                                        dangerscore = dangerscore + 1
                                        if (dangerscore > 0):
                                                Threat = True
                                        breaktime = True

                                else:
                                        breaktime = True
                        else:
                                if(isBlack(board,n)==False):
                                        n = n + 1
                                elif(isBlack(board,n)==True):
                                        moves = GetPieceLegalMoves(board,n)
                                        dangerscore = 0
                                        for i in range(0,len(moves)):
                                                if (moves[i]==position):
                                                        dangerscore = dangerscore + 1
                                        if (dangerscore > 0):
                                                Threat = True
                                                breaktime = True
                                        else:
                                                n = n + 1
        elif(player >= 20):
                n = 0
                while (breaktime == False):
                        if (n==63):
                                if (isWhite(board,n)==True):
                                        type(GetPieceLegalMoves(board,n))
                                        moves = GetPieceLegalMoves(board,n)
                                        dangerscore = 0
                                        for i in moves:
                                                if (i==position):
                                                        dangerscore = dangerscore + 1
                                        if (dangerscore > 0):
                                                Threat = True
                                        breaktime = True
                                else:
                                        breaktime = True
                        else:
                                if(isWhite(board,n)==False):
                                        n = n + 1
                                elif(isWhite(board,n)==True):
                                        moves = GetPieceLegalMoves(board,n)
                                        dangerscore = 0
                                        for i in moves:
                                              if (i==position):
                                                        dangerscore = dangerscore + 1
                                        if (dangerscore > 0):
                                                Threat = True
                                                breaktime = True
                                        else:
                                                n = n + 1
        if (Threat == True):
                return True

        elif(Threat == False):
                return False


 
