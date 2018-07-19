class TreeNode:
    def __init__(self, x):
        self.val = x ;
        self.left = None ; 
        self.right = None ; 

    def __str__(self):
        result = "root:{0} => left:{1}, right:{2}".format(self.val, \
                self.left.val if self.left != None else "null", \
                self.right.val if self.right != None else "null") ; 
        if self.left != None:
            result += "\n" + str(self.left) ; 

        if self.right != None: 
            result += "\n" + str(self.right) ; 
        return result ; 

def ReadTreeNode(nodeList):
    '''
        Parameter:nodeList : List<string> [3,9,20,null,null,15,7] for example.
        Return: The root node.
    '''
    treeNodes = dict() ; 
    for i in range(0, len(nodeList)):
        cur = nodeList[i] ; 
        if cur == 'null':
            continue ;
        parent = (i-1)//2 ;            
        curNode = TreeNode(cur) ;
        treeNodes[i] = curNode ; 
        try:
            print("cur:{0},parent:{1}".format(i, parent)) ; # debug
            parentNode = treeNodes[parent] ; 
            if i % 2 == 1:
                parentNode.left = curNode ; 
            else:
                parentNode.right = curNode ;
        except:
             print("Exception!"); # do not need to do anything.

    return treeNodes[0] ; 

class Solution:
    def zigzagLevelOrder(self,root):
        
        if root == None: 
            return [] ;
        result = [] ;
        Queue = [root] ; # all the nodes in queue are printed already.
        level = 0 ; 
        while len(Queue) != 0:
            level += 1 ;
            size = len(Queue) ; 
            row = [0 for x in range(0, size)] ; 
            for i in range(0, size):
                node = Queue[0] ; 
                Queue.pop(0); 
                if level % 2 == 1:
                    row[i] = node.val ; 
                else:
                    row[size-i-1] = node.val ; 
                if node.left != None:
                    Queue.append(node.left) ; 
                if node.right != None:
                    Queue.append(node.right) ;

            result.append(row) ; 
        return result ; 
    


if __name__ == "__main__":
    nodeList = ['0','2','4','1','null','3','-1','5','1','null','6','null','8'] ; 
    root = ReadTreeNode(nodeList); 
    # print(root) ; 

    s = Solution() ; 
    result = s.zigzagLevelOrder(root) ; 
    print("result: {0}".format(result)) ; 



