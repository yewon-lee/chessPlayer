class queue:
	
	def __init__(self):
		self.store = []
	
	def enqueue(self,tree):
		self.store = self.store + [tree]
	
	def dequeue(self):
		x = self.store[0]
		self.store = self.store[1:len(self.store)]
		return x

	def dequeue_diff(self):
		return self.store[1:len(self.store)]

	def Empty(self):
		if (len(self.store) == 0):
			return True
		else:
			return False
	
	
	
