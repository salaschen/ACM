'''
Prob: 49 - Group Anagrams
Author: Ruowei Chen
Date: 06/Mar/2022
'''
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        mem = dict()
        for word in strs:
            key = ''.join(sorted(word))
            if key in mem:
                mem[key].append(word)
            else:
                mem[key] = [word]
        result = []
        for key in mem:
            result.append(mem[key])
        return result

### test ###
s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))

strs = [""]
print(s.groupAnagrams(strs))

strs = ["a"]
print(s.groupAnagrams(strs))

