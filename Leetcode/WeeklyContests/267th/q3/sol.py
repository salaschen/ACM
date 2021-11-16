'''
Prob: 2075 Medium
Author: Ruowei Chen
Date: 16/Nov/2021
'''
class Solution:
    def decodeCiphertext(self, encodedText: str, rows:int) -> str:
        rowSize = len(encodedText)//rows
        if len(encodedText) == 0:
            return ""

        textRows = []
        start, end = 0, rowSize
        for i in range(rows):
            textRows.append(list(encodedText[start:end]))
            start, end = end, end + rowSize
        # print(textRows) # debug
        cols = len(textRows[0])
        result = ""
        r, c = 0, 0 # start from the top left
        while True:
            result += textRows[r][c] 
            if c == cols-1 and r == 0: # reach the last character
                break
            elif r == rows-1:
                c = c - r + 1
                r = 0
            elif c == cols-1:
                c = c - r + 1
                r = 0
            else:
                r = r + 1
                c = c + 1

        return result.rstrip()

### test ###
s = Solution()
encodedText = "ch   ie   pr"
rows = 3
print(s.decodeCiphertext(encodedText, rows))

encodedText = "iveo    eed   l te   olc"
rows = 4
print(s.decodeCiphertext(encodedText, rows))

encodedText = "coding"
rows = 1
print(s.decodeCiphertext(encodedText, rows))

encodedText = " b  ac"
rows = 2
print(s.decodeCiphertext(encodedText, rows))

