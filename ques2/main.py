from boy import Boy
from girl import Girl
from coup import Coup
from gift import Gift
from generateTest import create
import csv
import logging
from math import log10,exp

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p',
					level=logging.DEBUG,
                    filename='output.txt',
                    filemode='w')


def matchMaker():
	coupList=[]
	with open('boys.csv','rb') as csvfile:
		reader=csv.reader(csvfile,delimiter=',')
		By=[Boy(line[0],int(line[1]),int(line[2]),int(line[3]),line[4],int(line[5]))for line in reader]
		csvfile.close()
	with open('girls.csv','rb') as csvfile:
		reader=csv.reader(csvfile,delimiter=',')
		Gl=[Girl(line[0],int(line[1]),int(line[2]),int(line[3]),line[4])for line in reader]
		csvfile.close()
	logging.info('Match in progress\n')
	#Checking conditions
	for g in Gl:
		for b in By:
			logging.info('Matching:  Girl: ' + g.gname + '  with  Boy: ' + b.bname)
			if g.gstatus==False and b.bstatus==False and g.gattract>=b.battractReq and g.gbudget<=b.bbudget:
				g.gstatus=True
				b.bstatus=True
				g.bf=b.bname
				b.gf=g.gname
				coupList.append(Coup('Couple'+str(len(coupList)+1),b,g))
				#print('-----'+' '+b.battractReq+' '+g.gattract+'\n')
				logging.info('Commitment:  Girl: ' + g.gname + '  got commited with  Boy: ' + b.bname)
				break
			#elif(g.gstatus==True or b.bstatus==True):
			#	print (b.bname +' '+g.gname+' commited\n')
			#elif(g.gbudget>b.bbudget):
			#	print (b.bname+' '+g.gname+' too costly '+b.bbudget+' '+g.gbudget+'\n')
			#elif(b.battractReq>g.gattract):
			#	print (b.bname+' '+g.gname+' hotter '+b.battractReq+' '+g.gattract+' \n')
	logging.info('Match making done')
	with open('gifts.csv','rb') as csvfile:
		reader=csv.reader(csvfile,delimiter=',')
		Gi=[Gift(line[0],int(line[1]),int(line[2]),line[3])for line in reader]
		csvfile.close()
	for c in coupList:
		print c.cname+' : '+c.bobj.bname+' commited to '+c.gobj.gname+'\n'
		if(c.bobj.btypes=='Miser'):
			miserAllocate(c,Gi)
		if(c.bobj.btypes=='Generous'):
			generousAllocate(c,Gi)
		if(c.bobj.btypes=='Geek'):
			geekAllocate(c,Gi)
	print_gifts(coupList)



