

def readInput(directions, goals): # the name
    name = input() ; 
    if name == 'END':
        return 1 ;
    else:
        goals.append(name) ; 
    
    # the first line
    line = input().split() ; 
    start = ((int(line[0]), int(line[1])), 'START') ;
    end = ((int(line[3]), int(line[4])), 'END') ; 
    if line[2] == 'N':
        first = ((start[0][0]-1,start[0][1]), 'S') ;
    elif line[2] == 'S':
        first = ((start[0][0]+1,start[0][1]), 'N') ; 
    elif line[2] == 'W':
        first = ((start[0][0],start[0][1]-1), 'E') ; 
    elif line[2] == 'E':
        first = ((start[0][0],start[0][1]+1), 'W') ;
    goals.append(start) ; 
    goals.append(end) ; 
    goals.append(first) ; 
    # directions[start] = 'F';  
    
    # the rest lines
    line = input() ; 
    while line != '0':
        line = line.split() ; 
        point = (int(line[0]), int(line[1])) ;
        for i in range(2, len(line)):
            mark = line[i] ;
            if mark == '*':
                continue ; 
            else:
                directions[(point, translate(mark[0], ""))] = mark[1:] ; 
        line = input() ;
    return 0 ; 

def translate(direction, turn):
    answer = dict() ; 
    if turn == 'F':
        return direction ; 
    elif turn == "":
        answer = ['W', 'N', 'E', 'S'] ; 
        return answer[(answer.index(direction)+2)%len(answer)] ; 
    else:
        answer = ['W', 'N', 'E', 'S'] ; 
        return answer[(answer.index(direction)+(-1 if turn == 'L' else 1)) % len(answer)] ; 

def genPath(parents, child):
    # print("parents:", parents) ; # debug
    # print("child:", child) ; # debug
    path = [] ;
    
    path.insert(0, child[0]) ; 
    p = parents[child] ; 
    while p != None:
        path.insert(0, p[0]) ; 
        p = parents[p] ; 

    return path; 

def BFS(directions, start, first, end):
    path = [] ;
    
    parents = dict() ; # parnets is point=>point
    parents[first] = start; 
    parents[start] = None ;
    searched = set() ;  # point in the format is ((x,y), dirction)

    pointList = [] ; 
    pointList.append(first) ; 

    done = False ;
    while len(pointList) > 0 and not done:
        cur = pointList.pop(0) ; 

        # if the first one is already goal
        if cur[0] == end[0]:
            path = genPath(parents, cur) ; 
            return path ; 

        if cur in searched: # cur already been searched.
            continue ; 
        searched.add(cur) ;
        if cur not in directions.keys():
            continue ; 
        ds = directions[cur] ; 
        for d in ds: # there can be multiple directions for one point
            actualD = translate(cur[1], d) ; 
            child = ((0,0),'N') ;  #dummy
            if actualD == 'N':
                child = ((cur[0][0]+1, cur[0][1]), actualD) ; 
            elif actualD == 'S':
                child = ((cur[0][0]-1, cur[0][1]), actualD) ; 
            elif actualD == 'W':
                child = ((cur[0][0], cur[0][1]+1), actualD) ; 
            elif actualD == 'E':
                child = ((cur[0][0], cur[0][1]-1), actualD) ; 
            else:
                print("Error") ; 

            if not (child in parents.keys()):
                parents[child] = cur ; 
                # print("adding:", child, "turn:", d, " parent is:", parents[child]) ; # debug
            # print(parents) ;  # debug
                pointList.append(child) ; 

            if child[0] == end[0]:
                # print(parents) ;# debug
                path = genPath(parents, child) ;
                done = True ; 
                break ; 

    return path ; 

def work():
    # store the directions that a point can turn to
    # ex, 1 3 NL ER * => ((1,3),N)=>L, ((1,3),E)=>R
    directions = dict() ;
    variables = [] ; 
    if readInput(directions, variables) == 1:
        return 1 ; # end of program

    name = variables[0] ; 
    start = variables[1] ; 
    end = variables[2] ;
    first = variables[3] ; 

    # print(start, end, first) ; # debug
    
    path = BFS(directions, start, first, end) ; 
    print(name) ; 
    if len(path) == 0:
        print('  No Solution Possible') ; 
    else:
        result = "" ; 
        for i in range(1, len(path)+1):
            if i % 10 != 1:
                result += ' ' ;
            elif i % 10 == 1:
                result += '  ' ; 

            result += '('+str(path[i-1][0])+','+str(path[i-1][1])+')' ; 
            if i % 10 == 0 and i != len(path):
                result += '\n' ; 
        print(result) ; 

    return 0 ;


def main():
    Case = 1 ; 
    while work() == 0:
        Case += 1; 
    return ; 


if __name__ == "__main__":
    main() ; 
