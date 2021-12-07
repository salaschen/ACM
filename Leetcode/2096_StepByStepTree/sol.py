'''
Prob: Medium - Acceptance: 1757/5635
Author: Ruowei Chen
Date: 07/Dec/2021
Note:
    1) Change the find path function from recursive to iterative to avoid memory limit exceed
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def __init__(self):
        self.sPath = None 
        self.dPath = None
        self.start = None
        self.dest = None

    def getDirections(self, root: TreeNode, startValue:int, destValue: int) -> str:
        self.start = startValue
        self.dest = destValue
        self.findPath(root)
        sPath = self.sPath
        dPath = self.dPath
        slen, dlen = len(sPath), len(dPath)
        i = 0 
        while i < min(slen, dlen):
            if sPath[0] == dPath[0]:
                sPath = sPath[1:]
                dPath = dPath[1:]
                i += 1
            else:
                break
        result = ''
        for ch in sPath:
            result += 'U'
        result += dPath
        return result

    # change it
    def findPath(self, root: TreeNode) -> None:
        queue = [(root, '')]
        while self.sPath is None or self.dPath is None:
            node, path = queue.pop(0)
            if node is None:
                continue
            if node.val == self.start:
                self.sPath = path
            if node.val == self.dest:
                self.dPath = path
            queue.append((node.left, path+'L'))
            queue.append((node.right, path+'R'))
        return
           
### test ###
