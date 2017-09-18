'''
Matrix Chain Multiplication, UVa 442
Date: 18/Sep/2017 
Author: Ruowei Chen
'''

def evaluate(expression, matrix):
	stack = [] ; 
	result = 0 ; 
	for c in expression:
		if c == "(":
			stack.append(c) ; 
		elif c == ")":
			m2 = stack.pop() ; 
			m1 = stack.pop() ;
			sign = stack.pop() ;
			if type(m2) is not tuple or type(m1) is not tuple or sign != "(":
				print("Something's wrong.") ; 
				return ; 
			if m1[1] != m2[0]:
				print("error") ; 
				return ; 
			else:
				result += (m1[0]*m1[1]*m2[1]) ; 
				stack.append((m1[0], m2[1])) ; 
		else:
			stack.append(matrix[c]) ; 

	print(str(result)) ; 
	return ; 

def work():
	n = int(input()) ; 
	matrix = dict() ; 
	for i in range(0, n):
		name, r, c = input().strip().split() ; 
		matrix[name] = (int(r), int(c)) ; # store as a pair
	
	# now try to evaluate all the expressions.
	while True:
		try:
			line = input() ; 
			evaluate(line, matrix) ; 
		except EOFError:
			break ; 
	return ;
		

def main():
	work() ; 

if __name__ == "__main__":
	main() ; 
