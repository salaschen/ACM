class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # use a list to keep track of the index to be deleted.
        delete = []

        # use a stack to keep the index of unused '('
        left = []
        
        for i in range(len(s)):
            ch = s[i]
            if ch == ')':
                if len(left) == 0:
                    # this ')' is to be deleted
                    delete.append(i)
                else:
                    # the most recent '(' is consumed
                    left = left[:-1]
            elif ch == '(':
                left.append(i)
            
        # any unmatched ")" and unused "(" are to be deleted
        delete = set(delete + left)
        result = ''
        for i in range(len(s)):
            if i in delete:
                continue
            else:
                result += s[i]
        return result
        
### test ###
sol = Solution()
s = "lee(t(c)o)de)"
print(sol.minRemoveToMakeValid(s))
s = "a)b(c)d"
print(sol.minRemoveToMakeValid(s))

s = "))(("
print(sol.minRemoveToMakeValid(s))


