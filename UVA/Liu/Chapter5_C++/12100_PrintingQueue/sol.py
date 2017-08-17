'''
Printer Queue, ACM/ICPC NWERC 2006, UVa 12100.
Date: 16/Aug/2017 
Author: Ruowei Chen
Note: Brute-Force simulation
'''
def canPrint(j, numList):
	priority = j[1] ; 
	for j in range(9, 0, -1):
		if j == priority:
			numList[priority] -= 1 ; 
			return True ; 
		if numList[j] > 0 and j > priority:
			return False ; 
	return False ;

def process(job, numList, pos):
	cur = 1 ; 
	numJob = len(job) ; 
	while cur < numJob:
		if canPrint(job[0], numList):
			if job[0][0] == pos:
				return cur ; 
			else:
				job.pop(0) ; 
				cur += 1 ; 
		else:
			job.append(job.pop(0)) ; 

	return cur ; 

def work():
	num, pos = [int(s) for s in input().split()] ; 
	prior = [int(s) for s in input().split()] ; 
#	print(prior) ; # debug
	job = [] ; 
	numList = [] ; 
	for i in range(0, 10):
		numList.append(0) ; 
	for i in range(0, len(prior)):
		job.append((i, prior[i])) ; 
		numList[prior[i]] += 1 ; 

#	print(job) ; # debug
	result = process(job, numList, pos) ; 
	
	print(result) ; 
	return ;

def main():
	T = int(input()) ;
	for i in range(0, T):
		work() ; 

if __name__ == "__main__":
	main() ; 
