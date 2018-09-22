import random ;
import time ; 
import itertools ; 

class Solution:
    def totalFruit(self, tree):
        blocks = [(k, len(list(v))) for k,v in itertools.groupby(tree)]

        fruits = [] ; 
        result = 0 ; 
        types = set() ; 
        for i in range(0, len(blocks)):
            cur_type = blocks[i][0] ; 
            if len(types) == 2 and cur_type not in types:
                result = max(result, sum(list(map(lambda f: f[1], fruits)))) ; 
                types = set() ; 
                prev = fruits.pop() ; 
                fruits = [prev] ; 
                types.add(prev[0]) ; 
            types.add(cur_type) ; 
            fruits.append(blocks[i]) ; 
            
        result = max(result, sum(list(map(lambda f: f[1], fruits)))) ; 
        return result ; 

    def totalFruit0(self, tree):
        '''
        Note: A generic way by implementing a Basket class.
        '''
        # print("tree:", tree) ; 
        b = Basket(2) ;
        for i in range(0, len(tree)):
            b.TryPickFruit(tree[i]) ; 

        if b.Max < b.TotalCount():
                    b.BestPick = b.Fruits[:] ; 
        b.Max = max(b.Max, b.TotalCount()) ; 
    
        print("Best pick:", b.BestPick) ; # debug
        return b.Max ; 

class Basket:
    def __init__(self, typeLimit):
        if typeLimit < 1:
            typeLimit = 1 ; 
        self.typeLimit = typeLimit ; 
        self.numType = 0 ; 
        self.types = dict() ; # maps the type to the amount of fruit.
        self.Fruits = [] ; # each item is (int) => (type)
        self.BestPick = [] ; 
        self.Max = 0 ; 
    
    def GetNumType(self):
        return sum(list(map(lambda k: 1 if self.types[k] > 0 else 0, self.types))) ; 

    def TotalCount(self):
        return len(self.Fruits) ;

    def HasType(self, Type):
        return Type in self.types ;
    
    def DiscardFruit(self): # keep discarding unless completely get rid of one type
        while True:
            head = self.Fruits.pop(0) ; 
            self.types[head] -= 1 ; 
            if self.types[head] == 0:
                return ;

    def TryPickFruit(self, FruitType) :
        if FruitType in self.Fruits:
            self.types[FruitType] += 1 ; 
            self.Fruits.append(FruitType) ;
        else:
            if self.GetNumType() == self.typeLimit:
                if self.Max < self.TotalCount():
                    self.BestPick = self.Fruits[:] ; 
                self.Max = max(self.TotalCount(), self.Max) ; 
                self.DiscardFruit() ;
            self.types[FruitType] = 1 ;
            self.Fruits.append(FruitType) ; 

        return ; 

if __name__ == "__main__":
    s = Solution() ;

    tree = [3,3,3,1,2,1,1,2,3,3,4] ;
    print(s.totalFruit0(tree)) ; 
    print(s.totalFruit(tree)) ; 

    tree = [1,2,1]
    print(s.totalFruit0(tree)) ; 
    print(s.totalFruit(tree)) ; 
    
    tree = [0,1,2,2]
    print(s.totalFruit0(tree)) ; 
    print(s.totalFruit(tree)) ; 
    
    tree = [1,2,3,2,2]
    print(s.totalFruit0(tree)) ; 
    print(s.totalFruit(tree)) ; 
   
    tree = [4,4,4,4,4]
    print(s.totalFruit0(tree)) ; 

    print(s.totalFruit(tree)) ; 
     
    tree = [0,1,0,1,4,1,4,1,4,0]
    print(s.totalFruit0(tree)) ; 

    print(s.totalFruit(tree)) ; 

    tree = [1,0,1,4,1,4,1,2,3]
    print(s.totalFruit0(tree)) ; 

    print(s.totalFruit(tree)) ; 
             
    random.seed(0) ; 
    tree = [] ;
    for i in range(0, 40000):
        tree.append(random.randint(0, 10)) ;
    start = time.time() ; 
    print("large result = ", s.totalFruit(tree)) ; 
    end = time.time() ; 
    print("execution time: {0} milliseconds".format((end-start)*1000)) ; 
    print(s.totalFruit0(tree)) ; 

