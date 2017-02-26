class Girl:
	#Gal Classs

	def __init__(self,gname,gattract,gintellij,gbudget,gtypes):
		self.gname=gname
		self.gattract=gattract
		self.gintellij=gintellij
		self.gbudget=gbudget
		self.gtypes=gtypes
		self.gstatus=False
		self.bf=''
	def ellig_check(self,bbudget):
		if(self.gstatus==True):
			return False
		if(self.gbudget<=bbudget):
			return True
		else:
			return False