
def work():
    article = "" ; 
    while True:
        try :
            line = input() ; 
            for s in line:
                if s.isalpha():
                    article += s.lower() ; 
                else:
                    article += " " ; 
        except EOFError:
            break ; 
    words = sorted(article.split()) ; 
    wordSet = set() ;  
    for w in words:
        if w not in wordSet:
            print(w) ; 
            wordSet.add(w) ; 

def main():
    work() ; 

if __name__ == "__main__":
    main() ; 
