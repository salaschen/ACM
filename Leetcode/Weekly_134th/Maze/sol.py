'''
Date: 02/May/2019
Learn from someone else's solution.
Learned a few things:
    1) this is an interesting algorithm to test whether a collections of points is enough
    to block a region.
    2) a little more understanding of bfs
'''

class Solution:
    
    def isEscapePossible(self, blocked, source, target):
        return self.check(blocked, source, target) and self.check(blocked, target, source) ;

    # basically, we try to use bfs to walk from the source
    # to target, if we can walk more steps than the blocked cells
    # can round up, then we know the blocked cells can not stop the user.
    def check(self, blocked, source, target):
        seen = set() ; 
        queue = [source] ; 
        steps = 0 ;
        blocked = list(map(tuple, blocked)) ; 
        if len(blocked) == 0:
            return True ; 
        while len(queue) > 0:
            for _ in range(len(queue)):
                i,j = queue.pop(0) ; 
                if (i,j) == target:
                    return True ;
                for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if x < 0 or x >= 10**6 or y < 0 or y >= 10 **6:
                        continue ; 
                    if (x,y) not in seen and (x,y) not in blocked:
                        seen.add((x,y)) ; 
                        queue.append((x,y)) ; 
            steps += 1 ; 
            if steps == len(blocked): break ; 

        if steps < len(blocked):
            return False ; 
        
        return True ; 

    def isEscapePossible2(self, blocked, source, target):
        if len(blocked) == 0:
            return True ; 
        # grow the component
        block = set() ; 
        for b in blocked:
            block.add((b[0], b[1])) ;
        seen = set() ;
        src = (source[0], source[1]) ;
        target = (target[0], target[1]) ; 
        queue = [src] ;
        component = [] ; 
        
        while len(queue) > 0:
            p = queue.pop(0) ; 
            seen.add(p) ; 
            if p[0] == target[0] and p[1] == target[1]:
                return True ; 

            neibors = self.neighbors(p[0], p[1]) ;
            for n in neibors:
                if n not in block and n not in seen:
                    queue.append(n) ; 
        return False ; 

    def neighbors(self, r,c):
        lst = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)] ;
        lst = list(filter(lambda n: n[0] >= 0 and n[0] < (10 ** 6), lst)) ;
        lst = list(filter(lambda n: n[1] >= 0 and n[1] < (10 ** 6), lst)) ;
        return lst ;


def main():
    s = Solution() ; 
    blocked = [[0,1],[1,0]] ; 
    source = [0,0] ; target = [0,2] ;
    result = s.isEscapePossible(blocked, source, target) ;
    print(result) ;


if __name__ == "__main__":
    main() ; 
