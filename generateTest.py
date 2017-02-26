import csv
from random import randint

def boyCreate():
	#Creates boys file
	atrributes=['Miser','Generous','Geek']
	#(Name,Attractiveness,Intelligence,Budget,Type,Attractiveness Requirement)
	B=[('Boy'+str(i+1),randint(1,10),randint(1,10),randint(1,1000),atrributes[randint(0,2)],randint(1,10))for i in xrange(20)]
	with open('boys.csv','wb') as csvfile:
		writer=csv.writer(csvfile,delimiter=',')
		writer.writerows(B)
def girlCreate():
	#Creates girls file
	atrributes=['Choosy','Normal','Desperate']
	#(Name,Attractiveness,Intelligence,Budget,Type)
	G=[('Girl'+str(i+1),randint(1,10),randint(1,10),randint(1,1000),atrributes[randint(0,2)] )for i in xrange(5)]
	with open('girls.csv','wb') as csvfile:
		writer=csv.writer(csvfile,delimiter=',')
		writer.writerows(G)

def create():
	boyCreate()
	girlCreate()