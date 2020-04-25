'''
GCJ - Round1A - Square Dance
Author: Ruowei Chen
Date: 11/Apr/2020
Note: 
    1) Brute-force.
    2) Implementation based on the official analysis, use linkedlist to keep track of a 
    dancer's neighbors, and only checks the neighbors of an eliminated dancer.
'''
import random
import functools
import time
class Dancer:
    def __init__(self, coord: (int, int),  skill: int):
        self.r, self.c = coord
        self.coord = coord
        self.skill = skill
        self.east, self.north, self.west, self.south = [None for _ in range(4)]
        return
    
    def toBeEliminated(self) -> bool:
        neibors = self.neighbors()
        if len(neibors) == 0:
            return False
        else:
            total = 0
            num = 0
            for n in neibors:
                total += n.skill
                num += 1

            avg = total / num
            return self.skill < avg
    
    def updateNeighbors(self): # update the neighbor's upon the elimination
        if self.east != None:
            self.east.west = self.west
        if self.west != None:
            self.west.east = self.east
        if self.north != None:
            self.north.south = self.south
        if self.south != None:
            self.south.north = self.north

    def neighbors(self) :
        result = []
        if self.east is not None:
            result.append(self.east)
        if self.west is not None:
            result.append(self.west)
        if self.south is not None:
            result.append(self.south)
        if self.north is not None:
            result.append(self.north)
        return result
        
        # return list(filter(lambda d: d is not None, \
        #         [self.east, self.west, self.south, self.north]))

    def neighborString(self):
        return list(map(lambda d: str(d), self.neighbors()))

    def __str__(self):
        return "Dancer location: {0}, Skill: {1}".format((self.r, self.c), self.skill)

