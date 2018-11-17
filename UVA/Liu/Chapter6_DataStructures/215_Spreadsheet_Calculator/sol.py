'''
UVa 215 - Spreadsheet Calculator
Date: 14/Nov/2018 
'''
def work(row, col):
    oldExp = dict() ;
    for i in range(row):
        for j in range(col):
            expr = input().strip() ; 
            oldExp[translate(i,j)] = expr ; 

    # split the expression
    newExp = dict() ; 
    for k in oldExp:
        exp = oldExp[k] ; 
        newExp[k] = splitExp(exp) ;
    # print(newExp) ; # debug

    # keep goin through until no more can evaluate
    resolved, values = GoThrough(newExp) ; 

    # print out the result 
    if resolved:
        allKeys = (sorted(values.keys())) ;
        # print the col heading
        line = ' ' ; 
        for i in range(col):
            line += ' ' * 5 + str(i) ;
        print(line) ; 
        # print all the results.
        for i in range(row):
            line = allKeys[i*col][0] ;
            for j in range(col):
                curIndex = i * col + j ; 
                curKey = allKeys[curIndex] ; 
                line += "{0:>6}".format(values[curKey]) ; 
            print(line) ; 
    
    else:
        allKeys = sorted(list(values)) ;
        for key in allKeys:
            print("{0}: {1}".format(key,oldExp[key])) ; 

    print() ; # a blank line after each spreadsheet output.
    return ; 

def EvaluateCell(cell, Evaluated): 
    '''
    Cell is of format [tuple(op, val)] ; 
    Return an tuple integer if this cell can be resolved, 
    otherwise return original cell.
    '''
    result = 0 ; 
    for op, val in cell:
        if type(val) == int: 
            op = (lambda Op: 1 if Op == '+' else -1)(op);
            result = result +  op * val ;
        elif val in Evaluated:
            op = (lambda Op: 1 if Op == '+' else -1)(op);
            result = result +  op * Evaluated[val] ;
        else:
            return cell ; 
            
    return result ; 

# Go through each of the cell and try to evaluate
# return True if at least one cell has been evaluated
def GoThrough(newExp):
    queue = [] ;
    callBack = dict() ; # id = > set(id) ;

    # initialize the call back map
    for k in newExp.keys():
        callBack[k] = set() ; 
    
    # create the call back map
    for k in newExp.keys():
        lst = newExp[k] ;
        for op, val in lst:
            val = str(val) ;
            if not val.isnumeric() and val.isalnum() and val in callBack:
                callBack[val].add(k) ; 

    # print('Callback:', callBack) ; # debug

    # go through each cell to try to evaluate
    Evaluated = dict() ; # id => int
    allCells = set(newExp.keys()) ; 

    for k in newExp.keys():
        value = EvaluateCell(newExp[k], Evaluated) ; 
        if type(value) == int:
            # if the cell can be evaluted, add the value to the Evaluated map.
            # update the call back queue. 
            Evaluated[k] = value ; 
            allCells.remove(k) ; 
            for cell in callBack[k]:
                if cell not in Evaluated and cell not in queue:
                   queue.append(cell) ; 


    while len(queue) > 0:
        cur = queue.pop() ; 
        value = EvaluateCell(newExp[cur], Evaluated) ; 
        if type(value) == int:
            # if the cell can be evaluted, add the value to the Evaluated map.
            # update the call back queue. 
            Evaluated[cur] = value ; 
            if cur in allCells:
                allCells.remove(cur) ; 
            for cell in callBack[cur]:
                if cell not in Evaluated and cell not in queue:
                   queue.append(cell) ; 
    
    if len(allCells) == 0:
        return (True, Evaluated) ;
    else:
        return (False, allCells) ;

    return ; 
    
def splitExp(exp):
    # return a list of simple expressions.
    if exp == "":
        return [] ; 
    elif exp.isnumeric():
        num = int(exp) ; 
        if num < 0:
            return [('-', abs(num))] ; 
        else:
            return [('+', num)] ;
    else:
        first, restIndex = FirstExp(exp) ;
        return [first] + splitExp(exp[restIndex:]) ;

def FirstExp(exp):
    if exp == "":
        return "" ; 
    else:
        sym = "" ; 
        cur = 0 ; 
        if exp[0] == "-":
            sym = "-" ; 
            cur += 1 ;
        elif exp[0] == "+":
            sym = "+" ; 
            cur += 1 ; 
        else:
            sym = "+" ; 

        if exp[cur].isalpha(): # It's an expression.
            return ((sym, exp[cur:cur+2]), cur+2) ; 
        else: # It's a number
            st = cur ; 
            while cur < len(exp) and exp[cur].isnumeric():
                cur += 1 ; 
            return ((sym, int(exp[st:cur])), cur) ;



def translate(r, c):
    # both r and c begins with 0.
    rsym = chr(r + ord('A')) ;
    return rsym+str(c) ;

def main():
    while True:
        row, col = [int(n) for n in input().split()] ;
        if row == 0 and col == 0:
            break ; 
        else:
            work(row, col) ;
    return ;

if __name__ == "__main__":
    main() ; 
