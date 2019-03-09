/**
 * Problem: Leetcode 143 Reorder List (Medium)
 * Date: 09/Mar/2019
 * Author: Ruowei Chen
 * Note: Happy birthday to my mother.
 */
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val ; 
    struct ListNode * next ; 
};
struct ListNode * reverseList(struct ListNode * head)  ; 


void printList(struct ListNode * head) 
{
    if (head == NULL) {
        printf("NULL\n") ; 
        return ; 
    }
    struct ListNode * cur = head ; 
    while (1) {
        printf("%d", cur->val) ; 
        cur = cur->next ; 
        if (cur) {
            printf("->") ; 
        }
        else {
            break ; 
        }
    }
    printf("\n") ; 
}

struct ListNode * readList(FILE * fin) 
{
    int temp ;
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode)) ;    
    if (fscanf(fin, "%d\n", &temp) == EOF) {
        free(head) ; 
        return NULL ; 
    }
    else {
        head->val = temp ; 
        head->next = NULL ; 
    }
    struct ListNode * cur = head ; 
    while (fscanf(fin, "%d\n", &temp) != EOF) {
        cur->next = (struct ListNode *)malloc(sizeof(struct ListNode)) ; 
        cur = cur->next ; 
        cur->val = temp ; 
        cur->next = NULL ; 
    }
    return head ; 
}

// O(n) solution inspired by another user
// 1. Find the medium node.
// 2. Reverside the second half of the nodes.
// 3. Merge the first and second (reversed) half of the nodes
// E.g, 1->2->3->4->5 => 1->5->2->4->3
void reorderList(struct ListNode * head)
{
    if (head == NULL) return ; 
    struct ListNode * fast = head ; 
    struct ListNode * slow = head ; 
    while (1) {
        if (fast->next != NULL && fast->next->next != NULL) {
            fast = fast->next->next ; 
            slow = slow->next ; 
        }
        else {
            break ; 
        }
    }
    
    struct ListNode * second = reverseList(slow->next) ; 
    struct ListNode * first = head ; 

    // merge second with the first
    while (second) {
        struct ListNode * shead = second ; 
        second = second->next ; 
        struct ListNode * fhead = first ; 
        first = first->next ; 
        fhead->next = shead; 
        shead->next = first ; 
    }
    first->next = NULL ;
}

struct ListNode * reverseList(struct ListNode * head) 
{
    if (head == NULL || head->next == NULL) return head ; 
    struct ListNode * cur = head ; 
    struct ListNode * curNext = head->next ; 
    cur->next = NULL ; 
    while (curNext) {
        struct ListNode * nextNext = curNext->next ; 
        curNext->next = cur ; 
        cur = curNext ; 
        curNext = nextNext ; 
    }
    return cur ; 
}

int main(void)
{
    struct ListNode * head = readList(stdin) ; 
    printList(head) ; // debug
    reorderList(head) ; 
    // printList(reverseList(head)) ; // debug
    printList(head) ; 

    return 0 ; 
}