def miserAllocate(c,Gi):
	remainBud=c.gobj.gbudget
	valueGift=0
	giftAlloc=0
	if(c.gobj.gtypes=='Choosy'):
		for g in Gi:
			if(g.giallocated==False and remainBud>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				#valueGift+=g.givalue
				g.giallocated=True
				if(g.gitypes=='Luxury'):
					giftAlloc+=g.giprice
				g.cname=c.cname
				remainBud-=g.giprice
		c.gobj.ghappiness=log10(max(1,giftAlloc))
	if(c.gobj.gtypes=='Normal'):
		for g in Gi:
			if(g.giallocated==False and remainBud>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				valueGift+=g.givalue
				if(g.gitypes=='Luxury'):
					valueGift+=g.givalue
				g.cname=c.cname
				g.giallocated=True
				remainBud-=g.giprice
		c.gobj.ghappiness=giftAlloc+valueGift
	if(c.gobj.gtypes=='Desperate'):
		for g in Gi:
			if(g.giallocated==False and remainBud>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				valueGift+=g.givalue
				if(g.gitypes=='Luxury'):
					valueGift+=g.givalue
				g.cname=c.cname
				g.giallocated=True
				remainBud-=g.giprice
		c.gobj.ghappiness=exp(min(500,giftAlloc))
	c.bobj.bhappiness=c.bobj.bbudget-giftAlloc
	c.happiness=c.bobj.bhappiness+c.gobj.ghappiness
	compatibleCalculate(c)
def generousAllocate(c,Gi):
	remainBud=c.bobj.bbudget
	valueGift=0
	giftAlloc=0
	if(c.gobj.gtypes=='Choosy'):
		for g in Gi:
			if(g.giallocated==False and remainBud>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				g.giallocated=True
				if(g.gitypes=='Luxury'):
					giftAlloc+=g.giprice
				g.cname=c.cname
				remainBud-=g.giprice
		c.gobj.ghappiness=log10(max(1,giftAlloc))
	if(c.gobj.gtypes=='Normal'):
		for g in Gi:
			if(g.giallocated==False and remainBud>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				valueGift+=g.givalue
				g.cname=c.cname
				g.giallocated=True
				remainBud-=g.giprice
		c.gobj.ghappiness=giftAlloc+valueGift
	if(c.gobj.gtypes=='Desperate'):
		for g in Gi:
			if(g.giallocated==False and remainBud>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				g.cname=c.cname
				g.giallocated=True
				remainBud-=g.giprice
		c.gobj.ghappiness=exp(min(500,giftAlloc))
	c.bobj.bhappiness=c.gobj.ghappiness
	c.happiness=c.bobj.bhappiness+c.gobj.ghappiness
	compatibleCalculate(c)
def geekAllocate(c,Gi):
	remainBud=c.gobj.gbudget
	valueGift=0
	giftAlloc=0
	if(c.gobj.gtypes=='Choosy'):
		for g in Gi:
			if(g.giallocated==False and remainBud>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				g.giallocated=True
				if(g.gitypes=='Luxury'):
					giftAlloc+=g.giprice
				g.cname=c.cname
				remainBud-=g.giprice
		for g in Gi:
			if(g.giallocated==False and g.gitypes=='Luxury' and (remainBud+c.bobj.bbudget-c.gobj.gbudget)>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				g.cname=c.cname
				g.giallocated=True
				if(g.gitypes=='Luxury'):
					giftAlloc+=g.giprice
				remainBud-=g.giprice
				break
		c.gobj.ghappiness=log10(max(1,giftAlloc))
	if(c.gobj.gtypes=='Normal'):
		for g in Gi:
			if(g.giallocated==False and remainBud>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				valueGift+=g.givalue
				g.cname=c.cname
				g.giallocated=True
				remainBud-=g.giprice
		for g in Gi:
			if(g.giallocated==False and g.gitypes=='Luxury' and (remainBud+c.bobj.bbudget-c.gobj.gbudget)>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				valueGift+=g.givalue
				g.cname=c.cname
				g.giallocated=True
				remainBud-=g.giprice
				break
		c.gobj.ghappiness=giftAlloc+valueGift
	if(c.gobj.gtypes=='Desperate'):
		for g in Gi:
			if(g.giallocated==False and remainBud>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				g.cname=c.cname
				g.giallocated=True
				remainBud-=g.giprice
		for g in Gi:
			if(g.giallocated==False and g.gitypes=='Luxury' and (remainBud+c.bobj.bbudget-c.gobj.gbudget)>=g.giprice):
				logging.info('Gifting:  Boy: ' + c.bobj.bname + '  gave his Girlfriend: ' + c.gobj.gname + '  Gift: ' + g.giname + ' of price = ' + str(g.giprice) + ' units')
				c.giftList.append(g)
				giftAlloc+=g.giprice
				g.cname=c.cname
				g.giallocated=True
				remainBud-=g.giprice
				break

		c.gobj.ghappiness=exp(min(500,giftAlloc))
	c.bobj.bhappiness=c.gobj.gintellij
	c.happiness=c.bobj.bhappiness+c.gobj.ghappiness
	compatibleCalculate(c)	

def compatibleCalculate(c):
	c.compatibility=abs(c.bobj.bbudget-c.gobj.gbudget)+abs(c.bobj.bintellij-c.gobj.gintellij)+abs(c.bobj.battract-c.gobj.gattract)
		
def print_gifts(C):
	#prints all the Gifts gifted by Boyfriend for all the Couples
	for c in C:
		print 'Gifts given from Boy:  ' + c.bobj.bname + '  to Girl:  ' + c.gobj.gname + ':'
		for g in c.giftList:
			print 'Gift named:  ' + g.giname + '  of type:  ' + g.gitypes
		print '\n'
	print_rank(C,len(C)/2+1)
def print_rank(C, k):
	#prints the k most Happy Couples and k most Compatible Couples'
	A = sorted(C, key=lambda item: item.happiness, reverse=True)
	B = sorted(C, key=lambda item: item.compatibility, reverse=True)
	print str(k) + ' most Happy couples:'
	for i in range(k):
		print A[i].bobj.bname + ' and ' + A[i].gobj.gname

	print '\n' + str(k) + ' most Compatible couples:'
	for i in range(k):
		print B[i].bobj.bname + ' and ' + B[i].gobj.gname
create()
matchMaker()
