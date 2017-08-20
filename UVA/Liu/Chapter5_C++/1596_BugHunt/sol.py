'''
Bug Hunt, ACM/ICPC Tokyo 2007, UVa 1596.
Date: 18/Aug/2017
'''

def isDeclaration(line):
	result = True ; 
	result = result and isArrayName(line[0]) ; 
	result = result and line[1] == "[" and line[-1] == "]" ; 
	result = result and isNumber(line[2:-1]) ; 
	return result ;

def isAssignment(line):
	result = True ; 
	if "=" not in line:
		return False ; 
	first, second = line.split("=") ; 
	result = result and isArrayExpression(first) ; 
	result = result and isExpression(second) ; 
	return result; 
def isDigitPositive(n):
	return n in [str(s) for s in range(1, 10)] ; 
def isDigit(n):
	return n == "0" or isDigitPositive(n) ; 
def isDigitString(n):
	return isDigit(n) or (isDigit(n[0]) and isDigitString(n[1:])) ; 
def isNumber(n):
	return isDigit(n) or (isDigitPositive(n[0]) and isDigitString(n[1:])) ; 
def isArrayName(n):
	return n.isalpha() ;
def isExpression(exp):
	if isNumber(exp):
		return True ; 
	if len(exp) < 4:
		return False ; 
	return \
	   (isArrayName(exp[0]) and exp[1]=="[" and exp[-1]=="]" and 
		isExpression(exp[2:-1])) ; 

def isArrayExpression(exp):
	if len(exp) < 4: 
		return False ; 
	return isArrayName(exp[0]) and exp[1]=="[" and exp[-1] == "]" and isExpression(exp[2:-1]) ; 

# TEST FUNCTIONS
def testIsArrayName():
	for i in range(ord('A'), ord('z')+1):
		print(chr(i) + " " + str(isArrayName(chr(i)))) ; 
	return ; 

def testIsNumber():
	print("028" + " " + str(isNumber("028"))) ; 
	print("0" + " " + str(isNumber("0"))) ; 
	print("2348984a" + " " + str(isNumber("2348984a"))) ; 
	a = "1234567890" ; 
	print(a + " " + str(isNumber(a))) ; 
	a = "101" ; 
	print(a + " " + str(isDigitString(a))) ; 
	return ; 

def testIsExpression():
	print("Test Expression:-->"); 
	a = "12" ; 
	print(a + " " + str(isExpression(a))) ; 
	a = "012" ; 
	print(a + " " + str(isExpression(a))) ; 
	a = "x[12]"; 
	print(a + " " + str(isExpression(a))) ; 
	a = "a[x[3]]" ; 
	print(a + " " + str(isExpression(a))) ; 
	a = "a[b[a]]" ; 
	print(a + " " + str(isExpression(a))) ; 
	a = "a[b[ax[8]]]" ; 
	print(a + " " + str(isExpression(a))) ; 
	a = "a[b[a[z[Z[20]]]]]" ; 
	print(a + " " + str(isExpression(a))) ; 
	a = "a[[a[z[Z[20]]]]]" ; 
	print(a + " " + str(isExpression(a))) ; 
	return ; 

def testIsAssignment():
	print("TEST ASSIGNMENT -->") ;
	a = "a[10]" ;
	print(a + " --> " + str(isAssignment(a))) ; 
	a = "10" ;
	print(a + " --> " + str(isAssignment(a))) ; 
	a = "a[10]=10" ;
	print(a + " --> " + str(isAssignment(a))) ; 
	a = "a[10]=b[z[0]]" ;
	print(a + " --> " + str(isAssignment(a))) ; 
	a = "a[]=20" ;
	print(a + " --> " + str(isAssignment(a))) ; 
	a = "a=100" ;
	print(a + " --> " + str(isAssignment(a))) ; 
	a = "a[n[b[0]]]=20" ;
	print(a + " --> " + str(isAssignment(a))) ; 
	a = "a[n[z[B[T[235]]]]]=h[c[e[d[h[R[R[E[e[T[0]]]]]]]]]]" ;
	print(a + " --> " + str(isAssignment(a))) ; 
	a = "a[n]=020" ;
	print(a + " --> " + str(isAssignment(a))) ; 
	return ; 

