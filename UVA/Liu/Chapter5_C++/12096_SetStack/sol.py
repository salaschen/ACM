'''
update: 
    04/June/2017: Try to use id to identify set.
    Store id in self.sets instead of an actual set object.
'''
Set2IdMap = {} ; 

class Set:
    def __init__(self):
        self.sets = [] ;
        self.id = -1 ; 
        key = self.__str__() ; 
        if key in Set2IdMap:
            self.id = Set2IdMap[key] ; 
        else:
            self.id = len(Set2IdMap) ; 
            Set2IdMap[key] = self.id ; 

    def updateId(self):
        self.sets = sorted(self.sets) ;
        key = self.__str__() ; 
        if key in Set2IdMap:
            self.id = Set2IdMap[key] ; 
        else:
            self.id = len(Set2IdMap) ; 
            Set2IdMap[key] = self.id ; 

    def __str__(self):
        result = '(' ; 
        for index in self.sets:
            result += (str(index) + ",")
        result = result.rstrip(',') ; 
        result += ')' ; 
        return result ; 

    def cardinality(self):
        return len(self.sets) ; 

    def Add(self, s2Id):
        self.sets.append(s2Id) ; 
        return self; 
    
    def isSame(self, s2):
        '''
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
        '''
        return self.id == s2.id ; 
    
    # return the list of intersection sets.
    def intersect(self, s2):
        s2Copy = Set() ; s2Copy.copy(s2) ; 
        s2Copy.sets = sorted(s2Copy.sets) ; 

        inter = Set() ; 
        minus = Set() ; 
        x = 0 ; 
        while len(s2Copy.sets) > 0:
            s = s2Copy.sets.pop(0) ;
            if self.hasSet(s):
                inter.Add(s) ; 
            else:
                minus.Add(s) ; 

        minus.updateId() ; 
        return (inter, minus) ; 

    def union(self, s2):
        inter, minus = self.intersect(s2) ; 
        for x in minus.sets:
            self.Add(x) ; 
        return self ; 

    # copy from another set s
    def copy(self, s):
        self.id = s.id ; 
        for i in s.sets:
            self.Add(i) ; 

    def hasSet(self, sId):
        return sId in self.sets ; 

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
            s1.updateId() ; 
            stack.append(s1) ; 
        if com == 'INTERSECT':
            s1 = stack.pop() ; 
            s2 = stack.pop() ; 
            result = s1.intersect(s2)[0] ; 
            result.updateId() ; 
            stack.append(result) ; 
        if com == 'ADD':
            s1 = stack.pop() ; 
            s2 = stack.pop() ; 
            if s2.hasSet(s1.id) == False:
                s2.Add(s1.id) ; 
            s2.updateId() ; 
            stack.append(s2) ; 
        
        result = "" ; 
#        result = result + "[" + com + "] " ; # debug
#        result = result + str(stack[len(stack)-1]) + " - "  ; # debug
        result = result + str(stack[len(stack)-1].cardinality()) ; 
        print(result) ; 
        
#    print(Set2IdMap) ; # debug
    print("***") ; 
    return ; 

def test():
    s1 = Set() ;
    s2 = Set() ; 
    s1.Add(Set()) ; # (())
    s2.Add(Set()) ; # (())
    s1.Add(Set()) ; # ((), ())
    s1.updateId() ;
    s2.Add(Set()) ; # ((), ()) 
    s2.updateId() ; 

    s3 = Set(); 
    s3.Add(Set()) ; # (())
    s3.updateId() ; 
    s4 = Set() ; 
    s4.Add(s3) ; # ((()))
    s4.updateId() ;
    
    print (s4.hasSet(Set())) ; 
    s5 = Set() ;  # ()
    s5.Add(s3) ;  # ((()))
    s5.Add(s4) ;  # ((()), ((()))) 

    print(s5) ;
    print(s5.hasSet(Set())) ; 
    print(s3.isSame(Set())) ; 
    print(s4.isSame(Set())) ; 
    print(s4) ; 
    print('***') ; 

    print(s1) ; 
    print(s2) ; 
    print(s1.isSame(s2)) ; 
    print(s1.intersect(s2)[0]) ; 
    print(s1.intersect(s2)[1]) ; 
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
        x += 1;
        work() ; 
    return  ;

if __name__ == "__main__":
    main() ; 
