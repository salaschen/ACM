class Solution:
    def findSubstring(self, s: str, words:[str]) -> [int]:
        if len(s) == 0 or len(words) == 0:
            return []
        wordMap= dict() # str -> int (word count)
        for word in words:
            if word not in wordMap:
                wordMap[word] = 0
            wordMap[word] += 1

        subLen = len(words) * len(words[0])
        wlen = len(words[0])
        result = []

        for i in range(len(s)-subLen+1):
            substring = s[i:i+subLen]
            subMap = dict()
            # add each word
            pos = 0
            while pos < subLen:
                w = substring[pos:pos+wlen]
                if w not in subMap:
                    subMap[w] = 0
                subMap[w] += 1
                pos += wlen

            # now compare the submap with word map
            isSubstring = True
            # print(subMap) # debug
            for key in wordMap:
                if key not in subMap or wordMap[key] != subMap[key]:
                    isSubstring = False
                    break
            if isSubstring:
                result.append(i)
        return result
                
###### test ######
s = Solution()
string = "barfoothefoobarman"
words = ["foo", "bar"]
print(s.findSubstring(string, words))
string = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(s.findSubstring(string, words))
