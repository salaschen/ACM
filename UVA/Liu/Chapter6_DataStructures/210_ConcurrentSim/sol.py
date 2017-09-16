'''
Concurrency Simulator, ACM/ICPC World Finals 1991, UVa210
Date: 10/Sep/2017, Sunday.
Author: Ruowei Chen
'''
def getType(instruction):
	if instruction.strip() == "lock":
		return "lock" ; 
	elif instruction.strip() == "end":
		return "end" ; 
	elif instruction.strip() == "unlock":
		return "unlock" ;
	elif "=" in instruction:
		return "assign" ; 
	elif "print" in instruction:
		return "print" ; 
	else:
		return "error" ; 
	return ;

def process(progs, readyQueue, blockedQueue, cost, quantum, var, isLocked):
	'''
	Process the program in the queues.
	Returns the lock status of the current process.
	''' 
	curProg = readyQueue.pop(0) ; 
	hasBlocked = False ; 
	hasEnded = False ; 
	
	while quantum > 0:
		# read the next isntruction
	#	print("curProg="+str(curProg)) ; # debug
		ins = progs[curProg].pop(0) ;
		insType = getType(ins) ; 
		if insType == "lock":
			if isLocked == True:
				hasBlocked = True ; 
				progs[curProg].insert(0, ins) ; # add back the failed lock statement.
				break ; 
			else:
				isLocked = True ; 
		elif insType == "unlock":
			if isLocked == True:
				isLocked = False ; 
			if len(blockedQueue) > 0:
				pid = blockedQueue.pop(0) ; 
				readyQueue.insert(0, pid) ; 
		elif insType == "assign":
			varName, value = ins.strip().split("=") ;
			var[varName.strip()] = int(value.strip()) ; 
		elif insType == "print":
			varName = ins.split()[1].strip() ;
			value = var[varName] ; 
			print(str(curProg)+": " + str(value)) ; 
		elif insType == "end":
			hasEnded = True ; 
			break ; 
		else:
			print("UNKONWN instruction received.") ; 
		quantum -= cost[insType] ; 

	if hasBlocked == True:
		blockedQueue.append(curProg) ; 
	elif hasEnded == False:
		readyQueue.append(curProg) ; 
	
	# print(readyQueue, blockedQueue, isLocked) ; # debug
	return isLocked ; 
	
def work():
	# build up the variables dictionary
	var = dict() ; 
	for a in range(ord('a'), ord('z')+1):
		var[chr(a)] = 0 ; 
	# print(var) ; # debug

	# build up the statement execution time unit
	cost = dict() ; 
	line = input().strip().split() ;
	numProg = int(line[0]) ; 
	cost['assign'] = int(line[1]) ; 
	cost['print'] = int(line[2]) ; 
	cost['lock'] = int(line[3]) ; 
	cost['unlock'] = int(line[4]) ;
	cost['end'] = int(line[5]); 
	quantum = int(line[6]) ; 
	
	# use dictionary to store instructions for each program
	progs = dict() ;
	for i in range(0, numProg):
		progs[i+1] = [] ;
		line = input() ; 
		while True:
			progs[i+1].append(line) ;
			if line == "end":
				break ; 
			line = input().strip() ; 
	# print(progs) ; # debug

	# create two queues, the ready queue and the blocked queue.
	readyQueue = [i for i in range(1, numProg+1)] ; 
	blockedQueue = [] ; 
	isLocked = False ; 
	while len(readyQueue) + len(blockedQueue) > 0:
		isLocked = process(progs, readyQueue, blockedQueue, cost, quantum, var, isLocked) ; 

	return ; 

def main():
	n = int(input()) ; 
	for i in range(0, n):
		input() ; # eat the blank line
		if i >= 1:
			print() ; # blank line to seperate test cases
		work() ; 
	return ; 

if __name__ == "__main__":
	main() ; 