class Solution:
    def __init__(self):
        pass

    def main(self):
        T = int(input())
        for i in range(T):
            result = self.work()
            print('Case #{0}: {1}'.format(i+1, result))
        return
    
    def work(self):
        R, C = [int(n) for n in input().split()]
        skill = []
        for i in range(R):
            row = [int(n) for n in input().split()]
            skill.append(row)
        # result = self.run(skill, R, C)
        result = self.run2(skill, R, C)
        return result

    def genDancers(self, skill: [[int]], R: int, C: int):
        # create dancers
        dancers = []
        for i in range(R):
            row = []
            for j in range(C):
                cur  = Dancer((i,j), skill[i][j])
                row.append(cur)

                # now setup neighbors
                if i > 0:
                    north = dancers[i-1][j]
                    north.south, cur.north = cur, north
                
                if j > 0:
                    east = row[j-1]
                    cur.east, east.west = east, cur
            dancers.append(row)

        return dancers 

    # implementation of the official analysis
    def run2(self, skill: [[int]], R: int, C:int, debug=False):
        dancers = self.genDancers(skill, R, C)
        # debug
        if debug:
            skillMap = list(map(lambda row: \
                    list(map(lambda d: str(d), row)), skill))
            for row in skillMap:
                print(functools.reduce(lambda a,b: a+'  '+b, row))
            print()

        curTotal = sum(list(map(lambda row: sum(row), skill)))
        # toCheck = set(list(dancers.keys()))
        toCheck = set()
        for i in range(R):
            for j in range(C):
                toCheck.add((i,j))
        result = curTotal
        gone = set()
        while True:
            # check every one first.
            elimis = set()
            hasNextRound = False
            for loc in toCheck:

                if loc in gone:
                    continue

                dancer = dancers[loc[0]][loc[1]]
                # print(str(dancer), dancer.neighborString()) # debug
                if debug:
                    print(str(dancer), dancer.toBeEliminated()) # debug

                if dancer.toBeEliminated():
                    elimis.add(loc)
                    curTotal -= dancer.skill
                    hasNextRound = True
                    gone.add(loc)
                
                    # debug
                    if debug:
                        skillMap[loc[0]][loc[1]] = '*'
            # debug
            if debug:
                for row in skillMap:
                    print(functools.reduce(lambda a,b: a+'  '+b, row))

                print('eliminated: {0}'.format(elimis)) # debug
                print('curTotal: {0}'.format(curTotal)) # debug


            if not hasNextRound:
                break
            
            # set up toCheck for the next round
            toCheck = set()
            for loc in elimis:
                dancer = dancers[loc[0]][loc[1]]
                dancer.updateNeighbors()
                for n in dancer.neighbors():
                    toCheck.add(n.coord)
            
            result += curTotal
        return result 

    # run the dance on multiple rounds
    def run(self, skill, R, C):
        floor = [[1 for n in range(C)] for j in range(R)]
        result = 0
        
        while True: 
            # print(floor) # debug
            for i in range(R):
                for j in range(C):
                    if floor[i][j] == 1:
                        result += skill[i][j]
            num = self.round(floor, skill, R, C)
            if num == 0:
                break
        return result

    # return the number of players eliminated
    # also sets the floor for players that are eliminated
    def round(self, floor, skill, R, C):
        compass = dict()
        players = set()
        
        # get the compass in the same row.
        for i in range(R):
            pc = -1
            j = 0
            while j < C and j >= 0:
                if floor[i][j] == 0: 
                    j += 1
                else:
                    # now try to find the neighbor
                    players.add((i,j))
                    nc = -1
                    for k in range(j+1, C):
                        if floor[i][k] == 1:
                            nc = k
                            break
                    if (i, j) not in compass:
                        compass[(i,j)] = []
                    if pc != -1:
                        compass[(i,j)].append((i,pc))
                    if nc != -1:
                        compass[(i,j)].append((i, nc))
                    pc = j
                    j = nc

        # get the compass in the same col
        for j in range(C):
            pr = -1 
            i = 0
            while i < R and i >= 0:
                if floor[i][j] == 0:
                    i += 1
                else:
                    # now try to find the neighbor
                    players.add((i,j))
                    nr = -1
                    for k in range(i+1, R):
                        if floor[k][j] ==  1:
                            nr = k
                            break
                    if (i,j) not in compass:
                        compass[(i,j)] = []
                    if pr != -1:
                        compass[(i,j)].append((pr, j))
                    if nr != -1:
                        compass[(i,j)].append((nr, j))
                    pr = i
                    i = nr

        # now we have all the compass, do the 
        eliminated = set()
        for player in players:
            compLevel = sum(list(map(lambda p: skill[p[0]][p[1]], compass[player])))
            avg = 0
            if len(compass[player]) > 0:
                avg = compLevel / len(compass[player])
            if skill[player[0]][player[1]] < avg:
                eliminated.add(player)

        # now update the floor
        for p in eliminated:
            floor[p[0]][p[1]] = 0

        return len(eliminated)

#### test ####
def test():
    T = 100
    s = Solution()
    Pass = 0
    bTime, nTime = 0, 0
    for i in range(T):
        R, C = [random.randint(1, 100) for _ in range(2)]
        skill = []
        for j in range(R):
            skill.append([random.randint(1, 10**6) for _ in range(C)])
        start = time.time()
        expect = s.run(skill, R, C)
        end = time.time()
        bTime = bTime + (end-start)
        start = time.time()
        actual = s.run2(skill, R, C)
        end = time.time()
        nTime += (end-start)
        Pass += 1 if expect == actual else 0
        print('Case #{0}: {1}'.format(i+1, 'pass' if expect == actual else 'failed'))
    print('test result: {0}/{1} passed.'.format(Pass, T))
    print('bruteforce: {0:.3} sec, new : {1:.3} sec'.format(bTime, nTime))

# test()
s = Solution()
s.main()

# skill = [[5,7], [5,6]]
# result = s.run2(skill, len(skill), len(skill[0]))
# print(result)




