class Solution:
    def numRescueBoats(self, people, limit):
        result = 0 ; 
        people = sorted(people) ; 
        front, back = 0, len(people)-1 ; 
        while front < back:
            f,b = people[front], people[back] ; 
            if f+b <= limit: 
                result += 1 ;
                people[front], people[back] = 0, 0 ; 
                front += 1 ; 
                back -= 1 ; 
            else:
                back -= 1 ;
        result += len(list(filter(lambda n: n != 0, people))) ; 
        return result ; 


if __name__ == "__main__":
    
    s = Solution() ;

    people = [3,5,3,4] ;
    limit = 5 ; 
    print('result=', s.numRescueBoats(people, limit)) ; 

    people = [1,2]
    limit = 3 ; 
    print('result=', s.numRescueBoats(people, limit)) ; 

    people = [3,2,2,1]
    limit = 3 ; 
    print('result=', s.numRescueBoats(people, limit)) ; 


