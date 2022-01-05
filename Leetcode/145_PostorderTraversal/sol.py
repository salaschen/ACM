'''
Prob: 145 Binary Tree Post order traversal - Easy 
Author: Ruowei Chen
Date: 05/Jan/2022
Note:
    1) Recursive version is done.
    2) Iterative version is done.
'''

class Solution:
    # iterative
    def postorderTraversal(self, root: TreeNode) -> [int]:
        expanded = set()
        stack = [root]
        result = []
        while len(stack) > 0:
            cur = stack.pop()
            if cur is None:
                continue
            if cur in expanded:
                result.append(cur.val)
            else:
                stack.append(cur)
                stack.append(cur.right)
                stack.append(cur.left)
                expanded.add(cur)
        return result

    # recursive
    def postorderTraversal_recursive(self, root: TreeNode) -> [int]:
        if root is None:
            return []
        result = self.postorderTraversal(root.left)
        result = result + self.postorderTraversal(root.right)
        result = result + [root.val]
        return result

