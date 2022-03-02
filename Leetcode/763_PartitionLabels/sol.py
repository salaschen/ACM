'''
Prob: 763 Partition Labels - Medium
Author: Ruowei Chen
Date: 26/Feb/2022
Note:
    1) discovering intervals
    2) then merge those intervals
    3) whatever is left, it's the partition.
'''
class Solution:
    def partitionLabels(self, s: str) -> [int]:
        mem = dict()
        for i in range(len(s)):
            ch = s[i]
            if ch not in mem:
                mem[ch] = [i, i]
            else:
                x, y = mem[ch]
                mem[ch] = [x, i]

        partitions = []
        for key in mem.keys():
            x,y = mem[key]
            partitions.append([x,y,key])

        partitions = sorted(partitions)
        # print(partitions) # debug

        # do the merges
        j = 0
        while j < len(partitions)-1:
            cur = partitions[j]
            nex = partitions[j+1]
            if nex[0] >= cur[0] and nex[0] < cur[1]:
                # can merge
                x,y = min(cur[0], nex[0]), max(cur[1], nex[1])
                partitions[j] = [x,y,cur[2]]

                # remove partions[j+1]
                partitions = partitions[:j+1] + partitions[j+2:]
            else:
                j += 1
                
        # print(partitions) # debug
        result = []
        for i in range(len(partitions)):
            x, y, _ = partitions[i]
            result.append(y-x+1)
        return result

### test ###
sol = Solution()
s = "ababcbacadefegdehijhklij"
print(sol.partitionLabels(s))

s = "eccbbbbdec"
print(sol.partitionLabels(s))

