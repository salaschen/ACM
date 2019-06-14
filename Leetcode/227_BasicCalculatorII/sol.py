import random ; 

class Solution:
    def calculate(self, s):
        numStack = [] ; 
        opStack = [] ; 
        
        num, index = self.readNum(s, 0) ; 
        numStack.append(num) ; 
        operate = False ; 
        highOp = dict(); 
        highOp['*'] = lambda n1,n2: n1*n2 ; 
        highOp['/'] = lambda n1,n2: n1//n2 ;
        lowOp = dict() ; 
        lowOp['+'] = lambda n1,n2: n1+n2 ;
        lowOp['-'] = lambda n1,n2: n1-n2 ;
        while index < len(s):
            op, index = self.readOp(s, index) ; 
            if op is None or index is None:
                break ;
            else:
                opStack.append(op) ;

            if op in highOp.keys():
                operate = True ; 

            num, index = self.readNum(s, index) ; 
            if operate:
                op = opStack.pop(-1) ;
                num0 = numStack.pop(-1) ;
                num1 = highOp[op](num0, num) ; 
                numStack.append(num1) ; 
                operate = False ; 
            else:
                numStack.append(num) ; 
                
        # now deal with all the remaining lower priority operations.
        while len(opStack) > 0 and len(numStack) >= 2:
            num1 = numStack.pop(0) ; 
            num2 = numStack.pop(0) ; 
            op = opStack.pop(0) ; 
            num = lowOp[op](num1, num2) ; 
            numStack.insert(0, num) ; 

        return numStack[0] ; 
    
    def readNum(self, s, startIndex):
        # return (number, nextStartIndex)
        # guard against the overflow.
        if startIndex >= len(s):
            return (None, None) ; 

        i = startIndex ; 
        # skip spaces
        while s[i] == ' ': i += 1 ;
        # read the number
        number = ''; 
        while i < len(s) and s[i].isdigit() :
            number += s[i] ; 
            i += 1 ; 
        return (int(number), i) ; 

    def readOp(self, s, startIndex):
        # return (op -> str, nextStartIndex) ;
        if startIndex >= len(s):
            return (None, None) ; 
        
        i = startIndex ; 
        # skip spaces
        while i < len(s) and s[i] == ' ': i += 1 ; 
        if i >= len(s): return (None, None) ; 
        else: return (s[i], i+1) ; 


# test
def test():
    s = Solution() ; 
    exps = [("3+2*2", 7), (" 3/2 ", 1), ( "3+5 / 2 ", 5)] ;
    for expr, expected in exps:
        print('expected:{0}, result:{1}'.format(expected, s.calculate(expr))) ; 
    return ;

def genCase(length = 100):
    expr = '' ;
    expr += ' ' * (random.randint(0, 2)) ; 
    low, high = 1, 999 ; 
    expr += str(random.randint(low, high)) ; 
    ops = ['+', '//', '*', '-'] ;
    l = 1 ; 
    while l < length:
        expr += ' ' * (random.randint(0, 2)) ; 
        expr += random.choice(ops) ; 
        expr += str(random.randint(low, high)) ; 
        l += 1 ; 
    return expr ; 

def randomTest():
    random.seed(0) ; 
    times = 100 ; 
    expr = genCase(10) ; 
    s = Solution() ; 
    cases = [] ;
    for i in range(0, times):
        cases.append(genCase(10)) ; 
    
    for case in cases:
        expected = eval(case) ; 
        calculated = s.calculate(case.replace('//', '/')) ; 
        if expected != calculated:
            print('failed: {0}, \nexpected={1},calculated={2}'.format(case, expected,\
                    calculated)) ; 
        else:
            print('pass: {0}, \nexpected={1},calculated={2}'.format(case, expected,\
                    calculated)) ; 

    return ;

def main():
    # test() ;
    randomTest() ; 

if __name__ == '__main__':
    main() ; 
