from girl import Girl

class desperateGirl(Girl):
	def __init__(self,gname,gattract,gintellij,gbudget,gtypes):
		Girl.__init__(self,gname,gattract,gintellij,gbudget,gtypes)
		self.gstatus=False
		self.ghappiness=0
		self.bf=''
