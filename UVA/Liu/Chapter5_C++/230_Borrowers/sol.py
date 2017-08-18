'''
Python solution for Borrowers, ACM/ICPC World Finals 1994, UVa 230
Date: 17/Aug/2017
Author: Ruowei Chen
'''

def getBookBefore(bid, shelf):
	beforeId = bid - 1 ; 
	while True:
		if beforeId < 0:
			return -1 ; 
		elif beforeId in shelf:
			return beforeId ; 
		else:
			beforeId -= 1 ; 
	return -1; 

def process(books, index, shelf, returnList):
	returnList = sorted(returnList) ; 
	length = len(returnList) ;
	for i in range(0, length):
		bid = returnList.pop(0) ; 
		beforeId = getBookBefore(bid, shelf) ;
		title = books[bid][0] ; 
		if beforeId == -1:
			print("Put {0} first".format(title)) ;
		else:
			title0 = books[beforeId][0] ;
			print("Put {0} after {1}".format(title, title0)) ; 
		shelf.add(bid) ; 
	print("END") ; 
	return ; 

def work():
	books = [] ; 
	shelf = set() ; # book's id set.
	index = dict() ; # book's name->book'id
	while True:
		line = input() ; 
		if line == "END":
			break ;
		name, author = line.split("by") ; 
		books.append((name.strip(), author.strip())) ; 
	
	books = sorted(books, key=lambda b: b[0]) ; 
	books = sorted(books, key=lambda b: b[1]) ; 
	for i in range(0, len(books)):
		name = books[i][0] ; 
		index[name] = i ; 
		shelf.add(i) ; 
#	print(index) ; # debug
	
	returnList = [] ; # list of book's id
	while True:
		line = input().strip() ; 
		if line == "SHELVE":
			process(books, index, shelf, returnList) ; 
			returnList = [] ; 
		elif line == "END":
			break ; 
		else:
			name = line[7:].strip() ; 
			if line[:6] == "BORROW":
				shelf.remove(index[name]) ; 
			else:
				returnList.append(index[name]) ; 

	return ; 


def main():
	 work() ; 

if __name__ == "__main__":
	main() ; 
