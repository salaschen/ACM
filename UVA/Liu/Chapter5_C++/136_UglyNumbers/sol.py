import heapq 

def work():
    numSet = set() ; 
    h = [] ; 
    heapq.heappush(h, 1) ; 

    limit = 1500 ; 
    i = 1 ; 
    while i < limit:
        cur = heapq.heappop(h) ; 
#        print(cur) ; # debug
        i += 1 ; 
        l = [cur*2, cur*3, cur*5] ; 
        for n in l:
            if n not in numSet:
                heapq.heappush(h, n) ; 
                numSet.add(n) ; 

    print("The %d'th ugly number is %d." % (limit, heapq.heappop(h))) ; 
    return ; 

def main():
    work() ; 

if __name__ == "__main__":
    main() ; 
