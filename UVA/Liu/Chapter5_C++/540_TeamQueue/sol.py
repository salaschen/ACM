'''
Problem 540 UVA TEAM QUEUE
Date: 04/June/2017
'''

def Enqueue(Map, Rank, teamsInQueue, num):
    teamId = Map[num] ;
    if teamId in Rank:
        teamsInQueue[teamId].append(num) ; 
    else:
        Rank.append(teamId) ; 
        teamsInQueue[teamId].append(num) ; 
    return ; 

# optimistic, not to check boundary
def Dequeue(Rank, teamsInQueue):
    if len(Rank) == 0:
        return "" ; 
    teamId = Rank[0] ; 
    result = (teamsInQueue[teamId]).pop(0) ; 
    if len(teamsInQueue[teamId]) == 0:
        Rank.pop(0) ; 
    return result ; 

def work(t):
    num = 0 ;
    teamMap = {} ; 
    num = int(input()) ; 
    if num == 0:
        return 1 ; 
    
    teamRank = [] ; 
    teamsInQueue = [ [] for x in range(0, num) ] ; 
    for i in range(0, num):
        nums = [int(s) for s in input().split(" ")] ; 
        for j in range(1, len(nums)):
            teamMap[nums[j]] = i ; 

    # Reading and process command.
    print("Scenario #%d" % t) ; 
    line = input() ; 
    while line != 'STOP':
        if line[0] == 'E':
            Enqueue(teamMap, teamRank, teamsInQueue,
                    int((line.split(" "))[1])) ; 
        elif line[0] == 'D':
            print(Dequeue(teamRank, teamsInQueue)) ; 
        line = input() ; 
    print() ; 
    return 0 ; 


def main():
    t = 1 ; 
    while work(t) == 0:
        t += 1 ; 


if __name__ == "__main__":
    main() ; 
