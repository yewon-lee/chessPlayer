from chessPlayer_Helpers import *
from random import randint
from chessPlayer_tree import tree

def genBoard():
	"""
	Initializes the chess playing board
	Returns the board as a single list with all players placed in their starting positions
	10's indicate white players
	20's indicate black players
	"""
	board = [13,11,12,14,15,12,11,13]+8*[10]+32*[0]+8*[20]+[23,21,22,24,25,22,21,23]
	return board

def getDisp(board):
	accum = ''
	for i in range(0,len(board)):	
		if (board[i]==0 and (i+1)%8==0):
			accum = accum + str('#')+'   '
		elif(board[i]==0 and (i+1)%8<>0):
			accum = accum + str('#')+'   '
		elif(board[i]<>0 and (i+1)%8==0):
			accum = accum + str(board[i])+'  '
		else:
			accum = accum + str(board[i])+'  '
	return accum
	
def printDisp(board):
	"""
	Prints the current state of the board (list) in a 2D manner
	"""
	accum = getDisp(board)
	print(accum[224:255]+'\n')
	print(accum[192:223]+'\n')
	print(accum[160:191]+'\n')
	print(accum[128:159]+'\n')
	print(accum[96:127]+'\n')
	print(accum[64:95]+'\n')
	print(accum[32:63]+'\n')
	print(accum[0:31]+'\n')
	return True


def MovePlayer(board,position1,position2):
	"""
	Moves the player on position1 to position2
	position1 becomes empty (0)
	"""
	if (isMoveLegal(board,position1,position2)==True):
		board[position2]=board[position1]
		board[position1]=0
		return True
	else:
		return False
	
def hasWon(board):
	"""
	Returns True if the game is over, else returns False (i.e. both kings are alive)
	"""
	numKings = 0
	for i in range(0,len(board)):	
		if (board[i] == 15 or board[i]==25):
			numKings = numKings + 1
	if (numKings == 2):
		return False
	else:
		return True

def hasPlayerWon(board,player):
	"""
	Tells us if 'player' won the game given the state of the board
	"""
	dummy = 0
	if (player == 10):
		for i in range(0,len(board)):
			if(board[i]==15):
				dummy = dummy + 1
			if(board[i]==25):
				dummy = dummy - 1
		if(dummy == 1):
			return True
		else:
			return False
	elif (player == 20):
		for i in range(0,len(board)):
			if(board[i]==25):
				dummy = dummy + 1
			if(board[i]==15):
				dummy = dummy - 1
		if(dummy==1):
			return True
		else:
			return False
	else:
		print("ERROR: invalid player for hasPlayerWon function")
		return False	

def LetsPlay_ModifiedToTest(board):
	done = False
	printDisp(board)
	white_positions = GetPlayerPositions(board,10)
	print("INFO: these are white's positions: "+str(white_positions))
	for i in range (0,len(white_positions)):
		print(white_positions[i])
		x = GetPieceLegalMoves(board,white_positions[i])
		for j in range (0,len(x)):
			print('		 INFO: printing legal moves by above position')
			print('		'+str(x[j]))
			threat_or_not = IsPositionUnderThreat(board,x[j],10)
			if (threat_or_not==True):
				print("^under threat if you do this move")
			else:
				print("^not under threat if you do this move")
	printDisp(board)
        black_positions = GetPlayerPositions(board,20)
        print("these are black's positions: "+str(black_positions))
	for i in range (0,len(black_positions)):
        	print(black_positions[i])
                x = GetPieceLegalMoves(board,black_positions[i])
                for j in range (0,len(x)):
                	print("		INFO: printing legal moves by above position")
			print('         '+str(x[j]))
                        threat_or_not = IsPositionUnderThreat(board,x[j],20)
                        if (threat_or_not==True):
                        	print("^under threat if you do this move")
                        else:
                        	print("^not under threat if you do this move")

	return True


def NonCapturingMoves(board,player):
	"""
	Returns a list of all legal moves of 'player' that doesn't lead to the capture of the piece being moved
	"""
	accum = []
	L = GetPlayerPositions(board,player)	# get positions of player 10 or 20
	for i in L:				# for each of these positinos
		x = GetPieceLegalMoves(board,i) # get the legal moves
		for j in x:			# for each of these legal moves
			if(IsPositionUnderThreat(board,j,player)==False):	# take away only the legal moves that won't lead to the thingy's capture
				accum = accum + [[i,j]] #index 0 = original posn, index 1 = final posn
	return accum	
		
		
