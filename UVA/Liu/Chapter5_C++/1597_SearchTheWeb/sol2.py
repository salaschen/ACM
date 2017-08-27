'''
Searching the Web, ACM/ICPC Beijing 2004, UVa 1597
Date: 26/Aug/2017 
Note: Version 2. Setup a centralized index instead of a distributed one.
Author: Ruowei Chen
'''

def buildIndex(index, docIndex, docNumber, lineNumber, line, stop):
	tLine = "" ; 
	for i in range(0, len(line)):
		if not line[i].isalpha():
			tLine += " " ;
		else:
			tLine += line[i] ; 
	words = tLine.split() ; 
	for w in words:
		w = w.lower() ; 
		if w in stop:
			continue ; 
		if w in index:
			index[w].add((docNumber, lineNumber)) ; 
			docIndex[w].add(docNumber); 
		else:
			index[w] = set() ;
			index[w].add((docNumber, lineNumber)) ; 
			docIndex[w] = set() ; 
			docIndex[w].add(docNumber) ; 
	return ;


def readInput(texts):
	n = int(input()) ; 
	index = dict() ; 
	docIndex = dict() ;
	stop = ["the", "a", "to", "and", "or", "not"] ; 
	for i in range(0, n):
		line = input() ;
		curLine = 0 ; 
		doc = [] ; 
		while "*"*10 not in line:
			doc.append(line) ; 
			buildIndex(index,docIndex, i, curLine, line, stop) ; 
			line = input(); 
			curLine += 1 ; 
		texts.append(doc) ; 
	return (index, docIndex); 

def prepResult(index, result, docnumSet, word):
	if word not in index:
		return ; 
	for tup in index[word]:
		if tup[0] in docnumSet:
			if tup[0] not in result:
				result[tup[0]] = set() ; 
			result[tup[0]].add(tup[1]) ; 
	return ; 

def testHandleQuery(texts, index, docIndex):
#	handleQuery(texts, index, docIndex, "computer AND course") ; 
#	handleQuery(texts, index, docIndex, "computer AND student") ; 
#	handleQuery(texts, index, docIndex, "computer OR student") ; 
#	handleQuery(texts, index, docIndex, "computer OR books") ; 
#	handleQuery(texts, index, docIndex, "NOT books") ; 
#	handleQuery(texts, index, docIndex, "security") ; 
	handleQuery(texts, index, docIndex, "NOT test") ; 

	return ; 

def handleQuery(texts, index,docIndex, query):
	result = dict(); 
	# handle AND query.
	if "AND" in query:
		ops = query.split() ; 
		w1, w2 = ops[0], ops[2] ; 
		s1, s2 = set(), set() ; 
		if w1 in docIndex and w2 in docIndex:
			s1, s2 = docIndex[w1], docIndex[w2] ; 
		s = s1 & s2 ; # set intersection
		if len(s) > 0:
			prepResult(index, result, s, w1) ; 
			prepResult(index, result, s, w2) ; 
	# handle OR query
	elif "OR" in query:
		ops = query.split() ; 
		w1, w2 = ops[0], ops[2] ; 
		s1, s2 = set(), set() ;
		if w1 in docIndex: 
			s1 = docIndex[w1] ; 
		if w2 in docIndex: 
			s2 = docIndex[w2] ; 
		s = s1 | s2 ; # set union
		if len(s) > 0:
			prepResult(index, result, s, w1) ; 
			prepResult(index, result, s, w2) ; 
	# handle NOT query
	elif "NOT" in query:
		wholeSet = set([i for i in range(0, len(texts))]) ; 
		# print(wholeSet) ; # debug
		ops = query.split() ; 
		w1 = ops[1] ; 
		s1 = set() ; 
		if w1 in docIndex:
			s1 = docIndex[w1] ; 
		l = sorted(wholeSet - s1) ; 
		printWholeDoc(texts, l) ; 
		return ; 
	# handle single word query
	else:
		w1 = query.strip() ; 
		s1 = set() ; 
		if w1 in docIndex:
			s1 = docIndex[w1] ; 
		s = s1 ; 
		if len(s) > 0:
			prepResult(index, result, s, w1) ; 

	# sort the result by line number and docnumber.
	for key in result:
		result[key] = sorted(result[key]) ; 
	# print out result
	printResult(texts, result) ;
	return ; 

def printWholeDoc(texts, docList):
	for i in range(0, len(docList)):
		if i >= 1: 
			print("-"*10) ; 
		docNum = docList[i] ; 
		for l in texts[docNum]:
			print(l) ; 

	if len(docList) == 0:
		print("Sorry, I found nothing.") ; 

	print("="*10) ; 
	return ; 

def printResult(texts, result):
	if len(result) == 0:
		print("Sorry, I found nothing.") ; 
	else:
	#	print(result) ;   #debug
		sorted_key = sorted(result) ; 
		for k in range(0, len(sorted_key)):
			if k >= 1:
				print("-"*10) ; 
			docNum = sorted_key[k] ; 
			lines = result[docNum] ; 
			for l in lines:
				print(texts[docNum][l]) ; 

	print("="*10) ; 
	return ; 

def work():
	texts = [] ; 
	index, docIndex = readInput(texts) ; 
	'''
	# sort the index
	for k in index:
		index[k] = sorted(index[k], key=lambda t: t[1]) ; 
		index[k] = sorted(index[k], key=lambda t: t[0]) ; 
	'''

	# print(index) ; # debug
	# print(docIndex) ; # debug
	# handle queries
	#testHandleQuery(texts, index, docIndex) ; # debug
	
	n = int(input()) ; 
	for i in range(0, n):
		query = input() ; 
		handleQuery(texts, index, docIndex, query) ;

	return ; 

def main():
	work() ; 
	return ; 

if __name__ == "__main__":
	main() ;
