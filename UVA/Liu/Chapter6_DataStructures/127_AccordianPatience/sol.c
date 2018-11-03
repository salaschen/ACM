#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TRUE 0
#define FALSE 1

typedef struct Pile
{
    int id ;
    char cards[52][3] ;
    int numCard ; 
    struct Pile * prev ; 
    struct Pile * next ; 
} Pile ; 

// Prototypes
void AddCardToPile(Pile * pile, char* Card); 
void PopCardToPile(Pile * pile, char * buf) ; 
void ResetPiles(void) ;
int CardMatch(char * c1, char * c2) ; 
void MoveCard(Pile * p1, Pile *p2) ; // Move Card from p1 to p2
void PrintPile(Pile * pile) ; 
void PrintStack(Pile * start) ; // print the whole card stack beginning from pile
void TestMoveCard(void) ; 
Pile * Left (Pile * pile, int num) ; 
int PileMatch(Pile * p1, Pile * p2) ;
char * TopCardInPile(Pile * pile) ;
void ProcessPiles(void) ; 
void PrintResult(void) ;


// Sub-Routines
Pile piles[52] ;

void 
AddCardToPile(Pile * pile, char* Card)
{
    char * place = (char *)(pile->cards) + sizeof(char)*3*(pile->numCard) ; 
    memcpy(place, Card, sizeof(char)*2) ; 
    pile->numCard ++ ; 
}

void
PopCardToPile(Pile * pile, char * buf)
{
    char * place = pile->cards[pile->numCard-1] ; 
    memcpy(buf, place, sizeof(char)*3) ; 
    pile->numCard -= 1;
}

void 
ResetPiles()
{
    int i ; 
    for (i=0 ; i < 52 ; i++) {
        piles[i].id = i ;
        piles[i].numCard = 0 ; 
        memset(piles[i].cards, 0, sizeof(char)*52*3) ; 
        if (i > 0) {
            piles[i].prev = &piles[i-1] ; 
        }
        if (i < 51) {
            piles[i].next = &piles[i+1] ; 
        }
    }
    piles[0].prev = NULL ; 
    piles[51].next = NULL ;
}

int
CardMatch(char * c1, char * c2)
{
    if (c1[0] == c2[0] || c1[1] == c2[1]) 
        return TRUE ; 

    return FALSE ; 
}

void
PrintPile(Pile * pile)
{
    printf("Pile[%d]: %d cards in pile\n", pile->id, pile->numCard) ; 
    int i = 0 ; 
    for (i=0 ; i < pile->numCard ; i++) {
        if (i != 0 && i % 12 == 0) {
            printf("\n") ; 
        }
        printf("%s ", pile->cards[i]) ; 
    }
    printf("\n") ; 
}

void TestMoveCard(void)
{
    Pile p1 ; p1.numCard = 0 ; 
    Pile p2 ; p2.numCard = 0 ; 
    char card[3] = "6S" ;
    AddCardToPile(&p1, card) ; 
    PrintPile(&p1) ;
    MoveCard(&p1, &p2) ;
    PrintPile(&p1) ;
    PrintPile(&p2) ;
}

Pile * Left (Pile * pile, int num)
{
    int i = 0 ; 
    Pile * cur = pile ; 
    while (cur->prev != NULL && i < num) {
        cur = cur->prev ; 
        i += 1 ; 
    }
    if (i < num) return NULL ; 
    else return cur ; 
}

char * TopCardInPile(Pile * pile)
{
    if (pile == NULL) return NULL ;
    return pile->cards[pile->numCard-1] ;
}

int PileMatch(Pile * p1, Pile * p2) {
    if (p1 == NULL || p2 == NULL) return FALSE ; 
    return CardMatch(TopCardInPile(p1), TopCardInPile(p2)) ; 
}

void
MoveCard(Pile * p1, Pile *p2) 
{
    // Move Card from p1 to p2
    if (p1->numCard == 0) 
        return ; 
    char temp[3] ;
    PopCardToPile(p1, temp) ; 
    AddCardToPile(p2, temp) ; 
}

void PrintStack(Pile * start)
{
    Pile * cur = start ; 
    while (cur != NULL) {
        PrintPile(cur) ; 
        cur = cur->next ;        
    }
}

void
ProcessPiles()
{
    Pile * cur = &piles[0] ; 
    while (cur != NULL) {
        Pile * prev = Left(cur, 3) ; 
        if (prev != NULL && PileMatch(cur, prev) == TRUE) {
            MoveCard(cur, prev) ; 
            if (cur->numCard == 0) {
                (cur->prev)->next = cur->next ; // delete this pile
                if (cur->next) {
                    (cur->next)->prev = cur->prev ;
                }
            }
            cur = prev ;
            continue ; 
        }
        prev = Left(cur, 1) ; 
        if (prev != NULL && PileMatch(cur, prev) == TRUE) {

            MoveCard(cur, prev) ; 
            if (cur->numCard == 0) {
                (cur->prev)->next = cur->next ; // delete this pile
                if (cur->next) {
                    (cur->next)->prev = cur->prev ;
                }
            }
            cur = prev ;
            continue ; 
        }
        cur = cur->next ; 
    }
}

void PrintResult(void)
{
    Pile * start = &piles[0]; 
    if (start->numCard == 52) {
        printf("1 pile remaining: 52\n") ; 
    }
    else {
        int count = 0 ; 
        int nums[52] ;
        while (start != NULL) {
            nums[count++] = start->numCard ; 
            start = start->next ; 
        }
        printf("%d piles remaining:", count) ; 
        int i ; 
        for (i=0 ; i < count ; i++) {
            printf(" %d", nums[i]) ; 
        }
        printf("\n") ;
    }
}

int work(void)
{
    ResetPiles() ; 
    char temp[3] ; 
    scanf("%s", temp) ; 
    if (temp[0] == '#') {
        return 1 ;
    }
    AddCardToPile(&piles[0], temp) ; 
    int i = 1 ; 
    for (; i < 52 ; i++) {
        scanf("%s", temp) ; 
        AddCardToPile(&piles[i], temp) ; 
    }
    // PrintStack(&piles[0]);  // debug

    ProcessPiles() ;
    PrintResult() ; 

    return 0; 
}

int main(void)
{
    while (work() == 0) {
         ; 
    }
    return 0 ; 
}
