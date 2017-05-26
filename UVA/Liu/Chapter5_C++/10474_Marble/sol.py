import bisect

def work(t) :
    line = "" ; 
    while True:
        line = input() ; 
        if line != '': break ; 
    words = line.split(" ") ; # debug
    N = int(words[0]) ; 
    Q = int(words[1]) ; 
    if N==0 and Q ==0:
        return 1 ; 
    numList = [] ; 
    i = 0 ; 
    while i < N :
        line = input() ; 
        if line == '': continue ; 
        numList.append(int(line)) ; 
        i += 1 ; 
    numList.sort() ; 
    print("CASE# %d:" % (t)) ; 
    i = 0 ;
    while i < Q:
        line = input() ; 
        if line == '': continue ; 
        query = int(line) ; 
        p = bisect.bisect_left(numList, query) ; 
        if p != len(numList) and numList[p] == query:
            print("%d found at %d" % (query, p + 1)) ; 
        else:
            print("%d not found" % (query)) ; 
        i+=1 ; 
    return 0  ; 
    

def main():
    t = 1 ; 
    while (work(t) == 0):
        t += 1 ; 
    return ; 

if __name__ == "__main__":
    main() ; 
