'''
Revenge of Fibonacci, ACM/ICPC Shanghai 2011, UVa 12333
Date: 30/Aug/2017 
Note: Too slow for building up the nodes, fail.
Update: 
	1) Try again using Trie.
	2) Try using string representation addition instead of int and cast back to string
'''
class Trie:
	def __init__(self, value):
		self.index = value ; 
		self.children = [None for i in range(0, 10)] ; 
	
	def addToRoot(self, fib): # fib is (strNumber, index)
		b = int(fib[0][0]) ; 
		if self.children[b] is None:
			self.children[b] = Trie(None) ; 
		self.children[b].addToTrie(fib, 1) ; 
		return ; 
	
	def __str__(self):
		result = str(self.index) + ": ["; 
		for c in self.children:
			if c is not None:
				result += " " + str(c.index) ; 
			else:
				result += " " + str(c) ; 
		result += "]" ; 
		return result ; 

	def addToTrie(self, fib, pos):
		if len(fib[0]) == pos or pos == 40:
			if self.index == None:
				self.index = fib[1] ; 
		else:
			b = int(fib[0][pos]) ; 
			if self.children[b] == None:
				self.children[b] = Trie(None) ;
			self.children[b].addToTrie(fib, pos+1); 
			if self.index == None or self.index > fib[1]:
				self.index = fib[1] ; 
		return ; 
	
	def findRoot(self, query): # query is a string of at least one, at most 40 digits.
		b = int(query[0]) ; 
		if self.children[b] == None:
			return -1 ; 
		else:
			return self.children[b].findTrie(query, 1) ; 
	
	def findTrie(self, query, pos):
		if len(query) == pos:
			if self.index != None:
				return self.index ; 
			else:
				return -1 ; 
		else:
			b = int(query[pos]) ;
			if self.children[b] == None:
				return -1 ; 
			else:
				return self.children[b].findTrie(query, pos+1); 

def strAdd(s1, s2):
	result = "" ; 
	carry = '0' ;
	l1 = len(s1); 
	l2 = len(s2) ; 
	pos1 = l1-1 ; 
	pos2 = l2-1 ; 
	while pos1 >= 0 or pos2 >= 0 or carry == '1':
		c1 = s1[pos1] if pos1 >= 0 else '0' ;
		c2 = s2[pos2] if pos2 >= 0 else '0' ; 
		pos1 -= 1 ; 
		pos2 -= 1 ; 
		c3, carry = charAdd(c1, c2, carry) ; 
		result = c3 + result ; 
#	print("{0}+{1}={2}".format(s1, s2, result)) ; # debug
	return result ; 

def testStrAdd():
	a = "123" ; 
	b = "894" ; 
	strAdd(a,b) ; 
	return ; 

def charAdd(c1, c2, carry):
	c1 = int(c1) ; 
	c2 = int(c2) ; 
	carry = int(carry) ;
	result = c1 + c2 + carry ;
	carry = '0' ; 
	if result >= 10:
		result = str((result % 10)) ; 
		carry = '1' ; 
	else:
		result = str(result) ;
	return (result, carry) ;

def printTrie(root):
	if root is None:
		return ; 
	print(str(root)) ;
	if root is not None:
		for c in root.children:
			printTrie(c) ; 
	return ; 

def testTrie():
	root = genTrie(50000) ; 
#	printTrie(root) ; 
	n = int(input()) ; 
	for i in range(0, n):
		query = input().strip() ; 
		print(root.findRoot(query)) ; 
	'''
	print(root.findRoot('8')) ; 
	print(root.findRoot('89')) ;
	print(root.findRoot('123')) ;
	'''

	return ;
	
def genTrie(n):
	root = Trie("Root") ; 
	fib0 = '1' ; 
	fib1 = '1' ; 
	index = 0  ; 
	while index <= n:
		root.addToRoot((str(fib0), index)) ; 
		print("fib({0}) added".format(index, fib0)) ;  #debug
		temp = fib1 ; 
		fib1 = strAdd(fib0,fib1) ; # fib0+fib1 ;
		# fib1 = strAdd(fib0[:50], fib1[:50]) ; 
		fib0 = temp ; 
		index += 1 ; 
	return root ; 

	
def work():
	'''
	trie = genTrie(100000) ;
	print("Gen trie finished") ; # debug
	n = int(input()) ; 
	for i in range(0, n):
		query = input().strip() ;
		result = trie.findRoot(query) ;
		print(result) ; 
	'''
	testTrie() ; # debug
	return ; 

def main():
	work() ;

if __name__ == "__main__":
	main() ; 
