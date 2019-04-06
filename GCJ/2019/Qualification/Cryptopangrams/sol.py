def gcd(a,b):
    if b == a:
        return a ; 
    if b > a:
        return gcd(b, a) ; 
    if b == 0:
        return a ; 
    else:
        return gcd(b, a % b) ; 

def testGcd():
    a,b = 217, 1891 ; 
    print('a={0}, b={1}, gcd={2}'.format(a,b,gcd(a,b))) ; 
    return ; 

def genList(first, numbers):
    nums = [first] ; 
    for i in range(0, len(numbers)):
        if nums[-1] == 0:
            return [] ; 
        nums.append(numbers[i]//nums[-1]) ; 
    return nums ; 

def work(Case):
    N, L = [int(n) for n in input().split()] ; 
    numbers = [int(n) for n in input().split()] ; 
    while len(numbers) < L:
        numbers.extend([int(n) for n in input().split()]) ; 

    # try to get the first number
    num = gcd(numbers[0], numbers[1]) ; 
    ppnum = [] ;
    pnum = [] ; 
    if numbers[0] == numbers[1]:
        # meaning the first two numbers are the same.
        # try to see if it's a square.
        t = numbers[0] ** 0.5 ; 
        if t.is_integer(): 
            num = int(t) ; 
            pnum = genList(num, numbers) ; 
            ppnum = list(set(pnum.copy())) ;
        else:
            index = 0 ; 
            while numbers[index] == numbers[index+1]:
                index += 1 ; 
            first = gcd(numbers[index], numbers[index+1]) ; 
            # there are two possibilities
            nums1 = genList(first, numbers) ; 
            nums2 = genList(numbers[0]//first, numbers) ; 
            ppnum = list(set(nums1.copy())) ; 
            pnum = nums1 ;
            if len(ppnum) != 26:
                ppnum = list(set(nums2.copy())) ;
                pnum = nums2 ; 

    # normal case
    else:
        second = num; 
        first = numbers[0] // second ; 
        nums1 = genList(first, numbers) ; 
        ppnum = list(set(nums1.copy())) ; 
        pnum = nums1 ;

    # print(ppnum) ; # debug
    # print(len(ppnum)) ; # debug
    ppnum.sort() ;
    Map = dict() ; 
    Aindex = ord('A') ; 
    for i in range(0, len(ppnum)):
        Map[ppnum[i]] = chr(Aindex+i) ; 
    # print(Map) ; # debug

    message = '' ;
    for c in pnum:
        message += Map[c] ; 
    print('Case #{0}: {1}'.format(Case, message)) ; 
    return ; 

def main():
    # testGcd(); 
    T = int(input()) ; 
    for i in range(1, T+1):
        work(i) ; 

if __name__ == "__main__":
    main() ; 
