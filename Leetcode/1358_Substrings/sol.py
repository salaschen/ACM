class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        at, bt, ct = [], [], []
        for i in range(0, len(s)):
            if s[i] == 'a':
                at.append(i)
            elif s[i] == 'b':
                bt.append(i)
            else:
                ct.append(i)
        count = 0
        alen, blen, clen = len(at), len(bt), len(ct)
        curLen = len(s)
        while alen > 0 and blen > 0 and clen > 0:
            pos = min([at[alen-1], bt[blen-1], ct[clen-1]])
            popn = max([at[alen-1],bt[blen-1], ct[clen-1]])
            count += (pos + 1)
            '''
            if at[alen-1] == popn:
                at.pop()
                alen -= 1
            elif bt[blen-1] == popn:
                bt.pop()
                blen -= 1
            else:
                ct.pop()
                clen -= 1
            '''
            if s[curLen-1] == 'a':
                alen -= 1
            elif s[curLen-1] == 'b':
                blen -= 1
            else:
                clen -= 1
            curLen -= 1
        return count

####### test ########3
s = Solution()
a = "abcabc"
print(s.numberOfSubstrings(a))

