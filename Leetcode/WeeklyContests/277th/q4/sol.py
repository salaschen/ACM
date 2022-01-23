'''
DFS?
'''
class Solution:
    def __init__(self):
        self.best = 0
        self.size = 0

    def maximumGood(self, statements: [[int]]) -> int:
        self.size = len(statements)
        for i in range(self.size):
            pass

        bad = self.findCycle(statements)
        # print('statements:', statements) # debug
        # print('bad:', bad) # debug
        
        people = set([i for i in range(self.size)])
        people = people - bad

        # print('people:', people) # debug
        if len(people) == 0:
            return 0

        # print('friends:', self.friends) # debug
        result = 0
        for p in people:
            friends = self.friends[p]
            # print('trying: ', p) # debug
            # print('initial:', people-friends) # debug
            temp = self.dfs(friends, people-friends, statements) 
            result = max(result, temp)

        return result 

    def dfs(self, friends: set, remaining: set, statements:[[int]]) -> int:
        t1 = len(friends)

        if len(remaining) == 0:
            return t1

        p = remaining.pop()
        t2 = self.dfs(friends, remaining, statements)

        otherSet = self.friends[p]
        t3 = 0
        if self.check(friends, otherSet, statements):
            t3 = self.dfs(friends.union(otherSet), remaining-otherSet, statements) 

        result = max(t1, t2, t3)
        remaining.add(p)
        return max(t1, t2, t3)

    # check whether two groups are in conflict or not
    # return True if can be harmony, False otherwise
    def check(self, g1: set, g2: set, statements: [[int]]) -> bool:
        for p1 in g1:
            for p2 in g2:
                if statements[p1][p2] == 0 or statements[p2][p1] == 0:
                    return False
        return True


    # return a set of people that cannot be good person.
    # and for each people, find a group of friends when this person is 
    # a good person.
    def findCycle(self, statements: [[int]]) -> set:
        n = self.size 
        bad = set()
        self.friends = dict()
        for i in range(n):
            if i in bad:
                continue
            self.friends[i] = self.dfsCycle(i, statements, bad)
        
        return bad 

    # return the friends of root
    # if root cannot be a good person, then return an empty set.
    def dfsCycle(self, root, statements: [[int]],  bad: set) -> set:
        cur = root
        queue, added = [root], set()
        result = set()
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur in bad:
                return set() 

            # check if cur is contradicting with anyone already in result
            for p in result:
                if statements[p][cur] == 0 or statements[cur][p] == 0:
                    # contradicts happens
                    bad.add(root)
                    return set() # return an empty set

            # no contradictions is found
            result.add(cur)

            # expand the queue
            for p in range(self.size):
                if p not in result and p not in added and statements[cur][p] == 1:
                    added.add(p)
                    queue.append(p)
                    
        return result
    

### test ###
s = Solution()

statements = [[2,1,2],[1,2,2],[2,0,2]]
print(s.maximumGood(statements))

statements = [[2,1,2],[1,2,1],[0,0,2]]
print(s.maximumGood(statements))

statements = [[2,0],[0,2]]
print(s.maximumGood(statements))

statements = [[2,0,2,2,0],[2,2,2,1,2],[2,2,2,1,2],[1,2,0,2,2],[1,0,2,1,2]]
print(s.maximumGood(statements))

statements = [[2,2,2,2],[1,2,1,0],[0,2,2,2],[0,0,0,2]]
print(s.maximumGood(statements))

statements = [[2,2,2,2,0,1,2,0,0,2],[2,2,2,2,2,2,2,2,2,2],[2,0,2,2,0,1,0,2,2,1],[2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2],[1,0,1,0,2,2,2,0,0,1],[2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2],[2,0,1,2,2,1,2,2,2,2]]
print(s.maximumGood(statements))

