class Solution:
    def findOcurrences(self, text, first, second):
        words = text.split() ; 
        if len(words) < 2:
            return [] ;

        result = [] ; 
        f,s = words[0], words[1] ; 
        index = 2 ;
        while index < len(words):
            cur = words[index] ; 
            if f == first and s == second:
                result.append(cur) ; 
            f, s = s, cur ; 
            index += 1 ; 
        return result;

def main():
    s = Solution() ; 

    first = 'a' ;
    second = 'good' ;
    text = 'alice is a good girl she is a good student' ; 
    
    print(s.findOcurrences(text, first, second)) ;
    return ;

if __name__ == "__main__":
    main() ; 
