'''
UVa 12118 - AM/ICPC Dhaka 2007 - Inspector's Dilemma.
Date: 18/Nov/2018
Author: Ruowei Chen
'''

class Path:

    def __init__(self):
        self.degree = dict() ; # int => int (number of degrees for each node)
        self.start = None ; 
        self.end = None ; 
        return ; 
    
    def __str__(self):
        return str(self.degree) ; 

    def HalfDegree(self):
        for k in self.degree.keys():
            self.degree[k] = self.degree[k]//2;
        return ; 

    def MakeEulerPath(self): # add extra edges if needed to make Euler path
        # get a list of nodes that have odd degrees
        oddNodes = [] ; 
        allKeys = list(self.degree.keys()) ; 
        # print('print path:', str(self)) ; # debug
        for v in allKeys:
            if self.degree[v] % 2 == 1:
                oddNodes.append(v) ; 
        if len(oddNodes) % 2 == 1:
            print("number of odd nodes should not be odd") ; 
            raise Exception ; 
        if len(oddNodes) == 0: # already an Euler path
            self.start = allKeys[0];   # randomly choose a start and end
            self.end = allKeys[1] ; 
            return ; 
        else:
            self.start = oddNodes.pop() ; 
            self.end = oddNodes.pop() ; 
            while len(oddNodes) > 0:
                v1 = oddNodes.pop() ; 
                v2 = oddNodes.pop() ; 
                self.degree[v1] += 1 ; 
                self.degree[v2] += 1 ; 
        return ; 

    def AddEdge(self, edge): # edge is a tuple (int, int)
        v1, v2 = edge ; 
        if v1 not in self.degree:
            self.degree[v1] = 0 ; 
        if v2 not in self.degree:
            self.degree[v2] = 0 ; 
        self.degree[v1] += 1 ;
        self.degree[v2] += 1 ; 
        return ;

    def MergePath(self, path2):
        self.MakeEulerPath() ; 
        path2.MakeEulerPath() ; 
        # add keys from path2 to self
        for k in path2.degree.keys():
            if k not in self.degree:
                self.degree[k] = path2.degree[k] ; 
            else:
                self.degree[k] += path2.degree[k] ; 
        # connect the start to start
        self.degree[self.start] += 1 ; 
        self.degree[path2.start] += 1 ; 
        self.start = self.end ; 
        self.end = path2.end ; 
        return ;


    def GetNumEdges(self):
        result = 0 ; 
        for k in self.degree.keys():
            result += self.degree[k] ;
        return result//2

def GetPath(edges):
    if len(edges.keys()) == 0:
        return None ; 
    path = Path() ;
    queue = [list(edges.keys())[0]] ;
    while len(queue) > 0:
        v1 = queue.pop() ; 
        if v1 not in edges:
            continue ; 
        else:
            for v2 in edges[v1]:
                path.AddEdge((v1, v2)) ; 
                queue.append(v2) ; 
            edges.pop(v1) ; 
        continue ;
    path.HalfDegree() ; # because the same edge is added twice
    return path ;

def work(Case):
    V,E,T = [int(n) for n in input().split()] ;
    if V == 0 and E == 0 and T == 0:
        return 1 ; 

    if E == 0:
        print('Case {0}: {1}'.format(Case, 0)) ; 
        return 0 ;

    # read in the edges
    edges = dict() ; # int => set<int>
    for i in range(E):
        a,b = [int(n) for n in input().split()] ; 
        if a not in edges:
            edges[a] = set() ; 
        if b not in edges:
            edges[b] = set() ; 
        edges[a].add(b) ; 
        edges[b].add(a) ; 

    # print('edges:', edges) ; # debug

    # Generate disconnected paths
    PathList = [];    
    while len(edges.keys()) > 0:
        path = GetPath(edges) ; 
        PathList.append(path) ;

    mainPath = PathList.pop() ; 
    mainPath.MakeEulerPath() ;
    while len(PathList) > 0:
        path = PathList.pop() ; 
        mainPath.MergePath(path) ; 
    
    print('Case {0}: {1}'.format(Case, mainPath.GetNumEdges() * T)) ; 
    return 0 ;


def solve():
    Case = 1 ; 
    while work(Case) == 0:
        Case += 1 ; 
    return ;

def main():
    solve() ; 
    return ; 

if __name__ == "__main__":
    main() ;
