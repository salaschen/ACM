import math

def padWord(word, requiredLen):
	pad = word ; 
	for i in range(0, requiredLen-len(word)):
		pad += " "  ;
	return pad ;

def work():
	numFile = 0 ; 
	try:
		numFile = int(input()) ; 
	except EOFError:
		return 1 ; 
	files = [] ; 
	maxLen = 0 ; 
	for i in range(0, numFile):
		fn = input().strip() ; 
		if len(fn) > maxLen: 
			maxLen = len(fn) ; 
		files.append(fn) ; 
	files = sorted(files) ; 
	numPerRow = 1 + int((60 -  maxLen) / (maxLen+2)) ;
	numRow = int(math.ceil(len(files) / numPerRow)) ; 
	# print out the dashes
	line = "" ; 
	for i in range(0, 60):
		line += "-" ; 
	print(line) ; 
	# print out each line
	for i in range(0, numRow):
		line = "" ; 
		for j in range(0, numPerRow):
			if i+j*numRow < len(files):
				line += padWord(files[i+j*numRow], maxLen+2) ; 
			else:
				break ; 
		line = line[0:-2] ; # remove the last 2 spaces
		print(line) ; 
	return 0 ;

def main():
	c = 0 ; 
	while work() == 0:
		c = c + 1 ; 
	return ; 

if __name__ == "__main__":
	main() ; 
