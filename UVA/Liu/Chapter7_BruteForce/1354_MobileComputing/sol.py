'''
UVa 1354 Mobile Computing, ACM/ICPC Tokyo 2005
Note: Brute Force DFS
Date: 01/Dec/2018
'''

class Node:
    def __init__(self, value=None):
        self.value = value ; 
        self.parent = None ; 
        self.left = None ; 
        self.right = None ; 
        self.pos = None ; 

    def __str__(self):
        result = '[node]: value={0}, pos={4},  parent={1}, left={2}, right={3}\n'\
            .format( self.value, \
            self.parent.value if self.parent else 'None', \
            self.left.value if self.left else 'None', \
            self.right.value if self.right else 'None', \
            self.pos) ;
        if self.left:
            self.left.parent = self ; 
            result += str(self.left) ; 
        if self.right:
            self.right.parent = self ; 
            result += str(self.right) ; 
        return result ; 

    def setChildPos(self): # set its children's positions repective to it's own 
        if self.pos is None or self.left is None or self.right is None:
            return ; 
        lw, rw = self.left.value, self.right.value ; 
        ll, rl = rw/(lw+rw), lw/(lw+rw) ;  # lengths
        self.left.pos = self.pos - ll ;
        self.right.pos = self.pos + rl ;
        return ;
            
    def endPoints(self): 
        # get the left and right most end points of it's childrens
        # return as a tuple (left, right)
        if self.left is None or self.right is None:
            return (self.pos, self.pos) ; 
        else:
            self.setChildPos() ;
            lends = self.left.endPoints(); 
            rends = self.right.endPoints() ; 
            return (min(lends[0], rends[0]), max(lends[1], rends[1]))  ; 

def solve():
    main() ; 

def search(nodes):
    if len(nodes) == 1:
        nodes[0].pos = 0 ; 
        left, right = nodes[0].endPoints() ; 
        return [abs(right-left)] ; 
    else:
        result = [] ;
        for i in range(0, len(nodes)):
            for j in range(0, len(nodes)):
                if i == j: 
                    continue ; 
                nodecopy = nodes[:] ; 
                v1 = nodecopy[i] ; 
                v2 = nodecopy[j] ; 
                nodecopy.remove(v1) ; nodecopy.remove(v2) ;
                newNode = Node(v1.value+v2.value) ; 
                v1.parent = newNode ; v2.parent = newNode ; 
                newNode.left = v1 ; 
                newNode.right = v2 ; 
                nodecopy.append(newNode) ; 
                temp = search(nodecopy) ;
                result.extend(temp) ; 
        return result ; 

def work(room, data):
    # print('data:', data) ; # debug
    nodes = [Node(n) for n in data] ; 
    # dfs on the nodes
    widths = search(nodes) ; 

    result = -1 ; 
    for w in widths:
        if w < room and w > result:
            result = w ; 
    print(result) ; 
    return ; 

def main():
    N = int(input()) ; 
    for i in range(N):
        data = [] ;
        room = float(input()) ; 
        num = int(input()) ; 
        for j in range(num):
            data.append(int(input())) ; 
        work(room, data) ; 
    return 0 ;

if __name__ == "__main__":
    solve() ;
