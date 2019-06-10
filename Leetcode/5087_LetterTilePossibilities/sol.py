'''
Note:
    1. 1 <= tiles.length <= 7
    2. tiles consists of uppercase English letters.
'''

class Solution:
    def numTilePossibilities(self, tiles):
        perms = self.permutation(tiles) ; 
        result = set() ; 
        for word in perms:
            for i in range(1, len(tiles)+1):
                result.add(word[:i]) ; 
        
        return len(result) ;

    def permutation(self, text):
        # text is str
        # return List[str]
        if len(text) == 0:
            return [] ;
        if len(text) == 1:
            return [text] ; 

        head = text[0] ; 
        tailPerm = self.permutation(text[1:]) ; 
        
        result = set() ;
        for tail in tailPerm:
            for i in range(0, len(tail)+1):
                result.add(tail[0:i]+head+tail[i:]) ; 

        return list(result) ; 



# test 
def main():
    s = Solution() ; 
    result = s.permutation('AAABBC') ;
    print(result) ; 

    print(s.numTilePossibilities('AAABBC')) ; 
    print(s.numTilePossibilities('AAB')) ; 



if __name__ == "__main__":
    main() ; 

        

