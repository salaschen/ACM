'''
Trees on the level, Duke 1993, UVa 122
Date: 25/Sep/2017
Author: Ruowei Chen
'''
def isComplete(pathes):
	if "A" not in pathes:
		return False ; 
	for p in pathes:
		if len(p) == 1:
			continue ; 
		if p[:-1] not in pathes:
			return False ; 
	return True ; 

def work():
	pathes = set() ; 
	nodes = [] ; 
	line = "" ;
	try:
		line = input() ; 
	except EOFError:
		return 1 ;
	done = False ; 
	complete = True ; 
	while not done:
		line = line.split() ; 
		for e in line:
			if e == "()":
				done = True ; 
			else:
				value, path = e.strip("()").split(",") ; 
				if value == "":
					complete = False ; 
				if path == "":
					path = "A" ; 
				if path in pathes:
					complete = False ; 
				pathes.add(path) ;
				nodes.append((value,path)) ; 
		if not done:
			line = input() ; 
	
	# going to print the result
	if not isComplete(pathes) or not complete:
		print("not complete") ;
	else:
		nodes = sorted(nodes, key = lambda k: k[1]) ; 
		nodes = sorted(nodes, key = lambda k: len(k[1])) ; 
		result = "" ; 
		# print(nodes) ; # debug
		for i in range(0, len(nodes)):
			if i > 0:
				result += " " ;
			result += nodes[i][0] ; 
		print(result) ;
	return 0 ;

def main():
	T = 0 ; 
	while work() == 0:
		T += 1 ;
	return ; 

if __name__ == "__main__":
	main() ; 
