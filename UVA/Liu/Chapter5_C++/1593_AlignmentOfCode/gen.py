'''
Generate test case for the 1593 problem
'''
import random
import time


def gen():
	random.seed(time.time()) ; 
	numLine = 1000 ; 
	for i in range(0, numLine) : 
		lineLength = random.randint(50, 180) ;
		curlen = 0 ; 
		result = "" ; 
		genSp = True ; 
		while curlen < lineLength:
			if genSp == True:
				# generate spaces
				numSp = int(random.randint(0, lineLength-curlen)/10) ; 
				result += numSp * " " ; 
				curlen += numSp ; 
				genSp = False ; 
			else:
				# generate word
				wordLen = random.randint(1, lineLength-curlen) ; 
				w = "" ; 
				for i in range(0, wordLen):
					w += chr(random.randint(33, 126)) ; 
				result = result + w + " " ;
				curlen = curlen + wordLen + 1 ;
				genSp = True ; 
		print(result) ;	

	return ; 


def main():
	gen() ; 

if __name__ == "__main__":
	main() ;
