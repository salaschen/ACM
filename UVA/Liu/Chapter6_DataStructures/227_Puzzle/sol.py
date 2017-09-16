'''
Uva227 Puzzle. Write a program to display resulting frames given
their initial configuration and sequences of moves.
'''

def printConfig(Case, config, isLegal):
	if Case > 1:
		print() ; 
	print("Puzzle #" + str(Case) + ":") ; 
	if isLegal == False:
		print("This puzzle has no final configuration.") ;
		return ; 
	for i in range(0, 5):
		line = "" ; 
		for j in range(0, 5):
			if j > 0:
				line += " " ; 
			line += config[i*5+j] ; 
		print(line) ;
	return ; 

def work(Case):
	'''
	Work function. Return 1 if end is reached.
	'''
	line = input();
	if line == "Z":
		return 1 ; # end
	config = [] ;
	if len(line) == 4:
		line += " " ; 
	for c in line:
		config.append(c) ; 
	for i in range(0, 4):
		line = input() ;
		if len(line) == 4:
			line += " " ; 
		for c in line:
			config.append(c) ; 
#	print("config", config) ; # debug
	moves = [] ; 
	endMoves = False ; 
	while not endMoves:
		line = input().strip()  ; 
		for m in line:
			if m == "0":
				endMoves = True ; 
			else:
				moves.append(m) ; 
#	print("moves", moves) ; # debug
	
	# process moves
	if " " in config:
		blankPos = config.index(" ") ; 
		isLegal = True ; 
	else:
		isLegal = False ; 
	while isLegal and len(moves) > 0:
		curMove = moves.pop(0) ; 
		nextPos = 0 ; 
		if curMove == "A":
			if blankPos < 5:
				isLegal = False ; 
				break ; 
			else:
				nextPos = blankPos - 5 ;
		elif curMove == "R":
			if blankPos % 5 == 4:
				isLegal = False ; 
				break ; 
			else:
				nextPos = blankPos + 1;
		elif curMove == "L":
			if blankPos % 5 == 0:
				isLegal = False ;
				break ; 
			else:
				nextPos = blankPos - 1 ;
		elif curMove == "B":
			if blankPos >= 20:
				isLegal = False ; 
				break ; 
			else:
				nextPos = blankPos + 5 ;
		else:
			isLegal = False ; 
			break ; 
		
		config[blankPos] = config[nextPos] ;
		config[nextPos] = " " ;
		blankPos = nextPos ; 

	printConfig(Case, config, isLegal) ; 

	return 0 ;


def main():
	Case = 1 ; 
	while True:
		if work(Case) == 1:
			break ; 
		Case += 1 ;
	return ; 

if __name__ == "__main__":
	main() ; 
