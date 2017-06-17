

def work():
	row, col = 0, 0 ; 
	line = "" ;
	try:
		row, col = [int(s) for s in input().split()]
	except EOFError:
		return 1 ; 
	table = [ ["" for x in range(0, col)] for y in range(0, row)] ; 
	wDict = dict() ; # word dict
	wId = 0 ; 
	for i in range(0, row):
		line = input() ;
		values = line.split(',') ; 
		for j in range(0, col):
			if values[j] not in wDict:
				wDict[values[j]] = wId + 1 ;
				wId += 1 ; 
			table[i][j] = values[j] ; 
#	print(table) ; # debug
	# scan through the table and store the key:value in the dictionary
	tDict = dict() ; 
	for i in range(0, row):
		tRow = table[i] ;
		for j in range(0, col-1):
			for k in range(j+1, col):
				key = tRow[j] + "," + tRow[k] ; 
				value = (i, j, k) ; # tuple
				if key in tDict: # redundancy is found
					r, c1, c2 = tDict[key] ; 
					if c1 == j and c2 == k and r != i:
						print("NO") ; 
						print("%d %d" % (r+1, i+1)) ; 
						print("%d %d" % (c1+1, c2+1)) ; 
						return 0 ; 
				else:
					tDict[key] = value ;
	print("YES") ; 
	return 0 ; 

def main():
	c = 0 ; 
	while work() == 0:
		c += 1 ; 

if __name__ == "__main__":
	main() ;
