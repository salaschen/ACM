'''
Program for UVA 814 The letter Carrier's Rounds
Date: 26/Jun/2017
Note: Consider there's abnormal use of spaces in the input
'''
import functools ;

class MTA:
	def __init__(self, name):
		self.name = name ;
		self.receivers = [] ;
	
	def addRecv(self, recv):
		self.receivers.append(recv) ; 

	def __str__(self):
		result = "MTA" ; 
		result += " " + self.name ; 
		result += " " + str(len(self.receivers)) ; 
		for s in self.receivers:
			result += " " + s ; 
		return result ;
	
	def hasReceiver(self, name):
		return name in self.receivers ; 
# end of class MTA

class Communication:
	def __init__(self):
		self.sender = "" ;
		self.receivers = [] ;
		self.data = "" ;
		self.mDict = dict() ; 
	
	def __str__(self):
		self.buildDict() ;
		result = "*\n" + self.sender ;
		for r in self.receivers:
			result += " " + r ; 
		result += "\n" + self.data + "\n*"; 
		for key in self.mDict:
			result += "\n[" + key + "]:" + str(self.mDict[key]);
		return result ; 

	def buildDict(self):
		mid = 0 ; 
		for r in self.receivers:
			mta = r.split('@')[1] ; 
			if mta not in self.mDict:
				self.mDict[mta] = mid ; 
				mid += 1 ; 
		self.sortReceivers() ; 
		return ; 

	def sortReceivers(self):
		self.receivers = sorted(self.receivers, key=lambda r: self.mDict[r.split('@')[1]]) ; 
		return ; 
# end of class Communication

def readMTA():
	result = [] ;
	desc = "" ; 
	line = input() ; 
	while (line != "*"):
		if line[0:3] != "MTA":
			desc = desc + line + " " ; 
		else:
#			print("desc=" + desc) ; # debug
			names = desc.strip().replace(' ', '@').split('@') ;  
#			print(names) ; # debug
			if desc != "":
				mta = MTA(names[1]) ;
				for n in names[3:]:
					mta.addRecv(n) ;
				result.append(mta) ; 
			desc = line + " " ; 
		line = input() ;
	if desc != "":
		names = desc.strip().replace(' ', '@').split('@') ;  
		mta = MTA(names[1]) ;
		for n in names[3:]:
			mta.addRecv(n) ;
		result.append(mta) ;
	return result ; 

def readComms():
	comm = Communication() ;
	line = "" ; 
	try:
		line = input() ; # try to get names
	except EOFError:
		return "" ; 
	if line == "*":
		return "" ;
	names = line.split() ; 
	comm.sender = names[0] ; 
	for i in range(1, len(names)):
		comm.receivers.append(names[i]) ; 
	line = input() ;
	while line != "*":
		names = line.split(); 
		for n in names:
			comm.receivers.append(n) ; 
		line = input() ;
	line = input() ; # begin to get data
	comm.data = line + "\n" ; 
	line = input() ; 
	while line != "*":
		comm.data += (line + "\n") ; 
		line = input() ;
	comm.data = comm.data.strip() ; # delete the last \n
	return comm ; 


def hasRecv(recv, mtalist):
#	print("recv = " + recv);#debug
	recvName, mtaName = recv.split('@');
#	print("mtaName = " + mtaName); # debug
	for mta in mtalist:
#		print(mta) ; # debug
		if mta.name == mtaName:
			return recvName in mta.receivers;
	return False ;

def processComm(comm, mtalist):
	i = 0 ;
	mList = [[] for x in range(0, len(comm.mDict))] ; 
	for i in range(0, len(comm.receivers)):
		recv = comm.receivers[i] ;
		key = comm.mDict[recv.split('@')[1]];
		mList[key].append(recv) ;
	sp = " " * 5 ; 
	# process each MTA
	for rlist in mList:
		recvMTA = rlist[0].split('@')[1] ;
		sender = comm.sender.split('@')[1] ; 
		sentRecv = set() ; 
		print("Connection between %s and %s" % (sender, recvMTA)) ; 
		print("%sHELO %s\n%s250" % (sp, sender, sp)) ; 
		print("%sMAIL FROM:<%s>\n%s250" % (sp, comm.sender, sp)) ; 
		dataSent = False ; 
		for r in rlist:
			if r not in sentRecv:
				print("%sRCPT TO:<%s>" % (sp,r)) ; 
				if hasRecv(r, mtalist):
					sentRecv.add(r) ; 
					print(sp+"250") ; 
					dataSent = True ; 
				else:
					print(sp+"550") ; 
		if dataSent:
			print(sp+"DATA\n" + sp+"354") ; 
			data = functools.reduce(lambda x, y: x + '\n'+ sp + y, comm.data.split('\n')) ; 
			print(sp + data) ;
			print(sp+".\n"+sp+"250") ; 
		print(sp+"QUIT\n"+sp+"221") ;

	return ; 


def work():
	mtaList = readMTA() ;
#	for m in mtaList:
#		print(m) ; 

	comms = [] ;
	comm = readComms() ; 
	while comm != "":
		comms.append(comm) ; 
		comm = readComms() ; 
	
	# debug print
	for c in comms:
		c.buildDict() ;
#		print(c) ;
		processComm(c, mtaList) ;

	
def main():
	work() ;
	return 0 ;

if __name__ == "__main__":
	main() ; 
