import random 
import time 

class Solution:
    def maxProduct2(self, words):
        '''
        Note: Other users' submission. Beats 99.7% submissions.
        '''
        d = {} ;
        for w in words:
            mask = 0 ; 
            for c in set(w):
                mask |= (1 << (ord(c) - 97)) ; 
            d[mask] = max(d.get(mask, 0), len(w)) ;
        return max([d[x]*d[y] for x in d for y in d if not x & y] or [0])

    def maxProduct(self, words):
        '''
        :type words: List[str]
        :rtype: int
        :Note: Use bit operations
        : beats 58% of users.
        '''
        mappedWords = list(map(lambda w: self.translate(w), words)) ;
        result = 0 ; 
        # sort by word length
        # mappendWords = sorted(mappedWords, key=lambda elem: elem[1], reverse=True) ; 
        for i in range(0, len(words)-1):
            for j in range(i+1, len(words)):
                A = mappedWords[i] ; 
                B = mappedWords[j] ; 
                # if A[1] * B[1] <= result:
                #     break ; # exit inner loop
                if A[0] & B[0] == 0:
                    result = max(result, A[1]*B[1]) ; 
        return result ; 

    def translate(self, word):
        '''
        Translate a word into a tuple of (integer, integer)
        Where the first is the bitmap of the word, and the second is the 
        length of the word.
        '''
        length = len(word) ; 
        letters = set(list(word)) ;
        result = 0 ; 
        for ch in letters:
            result |= 1 << (ord(ch)-97) ; 
        return (result, length) ; 


    def maxProduct0(self, words):
        '''
        :type words: List[str]
        :rtype: int
        :Note: Brute Force
        '''
        result =0 ; 
        for i in range(0, len(words)-1):
            for j in range(i, len(words)):
                A = words[i] ; 
                B = words[j] ; 
                if not self.ShareSameLetter(A, B):
                    result = max(result, len(A)*len(B)) ; 
        return result ; 
        

    def ShareSameLetter(self, A, B):
        for c in A:
            if c in B:
                return True ; 
        return False ; 

def Test():
    size = 2000 ;
    maxLen = 1000 ; 
    words = [] ; 
    for i in range(0, size):
        wLen = random.randint(1, maxLen) ; 
        word = "" ; 
        for j in range(0, wLen):
            word += chr(random.randint(ord('a'), ord('z'))) ; 
        words.append(word) ; 
    
    s = Solution() ; 
    
    start = time.time() ; 
    r1 = s.maxProduct0(words) ; 
    end = time.time() ; 
    print("result 0={0}, time={1} milliseconds".format(r1, (end-start)*100)) ; 
     
    start = time.time() ; 
    r1 = s.maxProduct(words) ; 
    end = time.time() ; 
    print("result 1={0}, time={1} milliseconds".format(r1, (end-start)*100)) ; 
       
    start = time.time() ; 
    r1 = s.maxProduct2(words) ; 
    end = time.time() ; 
    print("result 2={0}, time={1} milliseconds".format(r1, (end-start)*100)) ; 
    return ; 
       
if __name__ == "__main__":
    s = Solution() ;

    words =  ["abcw","baz","foo","bar","xtfn","abcdef"] ;
    print("words:", words) ; 
    print(s.maxProduct(words)) ; 

    words = ["a","ab","abc","d","cd","bcd","abcd"]
    print("words:", words) ; 
    print(s.maxProduct(words)) ; 

    words = ["a","aa","aaa","aaaa"]
    print("words:", words) ; 
    print(s.maxProduct(words)) ; 

    Test() ; 
