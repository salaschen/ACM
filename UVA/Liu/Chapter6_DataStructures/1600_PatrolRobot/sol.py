def work():
    m, n = [int(x) for x in input().split()] ;
    k = int(input()) ; 
    matrix = [] ;
    for i in range(0, m):
        row = [int(x) for x in input().split()] ;
        matrix.append(row) ; 
    # print(matrix) ; # debug
    print(BFS(matrix, (1,1), (m,n), k)) ; 
    return ; 

def BFS(matrix, src, target, k):
    m, n = target ;
    queue = [(src, 0, 0)] ; 
    searched = set() ; 
    turboDict = dict() ; 
    while len(queue) > 0:
        cur, step, turbo = queue.pop(0) ; 
        if cur[0] == target[0] and cur[1] == target[1]:
            return step ; 
        ne = GetNextPos(cur, m, n) ; 
        for nn in ne:
            if nn not in searched:
                if matrix[nn[0]-1][nn[1]-1] == 0:
                    queue.append((nn, step+1, 0)) ; 
                    searched.add(nn) ;
                    turboDict[nn] = 0 ; 
                elif turbo+1 <= k:
                    queue.append((nn, step+1, turbo+1)) ; 
                    searched.add(nn) ; 
                    turboDict[nn] = turbo+1 ; 
            else: # nn in searched.
                if nn in turboDict and turbo+1 < turboDict[nn]:
                    turboDict[nn] = turbo+1 ; 
                    queue.append((nn, step+1, turbo+1)) ;

    return -1 ; 

def GetNextPos(cur, m,n):
    result = [(cur[0]+1,cur[1]), \
              (cur[0],cur[1]+1), \
              (cur[0]-1,cur[1]), \
              (cur[0], cur[1]-1)] ; 
    # print('cur:{0}, m:{1}, n:{2}'.format(cur, m, n)) ; # debug
    return list(filter(lambda pair: \
            pair[0] >= 1 and pair[0] <= m and
            pair[1] >= 1 and pair[1] <= n, result)) ;

def main():
    num = int(input()) ; 
    for i in range(num):
        work() ; 

if __name__ == "__main__":
    main() ; 
