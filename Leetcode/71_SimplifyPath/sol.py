class Solution:
    def simplifyPath(self, path: str) -> str:
        names = ['']
        plen = len(path)
        i = 0;
        while True:
            if i >= plen:
                break 

            # Read '/'
            while i < plen and path[i] == '/':
                i += 1

            if i >= plen:
                break 

            name = ''
            while i < plen and path[i] != '/':
                name += path[i]
                i += 1
            
            if name == '.':
                continue
            elif name == '..':
                if len(names) > 0:
                    names.pop()
            else:
                names.append(name)

        result = '/'.join(names)

        if len(result) == 0:
            return '/'
        else:
            if result[0] != '/':
                result = '/' + result
            return result

### test ###
s = Solution()
path = '/home/'
print(s.simplifyPath(path))

path = '/../'
print(s.simplifyPath(path))

path = '/home/.//../foo/../'
print(s.simplifyPath(path))

path = '/home//foo/../'
print(s.simplifyPath(path))

path = "/a/./b/../../c/"
print(s.simplifyPath(path))

path = "/a/../../b/../c//.//"
print(s.simplifyPath(path))

path = "/home/../../.."
print(s.simplifyPath(path))

