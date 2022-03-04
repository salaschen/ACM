'''
Prob: 290 Word Pattern - Easy
Author: Ruowei Chen
Date: 04/Mar/2022
'''
class Solution():
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        mem = dict()
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            ch = pattern[i]
            if ch in mem:
                mem[ch].append(i)
            else:
                mem[ch] = [i]

        for key in mem.keys():
            matches = mem[key]
            first = matches[0]
            for j in range(1, len(matches)):
                pos = matches[j]
                if words[first] != words[pos]:
                    return False

        keys = list(mem.keys())
        for i in range(len(keys)):
            k1 = keys[i]
            w1 = words[mem[k1][0]]
            for j in range(i+1, len(keys)):
                k2 = keys[j]
                w2 = words[mem[k2][0]]
                if w1 == w2:
                    return False


        return True

### test ###
sol = Solution()
pattern, s = 'abba', 'dog cat cat dog'
print(sol.wordPattern(pattern, s))

pattern, s = 'abba', 'dog cat cat fish'
print(sol.wordPattern(pattern, s))

pattern, s = 'aaaa', 'dog cat cat dog'
print(sol.wordPattern(pattern, s))

pattern, s = 'abba', 'dog dog dog dog'
print(sol.wordPattern(pattern, s))

pattern, s = 'aaa', 'aa aa aa aa'
print(sol.wordPattern(pattern, s))


