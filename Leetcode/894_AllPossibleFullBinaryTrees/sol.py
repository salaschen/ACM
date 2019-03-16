class TreeNode:
    def __init__(self, x):
        self.val = x ; 
        self.left = None ; 
        self.right = None ;

    def __str__(self):
        valueList = [] ; 
        nodeList = [self];
        while len(list(filter(lambda n: n is not None, nodeList))) > 0:
            cur = nodeList.pop(0) ; 
            if cur is None:
                valueList.append("null") ; 
            else:
                valueList.append(str(cur.val)) ; 
                nodeList.append(cur.left) ; 
                nodeList.append(cur.right) ; 
        return str(valueList) ; 

class Solution:
    def __init__(self):
        self.TreeList = dict() ; 

    def allPossibleFBT(self, N: int) :
        if N in self.TreeList:
            return self.TreeList[N] ;

        if N == 0:
            self.TreeList[0] = [] ; 
            return self.TreeList[0] ; 
        
        if N == 1:
            self.TreeList[1] = [TreeNode(0)] ;
            return self.TreeList[1] ; 
        
        leftNum = 1 ; 
        result = [] ; 
        while leftNum <= N-2:
            rightNum = N-1-leftNum ; 
            leftList = self.allPossibleFBT(leftNum) ; 
            rightList = self.allPossibleFBT(rightNum) ; 
            for l in leftList:
                for r in rightList:
                    root = TreeNode(0) ; 
                    root.left = l ; 
                    root.right = r ; 
                    result.append(root) ; 
            leftNum += 2 ; 

        self.TreeList[N] = result ; 
        return self.TreeList[N] ; 

if __name__ == "__main__":
    s = Solution() ; 
    result = s.allPossibleFBT(15) ; 
    for node in result:
        print(node) ; 
