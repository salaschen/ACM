'''
UVa 548 - Tree
Date: 26/Sep/2017
Author: Ruowei Chen
'''

def buildTree(inOrder, postOrder):
	if len(inOrder) == 1 and len(postOrder) == 1:
		return inOrder[0] ;
	elif len(inOrder) == 0:
		return None ; 
	else:
		# print(inOrder, postOrder) ;  # debug
		length = len(postOrder) ; 
		root = postOrder[length-1] ; 
		div = inOrder.index(root) ; 
		llen, rlen = len(inOrder[:div]), len(inOrder[div+1:]) ; 
		left = buildTree(inOrder[:div], postOrder[:div]) ; 
		right = buildTree(inOrder[div+1:], postOrder[div:div+rlen]) ; 
		return (root, (left, right)) ; 

# Get the leaf which has the shortest path to the root
def process(root):
	node, value = getValue(root, 0) ; 
	print(node) ; 
	return ; 

def isLeaf(node):
	return type(node) is not tuple ;

def getValue(node, pathValue):
	if isLeaf(node): 
		return (node, pathValue+node) ; 
	else:
		lnode, lvalue = None, 0 ;
		rnode, rvalue = None, 0 ; 
		if node[1][0] != None:
			lnode, lvalue = getValue(node[1][0], node[0]+pathValue) ; 
		if node[1][1] != None:
			rnode, rvalue = getValue(node[1][1], node[0]+pathValue) ; 
		if lnode is None:
			return (rnode, rvalue) ; 
		elif rnode is None:
			return (lnode, lvalue) ; 
		else:
			if lvalue < rvalue:
				return (lnode, lvalue) ; 
			elif lvalue > rvalue:
				return (rnode, rvalue); 
			else:
				if lnode < rnode:
					return (lnode, lvalue) ; 
				else:
					return (rnode, rvalue) ;
	return None ; # should not reach this

def work():
	line = "" ; 
	try:
		line = input() ; 
	except EOFError:
		return 1 ; 
	
	inOrder = [int(s) for s in line.split()] ;
	postOrder = [int(s) for s in input().split()] ;
#	print(inOrder, postOrder) ; # debug
	root = buildTree(inOrder, postOrder) ; 
	# print(root) ; # debug
	process(root); 
	return 0 ;

def main():
	T = 0 ; 
	while work() == 0:
		T += 1 ;
	return ;

if __name__ == "__main__":
	main() ;
