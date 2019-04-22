'''
GCJ 2019 1A - Alien Rhyme
Author: Ruowei Chen
Date: 22/April/2019
Note:
    1) Implementation of the analysis solution, using trie.
'''

class Trie:
    # create a dummy node to represent the node.
    def __init__(self, value=''):
        self.value = value ;
        self.IsWord = False ; 
        self.childs = dict() ; # chiild is Str -> Trie
    
    def __str__(self):
        w = 'dummy' if self.value == '' else self.value ; 
        return '{0}, fvalue={2} -> {1}'.\
                format(w, list(self.childs.keys()), self.fvalue()) ; 

    def addWord(self, word):
        # if word is empty, just return
        if len(word) == 0:
            self.IsWord = True ; 
            return ;
        char = word[0] ; 
        if char not in self.childs:
            self.childs[char] = Trie(char) ; 
        self.childs[char].addWord(word[1:]) ;
        return ;

    def fvalue(self):
        # inherit all the values from child nodes.
        result = 0 ; 
        for key in self.childs.keys():
            result += self.childs[key].fvalue() ; 
        if self.IsWord:
            result += 1 ; 
        if result >= 2 and self.value != '':
            result -= 2 ; 
        return result ; 

    def printTrie(self):
        print(self) ; 
        for key in self.childs.keys():
            self.childs[key].printTrie() ;

def reverseWord(word):
    w = list(word) ; 
    w.reverse() ; 
    result = '' ; 
    for char in w:
        result += char ; 
    return result ; 

def test():
    words = ['JAM', 'CODEJAM', 'SPACEJAM', 'APPLEJAM'] ;
    trie = Trie() ; 
    for w in words:
        w = reverseWord(w) ; 
        trie.addWord(w) ; 

    trie.printTrie() ;
    return ;

def work(Case):
    N = int(input()) ; 
    words = [] ;
    for i in range(N):
        w = input() ; 
        rw = reverseWord(w) ;
        words.append(rw) ; 
    trie = Trie() ;
    for w in words:
        trie.addWord(w) ; 
    
    # trie.printTrie() ; # debug
    print('Case #{0}: {1}'.format(Case, N-trie.fvalue())) ; 
    return ;

def solve():
    T = int(input()) ; 
    for i in range(T):
        work(i+1) ; 
    return ;

def main():
    # test() ;
    solve() ; 
    return ;

if __name__ == "__main__":
    main() ; 
