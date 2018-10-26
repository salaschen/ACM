class Node:
    def __init__(self, string, level, valueDict):
        self.type = 'leaf' if '[' not in string else 'branch' ; 
        self.value = int(string) if self.type == 'leaf' else None ; 
        self.level = level ; 
        if self.type == 'branch':
            # lstr, rstr = string.strip('[]').split(',') ;
            string = string[1:-1] ; 
            # read the first comma that's not enclosed within
            # a bracket.
            balance = 0 ; 
            divPos = -1 ; 
            for i in range(0, len(string)):
                if string[i] == '[':
                    balance += 1 ; 
                elif string[i] == ']':
                    balance -= 1 ; 
                elif string[i] == ',':
                    if balance == 0:
                        divPos = i ;  
            lstr = string[:divPos] ; 
            rstr = string[divPos+1:] ;

            self.left = Node(lstr,level+1, valueDict) ; 
            self.right = Node(rstr, level+1, valueDict) ; 
        else:
            self.left, self.right = None, None ; 
            sumValue = (2 ** self.level) * self.value ; 
            if sumValue in valueDict:
                valueDict[sumValue] += 1 ; 
            else:
                valueDict[sumValue] = 1 ; 

        return ; 

    def __str__(self):
        result = self.type + ", level:{0} => ".format(self.level) ;
        if self.type == 'leaf':
            result += ' ' + str(self.value)  ; 
        else:
            result += ' left:{0}, right:{1}'\
                    .format(self.left.Dry(), self.right.Dry()) ;
        return result ; 

    def Dry(self):
        if self.type == 'leaf':
            return str(self.value) ; 
        else:
            return "[{0},{1}]".format(self.left.Dry(), self.right.Dry()) ; 

def printTree(root):
    if root.type == 'leaf':
        print(root) ; 
    else:
        printTree(root.left); 
        printTree(root.right) ; 
        print(root) ; 

def work():
    string = input() ; 
    valueDict = dict() ; 
    # root = Node(string, 0, valueDict) ; 
    # printTree(root) ; # debug
    stack = [] ; 
    i = 0 ; 
    while i < len(string):
        if string[i] == '[':
            stack.append('[');  
            i = i + 1 ; 
        elif string[i] == ']':
            stack.pop() ; 
            i = i + 1 ;
        elif string[i].isdigit():
            num = string[i] ; 
            i = i + 1 ; 
            while i < len(string) and string[i].isdigit():
                num += string[i] ; 
                i = i + 1 ; 
            num = int(num) ; 
            num = (2 ** len(stack)) * num ; 
            if num in valueDict:
                valueDict[num] += 1 ; 
            else:
                valueDict[num] = 1 ; 

        else: # string[i] == ','
            i = i + 1 ; 

    count, maxCount = 0, 0 ; 
    for k in valueDict.keys():
        cur = valueDict[k] ;
        count += cur; 
        if cur > maxCount:
            maxCount = cur ; 
    print(count-maxCount) ; 
    return ; 

def CountValues(Node, valueDict):
    if Node.type == 'leaf':
        sumValue = (2 ** Node.level) * Node.value ; 
        if sumValue in valueDict:
            valueDict[sumValue] += 1 ; 
        else:
            valueDict[sumValue] = 1 ; 
    else:
        CountValues(Node.left, valueDict) ; 
        CountValues(Node.right, valueDict) ; 

    return ;

def main():
    num = int(input()) ; 
    for i in range(num):
        work() ; 


if __name__ == "__main__":
    main() ; 

