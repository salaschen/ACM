'''
Prob: 102 Level Order Traversal - Medium
Author: Ruowei Chen
Date: 05/Jan/2022
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        result = []
        expand = [root]
        while len(expand) > 0:
            temp = []
            value = []
            for node in expand:
                if node is None:
                    continue
                temp = temp + [node.left, node.right]
                value.append(node.val)
            if len(value) > 0:
                result.append(value)
            value = []
            expand = temp
        return result
