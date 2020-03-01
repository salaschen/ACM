class Solution:
    def rankTeams(self, votes: [str]) -> str:
        # get the number of teams.
        numTeam = len(votes[0])
        if numTeam == 1:
            return votes[0]

        # prepare the vote record.
        voteDict = dict()
        for team in votes[0]:
            voteDict[team] = [0 for x in range(numTeam)]

        # now read the votes
        for vote in votes:
            for i in range(0, len(vote)):
                team = vote[i]
                pos = i
                voteDict[team][pos] += 1

        
        # now cluster the team to each block.
        blocks = self.clusterTeam(numTeam, voteDict, 0, list(votes[0]))
        # print('blocks:', blocks)
        result = ""
        for block in blocks:
            result += self.solveBlock(voteDict, numTeam, block, 1)
        return result
       
    
    # now solve each block
    def solveBlock(self, voteDict, numTeam, teams: [str], pos) -> str:
        if len(teams) == 0:
            return ""
        elif len(teams) == 1:
            return teams[0]
        
        # print('block:', teams)
        blocks = self.clusterTeam(numTeam, voteDict, pos, teams)
        result = ""
        for block in blocks:
            if len(block) == 1:
                result += block[0]
            else:
                result += self.solveBlock(voteDict, numTeam, block, pos+1)
        return result


    def clusterTeam(self, numTeam, voteDict, pos, teams: [str]) -> [[str]]:
        # now solve by alphabetical
        if numTeam == pos:
            lst = sorted(teams)
            result = ""
            for i in range(len(teams)):
                result += lst[i]
            return [[result]]

        voteCounts = set() 
        teamVote = dict()
        for key in teams:
            num = voteDict[key][pos]
            voteCounts.add(voteDict[key][pos])
            if num not in teamVote:
                teamVote[num] = [key]
            else:
                teamVote[num].append(key)

        voteCounts = sorted(list(voteCounts), reverse=True)
        result = []
        for i in range(0, len(voteCounts)):
            num = voteCounts[i]
            result.append(teamVote[num])

        return result



#### test ####
s = Solution()
'''
votes = ["ABC","ACB","ABC","ACB","ACB"]
print(s.rankTeams(votes))

votes = ["WXYZ","XYZW"]
print(s.rankTeams(votes))

votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
print(s.rankTeams(votes))
'''

votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
print(s.rankTeams(votes))

