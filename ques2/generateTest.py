import csv
from random import randint

def boyCreate():
	#Creates boys file
	atrributes=['Miser','Generous','Geek']
	#(Name,Attractiveness,Intelligence,Budget,Type,Attractiveness Requirement)
	B=[('Boy'+str(i+1),randint(1,10),randint(1,10),randint(1,1000),atrributes[randint(0,2)],randint(1,10))for i in xrange(40)]
	with open('boys.csv','wb') as csvfile:
		writer=csv.writer(csvfile,delimiter=',')
		writer.writerows(B)
def girlCreate():
	#Creates girls file
	atrributes=['Choosy','Normal','Desperate']
	#(Name,Attractiveness,Intelligence,Budget,Type)
	G=[('Girl'+str(i+1),randint(1,10),randint(1,10),randint(1,1000),atrributes[randint(0,2)] )for i in xrange(10)]
	with open('girls.csv','wb') as csvfile:
		writer=csv.writer(csvfile,delimiter=',')
		writer.writerows(G)
def giftCreate():
	#Creates gifts file
	atrributes=['Essential','Luxury','Utility']
	#(Name,price,value,Type)
	Gi=[('Gift'+str(i+1),randint(1,100),randint(1,10),atrributes[randint(0,2)] )for i in xrange(100)]
	with open('gifts.csv','wb') as csvfile:
		writer=csv.writer(csvfile,delimiter=',')
		writer.writerows(Gi)

def create():
	boyCreate()
	girlCreate()
	giftCreate()
create()