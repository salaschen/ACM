
class word:

    def __init__(self, string):
        self.counter = {} ; 
        self.text = string ;
        for i in range(ord('a'), ord('z')+1):
            self.counter[chr(i)] = 0 ; 
        for i in range(0, len(self.text)):
            self.counter[self.text[i].lower()] += 1 ; 

    def compareTo(self, word2):
        if len(self.text) != len(word2.text):
            return False ; 
        for i in range(ord('a'), ord('z')+1):
            if self.counter[chr(i)] != word2.counter[chr(i)]:
                return False ; 
        return True ; 

    def __str__(self):
        result = self.text  + " - "; 
        for i in range(ord('a'), ord('z')+1):
            result += (chr(i) + ":" + str(self.counter[chr(i)])+",") ; 
        return result.rstrip(",") ; 

def work():
    words = [] ; 
    line = input().lstrip() ;
    while (line != "#"):
        for w in line.split(' '):
            if w != '':
                words.append(word(w)) ; 
        line  = input() ; 

    # go through the list and remove any anagrams.
    pos = 0 ;
    while pos < len(words):
        hasAnagram = False; 
        nextW = pos + 1 ; 
        while nextW < len(words):
            if  words[pos].compareTo(words[nextW]) == True:
                words.pop(nextW) ; 
                hasAnagram = True ; 
            else:
                nextW += 1 ;
        if hasAnagram == True:
            words.pop(pos) ; 
        else:
            pos += 1 ; 


    for w in sorted(words, key=lambda w : w.text):
        print(w.text) ; 
    return ;
    
def repr(text):
    cList = [] ;
    ans = "" ; 
    for c in text:
        cList.append(c.lower()) ; 
    cList = sorted(cList) ; 
    for i in range(0, len(cList)):
        ans += cList[i] ; 
    return ans ; 

def work2():
    words = [] ; 
    count = {} ; 
    line = input().lstrip() ;
    while (line != "#"):
        for w in line.split(' '):
            if w != '':
                words.append(w) ; 
                r = repr(w) ; 
                if r not in count:
                    count[r] = 1 ; 
                else:
                    count[r] += 1 ; 
        line  = input() ; 

    ans = [] ; 
    for w in words:
        r = repr(w) ; 
        if count[r] == 1:
            ans.append(w) ; 
    for w in sorted(ans):
        print(w) ; 

def main():
    work2() ; 
    return ; 


if __name__ == "__main__":
    main() ;
