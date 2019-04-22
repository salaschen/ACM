'''
GCJ 1A: Alien Rhyme
Author: Ruowei Chen
Brute-Force
'''
def readInput():
    N = int(input()) ; 
    words = [] ; 
    for i in range(N):
        words.append(input()) ; 
    return words ; 

# return a list of strings that are each of targetLen
# which are equally selected from words.
# words: List[str]
# return: List[List[str]]
def select(words, targetLen):
    if len(words) < targetLen:
        return None ; 
    if len(words) == targetLen:
        return [words] ; 
    if targetLen == 0:
        return [] ; 
    result = [] ; 
    for i in range(len(words)):
        w = words.copy() ; 
        cur = w.pop(i) ; 
        wls = select(w, targetLen-1) ;
        if wls is None: 
            continue ; 
        if len(wls) == 0:
            result.append([cur]) ;
        else:
            for wordList in wls:
                wordList.append(cur) ; 
                wordList.sort() ;
                result.append(wordList) ;
    return result ; 

def checkPairs(pairs, Map):
    for i in range(0, len(pairs)-1):
        p1 = pairs[i] ; 
        for j in range(i+1, len(pairs)):
            p2 = pairs[j] ; 
            if p1[2] != p2[2]: # rhyming position is not the same.
                continue ; 
            w11 = p1[0] ; 
            w12 = p1[1] ; 
            w21 = p2[0] ; 
            w22 = p2[1] ; 
            if (w21, p1[2]) in Map[w11] or (w22, p1[2]) in Map[w11]:
                return False ; 
            if (w21, p1[2]) in Map[w12] or (w22, p1[2]) in Map[w12]:
                return False; 
    return True ; 

def tryMatch(pairs, restWords, Map):
    if len(restWords) == 0:
        return checkPairs(pairs, Map) ; 
    else:
        w = restWords[0] ; 
        found = False ; 
        matchings = Map[w] ; 
        result = False ; 
        for i in range(1, len(restWords)):
            other = restWords[i] ; 
            for p in matchings:
                if other == p[0]:
                    found = True ; 
                    ppairs = pairs.copy() ; 
                    ppairs.append((w, other, p[1])) ;
                    rwords = restWords.copy() ; 
                    rwords.remove(w) ; 
                    rwords.remove(other);
                    result = tryMatch(ppairs, rwords, Map) ; 
                    if result: 
                        return result ; 
                    else:
                        break ; 
        return False ; 
        
def canFindPairs(List):
    # generate the rhyme pairs
    Map = dict() ; # from word to (word, rpos) ; 
    for i in range(0, len(List)-1):
        w = List[i] ;
        wlen = len(w) ; 
        Map[w] = [] ; 
        for j in range(i+1, len(List)):
            aw = List[j] ; 
            if aw not in Map:
                Map[aw] = [] ; 
            alen = len(aw) ; 
            if aw[-1] != w[-1]:
                continue ; 
            length = 0 ; 
            for i in range(1, min(wlen, alen)+1):
                if aw[-1*i] == w[-1*i]:
                    length += 1 ; 
                else:
                    break ; 
            Map[w].append((aw, length)) ; 
            Map[aw].append((w, length)) ; 
    # print(Map) ; # debug
    
    # recursively try to match pairs.
    result = tryMatch([], List, Map) ; 

    return result; 

# return true or false
def hasSolution(words, targetLen):
    wordList = select(words, targetLen) ;    
    if wordList is None or len(wordList) == 0:
        return False ; 

    seenList = set() ; 
    for List in wordList:
        if str(List) in seenList:
            continue ; 
        if canFindPairs(List):
            return True ; 
        else:
            seenList.add(str(List)) ; 
    return False ; 

def solve(Case):
    words = readInput() ; 
    wlen = len(words) ; 
    if wlen % 2 == 1:
        wlen -=1 ; 

    while wlen > 0:
        if hasSolution(words, wlen):
            print('Case #{0}: {1}'.format(Case, wlen)) ; 
            return ; 
        else:
            wlen -= 2 ; 
    print('Case #{0}: 0'.format(Case)) ; 
    return ;

def work():
    T = int(input()) ; 
    for i in range(1, T+1):
        solve(i) ; 
    return ; 

def test():
    A = ['TARPOL', 'PROL', 'TARPRO', 'JAM', 'HAM', 'CODEJAM'] ; 
    result = select(A, 4) ; 
    print(len(result)) ; 
    print(result) ; 
    

def main():
   # test() ; 
    work() ; 

if __name__ == "__main__":
    main() ; 
