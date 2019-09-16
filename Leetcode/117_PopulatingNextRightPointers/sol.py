'''
Prob: Leetcode 117 - Populating Next Right Pointers in Each Node II
Date: 16/Sep/2019
Author: Ruowei Chen
Note: 
    1) First just read the nodes from an array into a tree.
'''
class Node:
    def __init__(self, val, left, right, next):
        self.val = val ; 
        self.left = left ; 
        self.right = right ; 
        self.next = next ; 

class Solution:
    def connect(self, root):
        self.createLink(None, root) ; 
        return root;

    # helper function, locate right neighbor's child.
    def rightNeighborChild(self, parent):
        if parent is None or parent.next is None:
            return None ; 
        
        neighbor = parent.next ; 
        if neighbor.left is not None:
            return neighbor.left ;
        if neighbor.right is not None:
            return neighbor.right ; 
        
        # when neighbor has no child, try to find the next right neighbor.
        # in a recursive fashion.
        return self.rightNeighborChild(neighbor) ;

    # create right link for a specific node
    def createLink(self, parent, node):
        if node is None:
            return ;

        # if the node has no parent, then it's a root node
        # which means it's impossible to have next node.
        if parent is None:
            node.next = None ; 

        # check first to see if this node has a right sibling.
        elif parent.right != node and parent.right is not None:
            node.next = parent.right ; 

        # find the right neighbor of the parentNode and try to find the first child node
        # of the right neighbor of the parentNode.
        # if there's None, then find the next right neighbor, and so on.
        else:
            node.next = self.rightNeighborChild(parent) ; 
        
        # now create link for its child node, start from the right branch.
        self.createLink(node, node.right) ; 
        self.createLink(node, node.left) ; 
        return ;


# return the root node of the tree
# for debug purposes
def getNode(nodeList, index, nodeListLength):
    if index >= nodeListLength:
        return None ; 
    if nodeList[index] is None:
        return None ; 
    # populating fields
    val = nodeList[index] ; 
    l,r = 2*index+1, 2*index+2 ; 
    left = getNode(nodeList, l, nodeListLength) ; 
    right = getNode(nodeList, r, nodeListLength) ; 
    result = Node(val, left, right, None) ; 
    return result ; 

def readTree(nodeList):
    nodeListLength = len(nodeList) ; 
    root = getNode(nodeList, 0, nodeListLength) ; 
    return root ; 

def printNode(node, spaceNum=0):
    indent = ' ' * spaceNum ; 
    if node is None:
        print(indent+'None') ; 
    else:
        left = 'None' if node.left is None else node.left.val ; 
        right = 'None' if node.right is None else node.right.val ; 
        next = 'null' if node.next is None else node.next.val ; 
        print(indent+'Node: {0},left:{1},right:{2},next:{3}'\
                .format(node.val, left, right, next)) ; 
        printNode(node.left, spaceNum+2) ; 
        printNode(node.right, spaceNum+2) ; 
    return ;

def printTree(root):
    printNode(root) ; 

def testReadTree():
    nodeList = [1,2,3,4,5,None,7] ;
    root = readTree(nodeList) ; 
    printTree(root) ; 
    return ;

def testSolution():
    s = Solution() ; 
    nodeList = [1,2,3,4,5,None,7,8,None,None,9,None,None,None,\
            10,11,None,None,None,None,None,None,None,None,None,None,None,None,None,None,\
            12] ; 
    root = readTree(nodeList) ; 
    s.connect(root) ; 
    printTree(root) ; 
    return ;

def test():
    # testReadTree() ; 
    testSolution() ;
    return ;

def main():
    test() ; 
    return ;


if __name__ == "__main__":
    main() ; 


