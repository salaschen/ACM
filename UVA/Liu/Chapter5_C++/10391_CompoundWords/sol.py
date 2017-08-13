'''
Prob: UVA 10391 - Compound Words
Date: 13/Aug/2017 
Author: Ruowei Chen
'''

def isCompound(wordSet, word):
	for sep in range(1, len(word)):
		if word[:sep] in wordSet and word[sep:] in wordSet:
			return True ; 
	return False ; 

def work():
	wordSet = set() ; 
	wordList = [] ;
	try:
		while True:
			word = input().strip() ; 
			wordSet.add(word) ; 
			wordList.append(word) ; 
	except EOFError:
		a = 0 ; # do nothing
	
	for w in wordList:
		if isCompound(wordSet, w):
			print(w) ; 
	return ; 

def main():
	work() ; 

if __name__ == "__main__":
	main() ; 
