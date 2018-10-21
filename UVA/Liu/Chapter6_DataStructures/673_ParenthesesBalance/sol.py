def work():
    line = input() ;
    stack = [] ;
    for c in line:
        if c == '(' or c == '[':
            stack.append(c) ; 
        else:
            if len(stack) == 0:
                return 'No' ;
            last = stack.pop(); 
            if c == ')' and last != '(':
                return 'No' ; 
            if c == ']' and last != '[':
                return 'No' ;
    if len(stack) > 0:
        return 'No' ; 
    return 'Yes' ;

def main():
    num = int(input()) ; 
    for i in range(0, num):
        print(work()) ; 

if __name__ == "__main__":
    main() ; 
