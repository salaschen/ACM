'''
Prob: Leetcode 1382 - Balance a Binary Search Tree - Medium
Author: Ruowei Chen
Date: 16/Mar/2020
'''

from BST import *

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = sorted(self.getValue(root))
        root = self.getSubTree(values, 0, len(values)-1)
        return root
    
    # from and to are inclusive
    def getSubTree(self, values, frm: int, to:int) -> TreeNode:
        # boundary check
        if frm > to: return None
        # if there is only one value.
        if frm == to: return TreeNode(values[frm])
        
        # multiple values.
        mid = (to+frm)//2
        root = TreeNode(values[mid])
        root.left = self.getSubTree(values, frm, mid-1)
        root.right = self.getSubTree(values, mid+1, to)
        return root

    def getValue(self, root: TreeNode):
        queue = [root]
        result = []
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur is not None:
                result.append(cur.val)
                queue += [cur.left, cur.right]
        return result


###### test ######
arr = [1,None, 2, None, 3, None, 4, None, None]
root = GenBST(arr)

s = Solution()
print(s.balanceBST(root))

