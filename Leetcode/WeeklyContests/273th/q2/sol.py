class Solution:
    def executeInstructions(self, n: int, startPos: [int], s: str) -> [int]:
        result = []
        for i in range(0, len(s)):
            seq = s[i:]
            result.append(self.countMoves(n, startPos, seq))
        return result

    def countMoves(self, n: int, startPos: [int], s) -> int:
        result = 0
        curPos = startPos
        for ch in s:
            nPos, temp = self.move(n, curPos, ch)
            if not temp:
                return result
            else:
                curPos = nPos
                result += 1
        return result

    def move(self, n: int, pos: [int], instruct: str) -> ([int], bool):
        d = dict()
        d['L'] = (0, -1)
        d['R'] = (0, 1)
        d['U'] = (-1, 0)
        d['D'] = (1, 0)
        direction = d[instruct]
        newPos = [pos[0] + direction[0], pos[1]+direction[1]]
        if newPos[0] < 0 or newPos[0] >= n:
            return (newPos, False)
        if newPos[1] < 0 or newPos[1] >= n:
            return (newPos, False)
        else:
            return (newPos, True)

### test ###
s = Solution()
n = 3
startPos = [0,1]
seq = "RRDDLU"
print(s.executeInstructions(n, startPos, seq))

n = 2
startPos = [1,1]
seq = "LURD"
print(s.executeInstructions(n, startPos, seq))

n = 1
startPos = [0,0]
seq = "LRUD"
print(s.executeInstructions(n, startPos, seq))

