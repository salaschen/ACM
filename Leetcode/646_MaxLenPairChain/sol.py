import random 
class Solution:
    def findLongestChain(self, pairs):
        '''
        Dynamic Programming
        '''
        sorted_pairs = sorted(pairs, key=lambda p: p[0]) ; 
        curMin = sorted_pairs[0][0] ;
        sorted_pairs.insert(0, [curMin-2, curMin-1]) ; # insert dummy pair for starting.
        d = [1 for x in range(0, len(sorted_pairs))] ; # d[0] is dummy start
        d[0] = 0 ; 
        result = 1 ; 
        for i in range(1, len(sorted_pairs)):
            cur = sorted_pairs[i]; 
            j = i-1  ; 
            while j >= 0:
                prev = sorted_pairs[j] ; 
                if self.LargerThan(cur, prev):
                    d[i] = d[j] + 1 ; 
                    result = max(result, d[i]) ; 
                    break ; 
                j -= 1 ; 
        print('result:', result) ; # debug
        return result ; 

    def LargerThan(self, p1, p2):
        # return True if p1 > p2
        return p1[0] > p2[1] ; 

if __name__ == "__main__":
    s = Solution() ; 
    pairs = [[1,2],[3,4],[2,3]] ; 
    print('pairs:', pairs) ; 
    s.findLongestChain(pairs) ; 

    pairs = [[1,2],[3,4],[5,6],[7,8]] ;
    print('pairs:', pairs) ; 
    s.findLongestChain(pairs) ; 

    pairs = [[1,2]] ; 
    print('pairs:', pairs) ; 
    s.findLongestChain(pairs) ; 

    pairs = [[1,9], [2,3], [4,5], [6,7]] ; 
    print('pairs:', pairs) ; 
    s.findLongestChain(pairs) ; 

    pairs = [[1,2], [4,7],[3,5], [5,6]] ; 
    print('pairs:', pairs) ; 
    s.findLongestChain(pairs) ; 

    # large case
    pairs = [] ; 
    num = 1000 ; 
    low, up = -10000, 10000 ; 
    for i in range(0, num):
        pairs.append([random.randint(low, up), random.randint(low, up)]) ; 
    s.findLongestChain(pairs) ; 
    