def testIsDeclaration():
	print("TEST DECLARATION -->") ; 
	a = "a[10]" ; 
	print(a + " --> " + str(isDeclaration(a))) ; 
	a = "a10]" ; 
	print(a + " --> " + str(isDeclaration(a))) ; 
	a = "a10" ; 
	print(a + " --> " + str(isDeclaration(a))) ; 
	a = "a[03]" ; 
	print(a + " --> " + str(isDeclaration(a))) ; 
	a = "a[[30]]" ; 
	print(a + " --> " + str(isDeclaration(a))) ; 
	a = "a[3]" ; 
	print(a + " --> " + str(isDeclaration(a))) ; 
	a = "$[40]" ; 
	print(a + " --> " + str(isDeclaration(a))) ; 

	return ; 

def test():
	# testIsDeclaration() ; 
	# testIsArrayName() ; 
	# testIsNumber() ; 
	# testIsExpression() ; 
	# testIsAssignment() ; 
	return ; 
# END OF TEST FUNCTIONS

def process_declaration(decl, line):
	name = line[0] ; 
	num = line[2:-1] ; 
	if not isArrayName(name) or not isNumber(num):
		return False ; 
	decl[name] = int(num) ; 
	return True ; 

def evaluate(decl, values, exp): # return (boolHasNoError, value) 
	if isNumber(exp):
		return (True, int(exp)) ; 
	elif isExpression(exp):
		name = exp[0] ; 
		isValid, offset = evaluate(decl, values, exp[2:-1]) ; 
		if not isValid:
			return (False, -1) ; 
		'''
		if name not in decl or offset >= decl[name]:
			return (False, 0) ; 
		if (name+str(offset)) not in values:
			return (False, 0) ; 
		'''
		if not isAssigned(name, offset, decl, values):
			return (False, -1) ; 
		return (True, values[name+str(offset)]) ; 
	else:
		return (False, -1) ; 

def isDeclared(name, offset, decl, values):
	return name in decl and offset < decl[name] ;

def isAssigned(name, offset, decl, values):
	return isDeclared(name, offset, decl, values) and \
		   name+str(offset) in values ; 

def process_assignment(decl, values, line): # return boolIsValidInstruction
	first, second = line.split("=") ; 
	name = line[0] ; 
	isValid, offset = evaluate(decl, values, first[2:-1]) ; 
	if not isValid: 
		return False ; 

	isValid, assignValue = evaluate(decl, values, second) ; 
	if not isValid:
		return False ; 
	if not isDeclared(name, offset, decl, values):
		return False ; 
	values[name+str(offset)] = assignValue ; 
	return True ; 

def execute_step(decl, values, line):
	if isDeclaration(line):
		return process_declaration(decl, line) ;
	elif isAssignment(line):
		return process_assignment(decl, values, line) ;
	else:
		return False; 

def execute_program():
	line = input().strip() ; 
	if line == ".":
		return 1 ; 
	decl = dict() ; # array-name -> array-size
	values = dict() ; # array-name+offset -> value
	cur = 1 ;
	hasError = False ; 
	while line != "." and not hasError:
		
		if not execute_step(decl, values, line):
			hasError = True ; 
		else:
			line = input() ;
			cur += 1 ;
	if line == "." and not hasError:
		print(0) ; 
	elif hasError:
		print(cur) ; 
		while line != ".":
			line = input() ; 
	return 0 ; 

def main():
	T = 0 ; 
	while execute_program() == 0:
		T += 1 ; 
	# test() ; 
	return ; 

if __name__ == "__main__":
	main() ; 