def AutoPlay(board):

	"""
	Takes in board as argument
	While no one has won, calling this function will have the chess AI play (black) agaisnt a random play generator (white)
	"""	

	done = False
	while True:
		printDisp(board)
		print("\n")
		print("\n")
		positions_white_list = NonCapturingMoves(board,10)
		a = randint(0,len(positions_white_list)-1) #get some random index to take a random position from position1whitelist
		white_choice = positions_white_list[a]
		position1_white = white_choice[0]
		position2_white = white_choice[1]
		MovePlayer(board,position1_white,position2_white)
		
		if (hasWon(board)==True):
			print("Game Over: white won")
			break
	
		printDisp(board)
		print("\n")
		print("\n")
		positions_black_list = NonCapturingMoves(board,20)
		b = randint(0,len(positions_black_list)-1)
		black_choice = positions_black_list[b]
		position1_black = black_choice[0]
		position2_black = black_choice[1]
		MovePlayer(board,position1_black,position2_black)
		
		if (hasWon(board)==True):
			print("Game Over: black won")
			break

	return True			

				
def findKingPosition(board,player):
	"""
	Finds the position of the king
	Args: 
		- board: list
		- player: white (10) or black (20)
	Assumption: king of the player hasn't been killed
	"""

	if (player==10):
		for i in range(0,64):
			if (board[i]==15):
				return i
	elif (player == 20):
		for i in range(0,64):
			if (board[i]==25):
				return i

