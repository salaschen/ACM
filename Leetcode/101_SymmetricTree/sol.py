'''
Prob: 101 - Symmetric Tree
Author: Ruowei Chen
Date: 05/Jan/2022
Note:
    1) *wrong* in order walk then compare the result array.
    2) Test both sub-trees were symmetrical
'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        # both subtrees are None
        if left is None and right is None:
            return True

        # only one of the subtree is None
        if left is None or right is None:
            return False

        return left.val == right.val and self.isMirror(left.left, right.right) \
                and self.isMirror(left.right, right.left)
