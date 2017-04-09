from boy import Boy

class miserBoy(Boy):
	def __init__(self,bname,battract,bintellij,bbudget,btypes,battractReq):
		Boy.__init__(self,bname,battract,bintellij,bbudget,btypes,battractReq)
		self.bstatus=False
		self.bhappiness=0
		self.gf=''
