'''
Prob: 144 Binary Tree Preorder Traversal - Easy
Author: Ruowei Chen
Dat: 05/Jan/2022
Note:
    1) Recursive version is done
    2) Iterative version is done
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # iterative
    def preorderTraversal(self, root: TreeNode) -> [int]:
        stack = [root]
        result = []
        while len(stack) > 0:
            cur = stack.pop()
            if cur is None:
                continue
            result.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
        return result

    # recursive
    def preorderTraversal_recursive(self, root: TreeNode) -> [int]:
        if root is None:
            return []
        result = [root.val]
        result = result + self.preorderTraversal(root.left)
        result = result + self.preorderTraversal(root.right)
        return result

