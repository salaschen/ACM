
def work():
	line = "" ; 
	lenDict = dict() ; 
	lines = [] ; # to store all the lines.
	while 1:
		try:
			line = input() ; 
		except EOFError:
			break ; 

		# if the line is not empty
		words = line.split() ; 
		wordStrip = [] ; 
		for w in  map(lambda s: s.strip(), words) : 
			wordStrip.append(w) ; 
		for i in range(0, len(wordStrip)):
			w = wordStrip[i] ; 
			if i not in lenDict or lenDict[i] < len(w):
				lenDict[i] = len(w) ; 
		lines.append(wordStrip) ; 

	# output
	for l in lines:
		if (len(l) != 1):
			result = pad(l[0], lenDict[0]) ; 
		else:
			result = l[0] ; 
		if (len(l) > 2):
			for i in range(1, len(l)-1):
				result = result + " " + pad(l[i], lenDict[i]) ; 
		if len(l) > 1:
			result = result + " " + l[len(l)-1] ; 

		print(result) ; 

	return ; 

def pad(word, length):
	numSpace = length - len(word) ; 
	return (word + " " * numSpace) ; 

def main():
	work() ; 
	return 0 ;

if __name__ == "__main__":
	main() ; 
