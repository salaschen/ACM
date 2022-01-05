'''
Prob: 94 - Binary Tree Inorder Traversal - Easy
Author: Ruowei Chen
Date: 05/Jan/2022
Note:
    1) Recursive version is done
    2) Iterative version is done
'''
class Solution:
    # iterative
    def inorderTraversal(self, root: TreeNode) -> [int]:
        stack = [root]
        result = []
        expanded = set()
        while len(stack) > 0:
            cur = stack.pop()
            if cur is None:
                continue
            if cur in expanded:
                result.append(cur.val)
            else:
                stack.append(cur.right)
                stack.append(cur)
                stack.append(cur.left)
                expanded.add(cur)
        return result


    # recursive
    def inorderTraversal_recursive(self, root: TreeNode) -> [int]:
        if root is None:
            return []
        result = self.inorderTraversal(root.left)
        result = result + [root.val]
        result = result + self.inorderTraversal(root.right)
        return result

