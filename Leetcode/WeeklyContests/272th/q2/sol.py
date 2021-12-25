class Solution:
    def addSpaces(self, s: str, spaces: [int]) -> str:
        result = ''
        prev = 0
        for pos in spaces:
            result = result + s[prev:pos] + ' ' + s[pos]
            prev = pos+1
            # print(result) # debug

        result += s[spaces[-1]+1:]
        return result

### test ###
sol = Solution()
s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
print(sol.addSpaces(s, spaces))

s = "icodeinpython"
spaces = [1,5,7,9]
print(sol.addSpaces(s, spaces))

s = "spacing"
spaces = [0,1,2,3,4,5,6]
print(sol.addSpaces(s, spaces))

