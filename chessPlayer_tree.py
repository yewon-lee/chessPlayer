from chessPlayer_queue import queue 

class tree:
	
	def __init__(self,x):
		self.store = [x,[]]
		self.n = 0
	
	def AddSuccessor(self,x):
		self.store[1] = self.store[1] + [x]
		x.n = self.n + 1
		return True

	def Print_DepthFirst(self):
		self.Print_DepthFirst_helper("	   ")
		return True
	
	def Print_DepthFirst_helper(self,prefix):
		print prefix+str(self.store[0])
		for i in self.store[1]:
			i.Print_DepthFirst_helper(prefix+"	")
		return True

	def Get_LevelOrder(self):		
		Q = queue()
		Q.enqueue(self.store)
		accum = []
		while (Q.Empty() == False):
			node = Q.dequeue()
			accum = accum + [node[0]]
			for i in range(0,len(node[1])):
				Q.enqueue(node[1][i].store)
		return accum
	
		
	def getFirstLeaf(self):
		X = self.store
		depth = X.getDepth()
		copyTree = list(self.store)
		for i in range(0,depth):
			copyTree = copyTree[1][0].store
		return copyTree


