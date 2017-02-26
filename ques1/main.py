from boy import Boy
from girl import Girl
from generateTest import create
import csv
import logging

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p',
					level=logging.DEBUG,
                    filename='output.txt',
                    filemode='w')


def matchMaker():
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
	for g in Gl:
		if g.gstatus == False:
			print 'A Girl: ' + g.gname + '  has no boyfriend'
		else:
			print 'A Girl: ' + g.gname + '  has a boyfriend Boy: ' + g.bf

create()
matchMaker()
