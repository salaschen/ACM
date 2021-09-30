'''
Note:
    1) TLE on about length of 10 expression.
    2) Try to do a intuitive recursion version.
'''
class Solution:
    def __init__(self):
        self.memory = dict() ;
        return ;

    def scoreOfStudents(self, s: str, answers: [int]) -> int:
        correct = self.correctEval(s) ;
        all = self.allEval(s) ; 
        result = 0 ; 
        for ans in answers:
            if ans in correct:
                result += 5 ; 
            elif ans in all:
                result += 2 ; 
        return result ;    

    # takes the expression and gives out the correct 
    # evaluation.
    def correctEval(self, expression: str) -> int:
        if expression.isnumeric():
            return int(expression) ; 

        pos = expression.find("*") ; 
        while pos != -1:
            temp = expression[:pos] + str(int(expression[pos-1]*int(expression[pos+1]))) + expression[pos+1:] ;
            expression = temp ; 
            pos = expression.find("*") ; 
        
        pos = expression.find("+") ; 
        while pos != -1:
            temp = expression[:pos] + str(int(expression[pos-1]+int(expression[pos+1]))) + expression[pos+1:] ;
            expression = temp ; 
            pos = expression.find("+") ; 
        
        return int(expression) ; 

   # merge two set of possible answers.
    def operateOnSet(self, set1, set2, op) -> set:
        result = set() ; 
        for operand1 in set1:
            for operand2 in set2:
                result.add(op(operand1, operand2)) ;
        return result ;
  
    # old
    def evalOneOp(self, expression: str, opStr: str, op, pos:int) -> str:
        if pos == -1:
            return expression ; 

        frontEndPos = pos - 1 ; 
        num1 = "" ;
        for i in range(pos-1, -1, -1):
            if expression[i].isnumeric():
                num1 = expression[i] + num1 ; 
                frontEndPos = i - 1 ;
            else:
                break ;
        lastStartPos = pos+1 ; 
        num2 = "" ; 
        for i in range(pos+1, len(expression)):
            if expression[i].isnumeric():
                num2 += expression[i] ; 
                lastStartPos = i + 1 ; 
            else:
                break ; 
        mid = op(int(num1), int(num2)) ; 
        newExpression = expression[0:frontEndPos+1] + str(mid) + expression[lastStartPos:] ;
        return newExpression ;
    # old
    def findAllOpInExp(self, expression: str, op: str) -> [int]:
        if expression.find(op) == -1:
            return [] ; 
        else:
            result = [] ; 
            for i in range(len(expression)):
                if expression[i] == op:
                    result.append(i) ;
            return result ;

    # evaluate the expression in all possibilities
    # old
    def allEval(self, expression: str) -> set:
        if expression in self.memory:
            return self.memory[expression] ; 
        
        # when there's no mix operations, only correct evaluation is 
        # possible.
        if expression.find("*") == -1 or expression.find("+") == -1:
            result = self.correctEval(expression) ;
            self.memory[expression] = result ; 
            return result ; 
            
        else:
            # when * presents, to do it improperly, we just 
            # randomly select an op and do that.
            allPlusPos = self.findAllOpInExp(expression,"+") ; 
            allMulPos = self.findAllOpInExp(expression, "*") ;
            allExpressions = list(map(
                lambda pos: self.evalOneOp(expression, "+", lambda a,b: a+b, pos),
                allPlusPos)) ;
            allExpressions += list(map(
                lambda pos: self.evalOneOp(expression, "*", lambda a,b: a*b, pos),
                allMulPos)) ;
            result = set() ; 
            for exp in allExpressions:
                result = result.union(self.allEval(exp)) ; 

            # do it properly
            result = result.union(self.correctEval(expression)) ;   
            self.memory[expression] = result ; 
            return result ; 

    # evaluate the expression correctly
    # old
    def correctEvalOld(self, expression: str) -> set:
        # if there exists *, do it first.
        pos = expression.find("*") ; 
        # print("evaluating: {0}".format(expression)) ; # debug
        if pos != -1:
            num1 = "" ;
            # the end index of the expression that doesn't include 
            # the operand for the multiplication.
            # e.x, 1+2*3, frontEndPos = 1 ("+").
            # if frontEndPos == -1, then it means we don't have front
            # expression.
            frontEndPos = pos-1 ; 
            for i in range(pos-1, -1, -1):
                if expression[i].isnumeric():
                    num1 = expression[i] + num1 ;
                    frontEndPos = i-1 ; 
                else:
                    break ;
            num2 = "" ;
            lastStartPos = pos+1 ; 
            for i in range(pos+1, len(expression)):
                if expression[i].isnumeric():
                    num2 += expression[i] ; 
                    lastStartPos = i + 1 ; 
                else:
                    break ;
            mulResult = int(num1) * int(num2) ; 
            newExpression = str(mulResult) ;
            if frontEndPos != -1:
                newExpression = expression[0:frontEndPos+1] + newExpression ;
            if lastStartPos != len(expression):
                newExpression = newExpression + expression[lastStartPos:] ;
            return self.correctEval(newExpression) ; 
        # no multiplication, but addition is present.
        elif expression.find("+") != -1:
            result = sum([int(n) for n in expression.split("+")]) ; 
            return set([result]) ; 
        # no operation, expression is just a pure number.
        else:
            try:
                return set([int(expression)]) ; 
            except:
                print("expression: {0} is not in correct form") ; 
                return -1 ; 
        return None ;

   


##### test #####
s = Solution() ; 
expList = [
            ("7+3*1*2", [20,13,42]),
            ("49", []), 
            ("1+2", [3,4]), 
            ("3*4", [12,7]),
            ("3+5*2", [13,0,10,13,13,16,16]),
            ("6+0*1", [12,9,6,4,8,6]),
            ("1+2*3+4",[13,21,11,15]),
            ("4+2*2+3*1+2", []),
            ] ; 
for exp,answers in expList:
    print("{0} evaluating all: {1}".format(exp, s.allEval(exp))) ; 

'''
for exp, answers in expList:
    print('scores:', exp, s.scoreOfStudents(exp, answers)) ;

'''

