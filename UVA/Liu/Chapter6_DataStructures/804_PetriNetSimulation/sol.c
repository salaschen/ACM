#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Transition
{
    int Input[101] ; 
    int Output[101] ; 
    int pnum; 
} Transition ; 

int places[101] ;
Transition transitions[101] ; 

int IsEnable(Transition *tr, int * places) {
    // return 0 if ok, 1 if not enable.
    int i  ;
    for (i=1 ; i <= tr-> pnum ; i++) {
        if (tr->Input[i] > places[i]) {
            return 1 ; 
        }
    }
    return 0 ; 
}

void Fire(Transition * tr, int * places) {
    int i ; 
    for (i=1 ; i <= tr->pnum ; i++) {
        places[i] -= tr->Input[i] ; 
        places[i] += tr->Output[i] ; 
    }
}

int TryFireEvent(int * places, int tnum, int pnum) { 
    // return 0 if Can file, 1 if not.
    int i ; 
    for (i=0 ; i < tnum ; i++) {
        Transition * tr = &transitions[i] ;
        if (IsEnable(tr, places) == 0) {
            Fire(tr, places) ; 
            return 0 ; 
        }
    }
    return 1 ; 
}

int work(int Case)
{
    int pnum ; 
    scanf("%d", &pnum) ; 
    if (pnum == 0)
        return 1 ; 
    int i ; 
    places[0] = 0 ; 
    for (i=0 ; i < pnum ; i++) {
        scanf("%d", &places[i+1]) ;
    }
    
    int tnum ; 
    scanf("%d", &tnum) ; 
    int cur = 0 ; 
    while (cur < tnum) {
        Transition * curTran = &transitions[cur] ; 
        memset(curTran->Input, 0, sizeof(int)*101) ; 
        memset(curTran->Output, 0, sizeof(int)*101) ; 
        int temp ; 
        curTran->pnum = pnum ;
        scanf("%d", &temp) ; 
        while (temp != 0) {
            if (temp < 0) {
                curTran->Input[-1*temp] += 1 ; 
            }
            else if (temp > 0) {
                curTran->Output[temp] += 1 ; 
            }
            scanf("%d", &temp) ; 
        }
        cur += 1 ; 
    }
    
    int rounds ;
    scanf("%d", &rounds) ; 

    int survived = -1 ; 
    for (i = 0 ; i < rounds ; i++) {
        int result = TryFireEvent(places, tnum, pnum) ; 
        if (result == 1) {
            survived = i ; 
            break ;
        }
    }

    if (survived >= 0)
    {
        printf("Case %d: dead after %d transitions\n", Case, survived) ; 
    }
    else {
        printf("Case %d: still live after %d transitions\n", 
                Case, rounds) ; 
    }
    printf("Places with tokens:") ; 
    for (i=0 ; i <= pnum ; i++) {
        if (places[i] > 0) {
            printf(" %d (%d)", i, places[i]) ; 
        }
    }
    printf("\n\n") ; 
    return 0 ; 
}


int main()
{
    int Case = 1 ; 
    while (work(Case) == 0) {
        Case += 1 ;
    }
    return 0 ;
}
