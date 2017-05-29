def blockPosition(num, block):
    if num not in block:
        return -1 ; 
    for i in range(0, len(block)):
        if block[i] == num:
            return i ; 
    return -1 ; 

# find the position of a number
def blockNum(num, blocks): 
    for i in range(0, len(blocks)):
        if num in blocks[i]:
            return i ; 
    return -1 ; # error.


def pile (act, numA, numB, blocks):
    nA = blockNum(numA, blocks) ; 
    nB = blockNum(numB, blocks) ; 
    if nA == nB:
        return ; 
    if nA == -1 or nB == -1:
        print("Error happen! when a=%d b=%d:" % (numA, numB)) ; 
        print(blocks) ; 
        quit() ; 
    pA = blockPosition(numA, blocks[nA]) ; 
    if act == "onto":
        restore(numB, blocks) ; 
    for i in range(pA, len(blocks[nA])):
        blocks[nB].append(blocks[nA][i]) ; 

    del blocks[nA][pA:] ; 

# print(blocks) ; # debug
    return ; 

# put all number on top of num back to initial positions.
def restore(num, blocks):
    n = blockNum(num, blocks) ; 
    p = blockPosition(num, blocks[n]) ; 
    for i in range(p+1, len(blocks[n])):
        num = blocks[n][i] ; 
        blocks[num].append(num) ; 
    del blocks[n][p+1:] ; 


def move(act, numA, numB, blocks):
    nA = blockNum(numA, blocks) ; 
    nB = blockNum(numB, blocks) ; 
    pA = blockPosition(numA, blocks[nA]) ; 
    pB = blockPosition(numB, blocks[nB]) ; 
    if nA == nB:
        return ; 
    # put all blocks on top of A back to initial positions.
    restore(numA, blocks) ; 
    if act == "onto":
        restore(numB, blocks) ; 
    blocks[nB].append(numA) ; 
    del blocks[nA][pA:] ; 

    return ; 

def printBlock(blocks):
    for i in range(0, len(blocks)):
        content = "" ; 
        for j in range(0, len(blocks[i])):
            content += (" " + str(blocks[i][j])) ; 
        print("%d:%s" % (i, content)) ; 

def process(cmd, act, numA, numB, blocks):
    if cmd == "move":
        move(act, numA, numB, blocks) ; 
    if cmd == "pile":
        pile(act, numA, numB, blocks) ;
    return ; 

def work():
    n = int(input()) ;
    blocks = [] ; 
    # initialize array
    for i in range(0, n):
        blocks.append([i]) ; 
#    print(blocks) ; # debug

    while True : 
        line = input() ;
        if line == "quit":
            printBlock(blocks) ; 
            return ; 
        cmd, numA, act, numB = line.split(" ") ; 
        numA = int(numA) ; 
        numB = int(numB) ; 
        process(cmd, act, numA, numB, blocks) ; 

def main():
    work();

if __name__ == "__main__":
    main() ; 