def isKingUnderThreat(board,player):
	"""
	Returns True or False depending on whether the king's position is under threat by opponent of player
	Args:
		- board: list
		- player: white (10) or black (20)
	""
	KingPos = findKingPosition(board,player)
	return IsPositionUnderThreat(board,KingPos,player) 


def MoveToWin(board,player):
	"""
	Returns the move that will lead to an immediate win, if available
	"""
	moves = genLegalMoves(board,player)	
	for i in moves:
		bc = list(board)
		MovePlayer(bc,i[0],i[1])	
		if (hasPlayerWon(bc,player)==True):
			rval = [True,i]
			return rval
	rval = [False,None]	
	return rval


def avg(List):
	"""
	Finds average value of a list
	"""
	accum = 0
	for i in List:
		accum = accum + i
	return float(accum)/(len(List))

def OpponentOf(player):
	"""
	Returns opponenet of player
	"""
	if (player==10):
		return 20
	elif(player==20):
		return 10
	else:
		print("ERR: invalid player no.")
		return False


def genLegalMoves(board,player):
	"""
	Returns list of all legal moves of the player
	"""
	accum = []
	L = GetPlayerPositions(board,player)
	for i in L:
		x = GetPieceLegalMoves(board,i)
		for j in x:
			accum = accum + [[i,j]]					
	return accum 


def ConvertPosToScore(List,board): 
	"""
	Converts the positions to a score
	Args: List (positions occupied by player), board (current board, a list)
	"""
	
	accum = []
	acc = 0
	for i in List:
		if (board[i]%10 == 0):
			accum = accum + [1]
		elif (board[i]%10 == 1):
			accum = accum + [3]
		elif (board[i]%10 == 2):
			accum = accum + [3]
		elif (board[i]%10 == 3):
			accum = accum + [5]
		elif (board[i]%10 == 4):
			accum = accum + [9]
		elif (board[i]%10 == 5):
			accum = accum + [20]

	# convert list of scores into a single number
	for i in range(0,len(accum)):
		acc = acc + accum[i]
	return acc

def P1MinusP2(board,player): 
	#P1 = Whte, P2 = Blk
	P1 = GetPlayerPositions(board,player)
	P2 = GetPlayerPositions(board,OpponentOf(player))
	P1Score = ConvertPosToScore(P1,board)
	P2Score = ConvertPosToScore(P2,board)
	return float(P1Score - P2Score)

def pickMax(List):
	"""
	Pick the maximum element of the list
	"""
	if (len(List)==0):
		print("ERR: can't compute max")
		return False
	else: 
		Max = float(List[0])
		for i in List:
			if (i>=Max):
				Max = i
		return Max

def pickMin(List):
	if (len(List)==0):
		print("ERR: can't compute Min")
		return False
	else:
		Min = float(List[0])
		for i in List:
			if(i<=Min):
				Min = i
		return Min
		

def MaxMinTree(board,player): 
        if (len(NonCapturingMoves(board,player))==0):
		Whte_Moves_1 = genLegalMoves(board,player)
	elif (len(NonCapturingMoves(board,player))<>0):
		Whte_Moves_1 = NonCapturingMoves(board,player) 
        moves = []
        root = tree(0)

	# i = white's moves
        for i in Whte_Moves_1: # first make white make a move 
                board_copy = list(board)
                MovePlayer(board_copy,i[0],i[1]) # for each move make the move
                if (len(genLegalMoves(board_copy,OpponentOf(player)))>0):
			Blk_Moves_1 = genLegalMoves(board_copy,OpponentOf(player))  #change??	# after you make the move make blk respond
                elif (len(genLegalMoves(board_copy,OpponentOf(player)))==0):
			Blk_Moves_1 = originalgenLegalMoves(board_copy,OpponentOf(player))
		y = tree(i)	# make each of whites moves a tree 
		accum2 = []

		# j = black's moves
                for j in Blk_Moves_1: # for each of blks responds moves
                        bcc = list(board_copy)
			MovePlayer(bcc,j[0],j[1])	
                        # here, accum to j the score that corresponds to each move (i.e. j)
			jTree = tree(j)			# make blk's move a tree
                        y.AddSuccessor(jTree)		# add blks move to whites move (form the tree)
			if (len(genLegalMoves(bcc,player))>0):
	                        Whte_Moves_2 = genLegalMoves(bcc,player)
			elif(len(genLegalMoves(bcc,player))==0):
				Whte_Moves_2 = originalgenLegalMoves(bcc,player)
			accum3 = []

			for k in Whte_Moves_2:
				bccc = list(bcc)	
				MovePlayer(bccc,k[0],k[1]) 
				newpos2 = k[1]
				k = k + [P1MinusP2(bccc,player)]
				kTree = tree(k)
				jTree.AddSuccessor(kTree)
				accum3 = accum3 + [k[2]]

			jTree.store[0] = jTree.store[0] + [pickMax(accum3)]		
			accum2 = accum2 + [pickMax(accum3)]
		
		y.store[0] = y.store[0] + [pickMin(accum2)] # for whte's score node, pick the one that maximizes p1-p2
        	root.AddSuccessor(y)			# add each of whtes moves as a successor to the root
		moves = moves + [y.store[0]]
	
	# print moves
	Max = [moves[0]]	# max is 3-list 
	for i in moves:
		if (i[2]>Max[0][2]):
			Max = [i]
		elif (i[2]==Max[0][2]):
			Max = Max + [i]

	# print Max
	choice = randint(0,len(Max)-1)
	root.store[0] = Max[choice]

	# return the tree
        return [root,moves]					
	
def pickTop3(originalCMs):

	# pick top1
	Max1 = originalCMs[0]
	for i in originalCMs:
		if (i>=originalCMs):
			Max1 = i
	copy1 = []
	for i in originalCMs:
		if (i<>Max1):
			copy1 = copy1 + [i]

	# pick top2
	Max2 = copy1[0]
	for i in copy1:
		if (i>=Max2):
			Max2 = i
	copy2 = []
	for i in copy1:
		if(i<>Max2):
			copy2 = copy2 + [i]

	# pick top3
	Max3 = copy2[0]
	for i in copy2:
		if (i>=Max3):
			Max3 = i
	return [Max1,Max2,Max3]

	
def chessPlayer(board,player):

	if (hasWon(board)==True):
		rval = [False,None,None,None]
		return rval
	elif (len(GetPlayerPositions(board,player))==0):
		rval = [False,None,None,None]
		return rval
	elif (len(genLegalMoves(board,player))==0):
		rval = [False,None,None,None]
		return rval
	else:
		status = True # may need to expand on this list
		mtw = MoveToWin(board,player)
		if (mtw[0]==True):
			move = mtw[1]
			MMTList = MaxMinTree(board,player)
		        treeroot = MMTList[0]
		        originalCMs = MMTList[1]
	        	candidateMoves = []
		        for i in originalCMs:
        		        candidateMoves = candidateMoves + [[i[0:2],i[2]]]
		        evalTree = treeroot.Get_LevelOrder()		
	
		elif(mtw[0]==False):
			# move & candidate moves
			MMTList = MaxMinTree(board,player)
			treeroot = MMTList[0]
			originalCMs = MMTList[1]
			candidateMoves = []
			for i in originalCMs:
				candidateMoves = candidateMoves + [[i[0:2],i[2]]]	
			move = treeroot.store[0][0:2]
			
			# evalTree
			evalTree = treeroot.Get_LevelOrder()
				
		rval = [status,move,candidateMoves,evalTree]
		return rval




