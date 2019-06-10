'''
Note: 
    1) Copy leetcode user 'bupt_wc' idea. Sort all the available characters
    in order first, and record their positions in the original text. Then in the
    alphabetical order of the keys, try one by one, to see if the key can be inserted
    so that all other keys are still available in a later position.
    For example, 'cdadabcc' contains 'a','b','c','d'. Their positions are:
    a = [2,4], b = [5], c = [0,6,7], d = [1,3]. We try 'a' first, and its first
    position is 2, then we make sure all the other characters have a position after
    2. Which is the case. Then we pick 'a' first, and remove all the positions that are
    before 2 because they won't be available. Now we have b:[5],c:[6,7],d:[3]. 
    Now we try b, the first position is 5, but d doesn't have a position that's later
    than 5, so we cannot pick b. Same goes for c. So in this turn we pick 'd'. Then
    we pick 'b' and 'c' in that order. Answer is 'adbc'
'''

class Solution:
    def smallestSubsequenceWrong(self, text):
        result = '' ; 
        for i in range(len(text)-1, -1, -1): 
            c = text[i] ; 
            if c not in result:
                result = c + result  ;
            else:
                ind = result.index(c) ; 
                temp = c + result[:ind] + result[ind+1:]  ; 
                if temp < result:
                    result = temp ; 
        rresult = '' ; 
        for c in text:
            if c not in rresult:
                rresult += c ; 
            else:
                ind = rresult.index(c) ; 
                temp = rresult[:ind]+rresult[ind+1:]+c ; 
                if temp < rresult:
                    rresult = temp ; 
        return min(rresult, result) ; 

    def smallestSubsequence(self, text):
        # create positions for all the keys.
        pos = dict() ; 
        for i in range(0, len(text)):
            c = text[i] ;
            if c not in pos:
                pos[c] = [] ; 
            pos[c].append(i) ; 

        # sort the keys
        keys = sorted(pos.keys()) ;

        # go through the key in alphabetical order.
        result = "" ;
        while len(keys) > 0:
            curKey = None ; 
            curPos = None ;
            for i in range(0, len(keys)):
                curKey = keys[i] ; 
                curPos = pos[curKey][0] ;
                # check if all other keys have positions that later than this key.
                if len(list(filter(lambda key: pos[key][-1] < curPos, keys))) == 0:
                    result += curKey ; 
                    break ;

            # remove the selected key
            keys.remove(curKey) ; 

            # remove all the positions that's before the curPos.
            for key in keys:
                while len(pos[key]) > 0:
                    if pos[key][0] < curPos:
                        pos[key].pop(0) ; 
                    else:
                        break ;

        # end while loop and return     
        return result ; 


# test 
def main():
    s = Solution() ; 
    texts = ['cdadabcc', 'abcd', 'ecbacba', 'leetcode', 'ddeeeccdec',\
            'cbaacabcaaccaacababa', \
            'acfdfdgaadgfacfgffeddeddaadfdcbegaeecfafffdecgeebd'] ;

    for text in texts:
        print('Input: {0}'.format(text)) ; 
        print('Output: {0}\n'.format(s.smallestSubsequence(text))) ; 

    return ;

if __name__ == "__main__":
    main() ;
