'''
Updating a Dictionary, UVa12504
Date: 27/Aug/2017
Author: Ruowei Chen
'''

def createDict(line):
	pairs = line.strip("{}").strip().split(",") ; 
	result = dict() ; 
#	print(pairs) ; # debug
	if ":" not in pairs[0]:
		return result ;
	for p in pairs:
		key, value = p.split(":") ;
		result[key] = value ; 
	return result;

def work():
	old_dict = createDict(input()) ; 
	new_dict = createDict(input()) ; 
	
	hasChange = False ; 
	# print(old_dict) ; # debug
	# print(new_dict) ; # debug

	old_keySet = old_dict.keys() ; 
	new_keySet = new_dict.keys() ; 
	
	# new keys added
	s = sorted(new_keySet - old_keySet) ; 
	if len(s) > 0:
		hasChange = True ; 
		line = "+" ; 
		for i in range(0, len(s)):
			if i >= 1:
				line += "," ;
			line += s[i] ; 
		print(line) ; 

	# old keys deleted
	s = sorted(old_keySet - new_keySet) ; 
	if len(s) > 0:
		hasChange = True ; 
		line = "-" ; 
		for i in range(0, len(s)):
			if i >= 1:
				line += "," ;
			line += s[i] ; 
		print(line) ; 

	# keys changed
	same = old_keySet & new_keySet ; 
	s = [] ; 
	for key in same:
		if old_dict[key] != new_dict[key]:
			s.append(key) ; 
	s = sorted(s) ; 
	if len(s) > 0:
		hasChange = True ; 
		line = "*" ; 
		for i in range(0, len(s)):
			if i >= 1:
				line += "," ;
			line += s[i] ; 
		print(line) ; 

	if hasChange == False:
		print("No changes") ; 

	print() ;
	return ; 

def main():
	n = int(input()) ; 
	for i in range(0, n):
		work() ; 
#	print() ;
	return 0; 

if __name__ == "__main__":
	main();
