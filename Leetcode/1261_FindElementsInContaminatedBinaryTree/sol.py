'''
Prob: Leetcode 1261 - Find Elements in a Contaminated Binary Tree.
Date: 17/Nov/2019
Author: Ruowei Chen
'''
class TreeNode:
    def __init__(self, x):
        self.val = x ; 
        self.left = None ; 
        self.right = None ; 
    
class FindElements:
    def __init__(self, root: TreeNode):
        # restore the contaminated treeNode
        root.val = 0 ; 
        self.valueSet = set() ; 
        self.restoreNode(root, self.valueSet) ; 
    
    def restoreNode(self, node, valueSet):
        # assume the value of this node is restored before the call.
        if node.left is not None:
            node.left.val = 2 * node.val + 1 ; 
            valueSet.add(node.left.val) ; 
            self.restoreNode(node.left, valueSet) ; 
        if node.right is not None:
            node.right.val = 2 * node.val + 2 ; 
            valueSet.add(node.right.val) ; 
            self.restoreNode(node.right, valueSet) ; 
        return ;
    
    def find(self, target: int) -> bool:
        return target in self.valueSet ; 