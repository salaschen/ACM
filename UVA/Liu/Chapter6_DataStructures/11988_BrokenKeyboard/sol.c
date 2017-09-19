/**
 * UVa 11988 - Broken Keyboard (a.k.a. Beiju Text)
 * Note: To display the Beiju text which is affected by the broken keyboard.
 * Date: 19/Sep/2017
 * Author: Ruowei Chen
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct node 
{
	char value ; 
	struct node *next ; 
} node ; 

int work(void)
{
	int c = getchar() ; 
	if (c == EOF)
		return 1 ; 
	node root ;  // dummy node 
	root.next = NULL ;
	root.value = -1 ; 
	node * cur = &root ; 
	node * tail = &root ; 
	while (c != '\n' && c != EOF)
	{
		if (c == '[')
		{
			cur = &root ; 
		}
		else if (c == ']')
		{
			cur = tail ; 
		}
		else {
			node * newNode = (node *)malloc(sizeof(node)) ; 
			newNode->value = c ; 
			newNode->next = cur->next ; 
			cur->next = newNode ; 
			cur = newNode ; 
			if (cur->next == NULL) {
				tail = cur ; 
			}
		}
		c = getchar() ; 
	}
	// print out the linked list
	cur = root.next ; 
	while (cur != NULL) {
		node * next = cur->next ; 
		printf("%c", cur->value) ; 
		free(cur) ; 
		cur = next ;
	}
	printf("\n") ; 
	return 0 ;
}


int main(void)
{
	while (work() == 0)
		; 
	return 0 ;
}
