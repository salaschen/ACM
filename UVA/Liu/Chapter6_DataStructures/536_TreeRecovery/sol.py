def work(pred, inord):
    return transform(pred, inord) ; 

def transform(pred, inord):
    if len(pred) == 0 and len(inord) == 0:
        return "" ; 
    if len(pred) == 1 and len(inord) == 1:
        return pred ;
    root = pred[0] ; 
    leftLen = inord.find(root) ; 
    rightLen = len(pred) - 1 - leftLen ;
    left = transform(pred[1:leftLen+1], inord[:leftLen]) ; 
    right = transform(pred[leftLen+1:], inord[leftLen+1:]) ; 
    return left+right+root ; 

def main():
    
    try:
        while True:    
            pred, inord = input().split() ; 
            print(work(pred, inord)) ; 
    except:
        return ; 

if __name__ == "__main__":
    main() ; 
