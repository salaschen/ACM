class Solution:
    def reconstructQueue(self, people):
        '''
        :type people: List[List[int]]
        :rtype: List[List[int]]
        '''
        # sort the people by height first, then by number of people in front
        people = sorted(people, key=lambda p: p[1]) ; 
        people = sorted(people, key=lambda p: p[0], reverse=True) ; 

        print(people) ; # debug

        result = [] ; 
        for i in range(0, len(people)):
            p = people[i] ;
            insPos = p[1] ; 
            result.insert(insPos, p) ; 
        
        return result ; 


if __name__ == "__main__":
    s = Solution() ;
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] ; 
    result = s.reconstructQueue(people) ; 
    print('result:', result) ; 
