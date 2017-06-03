class Set:
    def __init__(self):
        self.depth = 1 ; 
        self.sets = [] ;

    def __str__(self):
#        result = 'Card=' + str(self.cardinality())  ;
#        result += ', Depth=' + str(self.depth) ; 
        result = '(' ; 

        for s in self.sets:
            result += s.__str__()  + ',' ; 
        result = result.rstrip(',') ; 
        result += ')' ; 
        return result ; 

    def cardinality(self):
        return len(self.sets) ; 

    def depth(self):
        return self.depth ; 
        
    def Add(self, s2):
        self.sets.append(s2) ; 
        if s2.depth >= self.depth:
            self.depth = s2.depth + 1 ; 
#        self.sets = sorted(self.sets, key=lambda s: s.depth) ; 
        return self; 
    
    def isSame(self, s2):
        if self.cardinality() != s2.cardinality():
            return False ; 
        if self.depth == 1 and s2.depth == 1:
            return True ; 
        # Test Every 
        
        inter = self.intersect(s2) ; 
        if len(inter.sets) != len(self.sets):
            return False;
        # return self.isSameList(self.sets, s2.sets) 
        return True ; 

    def isSameList(l1, l2):
        while len(l1) > 0:
            s1 = l1.pop(0) ; 
            found = False ; 
            for i in range(0, len(l2)):
                s2 = l2[i] ; 
                if s1.depth < s2.depth:
                    return False ; 
                if s1.isSame(s2):
                    l2.pop[i] ; 
                    found = True ; 
                    break ; 
            if found == False:
                return False ; 
        return True ; 

    def minus(self, subset):
        result = Set() ; 
        selfCopy = Set() ; selfCopy.copy(self) ; 
        subCopy = Set() ; subCopy.copy(subset) ; 
        while len(subCopy.sets) > 0:
            s1 = subCopy.sets.pop() ; 
            for i in range (0, len(selfCopy.sets)):
                if s1.isSame(selfCopy.sets[i]):
                    selfCopy.sets.pop(i) ; 
                    break ; 
        for x in selfCopy.sets:
            result.Add(x) ; 
        return result ; 

    # return the list of intersection sets.
    def intersect(self, s2):
        s1Copy = Set() ; s1Copy.copy(self) ; 
        s2Copy = Set() ; s2Copy.copy(s2) ; 

        result = Set() ; 
        x = 0 ; 
        while len(s1Copy.sets) > 0:
            s = s1Copy.sets.pop() ;
            for i in range(0, len(s2Copy.sets)):
                ss = s2Copy.sets[i] ; 
                if s.isSame(ss) == True:
                    result.Add(s) ; 
                    s2Copy.sets.pop(i) ; 
                    break ; 
        return result ;   

    def union(self, s2):
        inter = self.intersect(s2) ; 
        for x in (s2.minus(inter)).sets:
            self.Add(x) ; 
        return self ; 

    def copy(self, s):
        self.depth = s.depth ; 
        for i in s.sets:
            self.Add(i) ; 

    def hasSet(self, s):
        for ss in self.sets:
            if ss.isSame(s):
                return True ; 
        return False ; 

def work():
    stack = []
    num = int(input()) ; 
    for i in range(0, num):
        com = input() ; 
        if com == 'PUSH':
            stack.append(Set()) ; 
        if com == 'DUP':
            top = stack.pop() ; 
            dup = Set() ; 
            dup.copy(top) ; 
            stack.append(top) ; 
            stack.append(dup) ; 
        if com == 'UNION':
            s1 = stack.pop() ; 
            s2 = stack.pop() ; 
            s1.union(s2) ; 
            stack.append(s1) ; 
        if com == 'INTERSECT':
            s1 = stack.pop() ; 
            s2 = stack.pop() ; 
            stack.append(s1.intersect(s2)) ; 
        if com == 'ADD':
            s1 = stack.pop() ; 
            s2 = stack.pop() ; 
            if s2.hasSet(s1) == False:
                s2.Add(s1) ; 
            stack.append(s2) ; 
        
        result = "" ; 
#        result = result + "[" + com + "] " ; # debug
#        result = result + str(stack[len(stack)-1]) + " - "  ; # debug
        result = result + str(stack[len(stack)-1].cardinality()) ; 
        print(result) ; 
        
    print("***") ; 
    return ; 

def test():
    s1 = Set() ;
    s2 = Set() ; 
    s1.Add(Set()) ; # (())
    s2.Add(Set()) ; # (())
    s1.Add(Set()) ; # ((), ())
    s2.Add(Set()) ; # ((), ()) 

    s3 = Set(); 
    s3.Add(Set()) ; # (())
    s4 = Set() ; 
    s4.Add(s3) ; # ((()))
    print (s4.hasSet(Set())) ; 
    s5 = Set() ; 
    s5.Add(s3) ; 
    s5.Add(s4) ; 
    print(s5) ;
    print(s5.hasSet(Set())) ; 
    print(s3.isSame(Set())) ; 
    print(s4.isSame(Set())) ; 
    print(s4) ; 
    print(s4.cardinality()) ; 
    print(Set().cardinality()) ; 
    print(s4.depth) ; 
    print('***') ; 

    print(s1) ; 
    print(s2) ; 
    print(s1.isSame(s2)) ; 
    print(s1.intersect(s2)) ; 
    print(s4) ; 
    print(s4.union(s2)) ; 
    print(s4.union(s3)) ; 
    print(s4.union(s1)) ; 
    print(s4.Add(s2)) ; 
    

def main():
    # debug
#    test() ; 
    x = 0 ;
    T = int(input()) ; 
    for i in range(0, T):
#        x += 1;
        work() ; 
    return  ;

if __name__ == "__main__":
    main() ; 
