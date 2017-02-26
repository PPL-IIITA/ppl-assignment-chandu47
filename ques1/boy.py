class Boy:
	#Buoy Classs

	def __init__(self,bname,battract,bintellij,bbudget,btypes,battractReq):
		self.bname=bname
		self.battract=battract
		self.bintellij=bintellij
		self.bbudget=bbudget
		self.btypes=btypes
		self.battractReq=battractReq
		self.bstatus=False
		self.gf=''
	def ellig_check(self,minBudget,gfAttract):
		if(self.bstatus==True):
			return False
		if(self.battractReq<=gfAttract and self.bbudget>=minBudget):
			return True

		else:
			if(self.battractReq>gfAttract):
				print (self.bname+'not attractive\n')
			elif(self.bbudget<minBudget):
				print 'costly\n'
			return False
