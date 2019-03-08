/**
 * 472 Concatenated Words - Hard
 * Date: 08/Mar/2019
 * Author: Ruowei chen
 * 1) Sort the list of words by length first, then by alphabetical order.
 * 2) Walk through the list, try to match each word by using all words 
 * before the current word.
 *
 * Note:
 * 1) Need to handle special case that some word is just empty "".   
 * */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

/***************
 * Structure
 **************/
typedef struct 
{
    char * buf ; 
    int oldIndex ; 
    int len ;  // length of this string.
} Word ; 

/****************
 * Prototypes
 *
 *****************/
char ** findAllConcatenatedWordsInADict(char **words, int wordsSize,
        int * returnSize) ;
int cmpStr(const void * s1, const void * s2) ;
void printWords(char ** words, int size, char * desc) ;
void printPointers(char ** words, int size) ;

/***********************
* Global Variables
***********************/
#define MAXSIZE 10010 
Word wordList[MAXSIZE] ; 

/******************
 * Sub Routines 
 *
 * ***************/
// s1 and s2 are pointers to Word
int cmpStr(const void * s1, const void * s2) 
{
    Word * w1 = (Word *) s1 ; 
    Word * w2 = (Word *) s2 ;
    int s1Len = strlen(w1->buf) ; 
    int s2Len = strlen(w2->buf) ;
    if (s1Len != s2Len) {
        return s1Len - s2Len ; 
    }
    else {
        return strcmp(w1->buf, w2->buf) ; 
    }
}

int intCmp(const void * i1, const void * i2)
{
    int * ii1 = (int *)i1 ;
    int * ii2 = (int *)i2 ; 
    return *ii1 - *ii2 ; 
}

/**
 * words - list of words to be searched
 * wordsSize - length of the list
 * pos - position of the target word in the list 
 * from - from which character begin to search, for example, 
 * the word is "catsanddogs", from = 4, so the actual target word
 * is "anddogs".
 * Return 1 if match is found, 0 otherwise.
 */
int tryMatch(Word * words, int wordsSize, int pos, int from) 
{
    // if the target is empty string, return True (1)
    Word * target = &words[pos] ; 
    int tlen = target->len ;
    int remainLen = tlen - from ; 
    if (remainLen == 0) return 1 ;

    // Walk through each word
    int i ; 
    for (i=0 ; i < pos ; i++) {
        Word * cur = &words[i] ; 
        int curLen = cur->len;
        if (curLen > remainLen) {
            return 0 ; 
        }

        // when the current word can match part of the target string
        // starting from the head, recursively try to match the remaining 
        // characters.
        if (strncmp(cur->buf, &(target->buf[from]), curLen) == 0) {
            int temp = 1 & tryMatch(words, wordsSize, pos, from+curLen) ; 
            // when a whole match is found, return 1 straight away.
            if (temp == 1) {
                return 1 ; 
            }
        }
    }
    return 0 ;
}

char ** findAllConcatenatedWordsInADict(char **words, int wordsSize,
        int * returnSize)
{
    assert(returnSize != NULL) ; 
    *returnSize = 0 ;
    
    // result is at most the size of the words list.
    char ** result = (char **) malloc (sizeof(char *) * wordsSize) ;
    int * resultIndex = (int *) malloc (sizeof(int)*wordsSize) ; 

    // Initialize the list of Words
    int i ; 
    int nonEmptyWordSize = 0 ; 
    for (i=0 ; i < wordsSize ; i++) {
        if (words[i] == NULL || strlen(words[i]) == 0) continue ; 
        Word * cur = &wordList[nonEmptyWordSize++] ; 
        cur->buf = words[i] ; 
        cur->oldIndex = i ; 
        cur->len = strlen(cur->buf) ;
    }

    // printWords(words, wordsSize, "Before:") ; // debug

    // sort the words list
    qsort(wordList, wordsSize, sizeof(Word), cmpStr) ; 

    // printWords(wordList, wordsSize, "After:") ; // debug

    // go through each word and try match
    for (i=1 ; i < wordsSize ; i++) {
        if (tryMatch(wordList, nonEmptyWordSize, i, 0) == 1) {
            // printf("matched: %s\n", wordList[i].buf) ; // debug
            resultIndex[*returnSize] = wordList[i].oldIndex ; 
            (*returnSize) += 1 ; 
        }
    }   
    
    // sort the index list
    qsort(resultIndex, *returnSize, sizeof(int), intCmp) ; 

    for (i=0 ; i < *returnSize ; i++) {
        result[i] = words[resultIndex[i]] ; 
    }
    
    free(resultIndex) ; 
    return result ; 
}

int main(void)
{   
    char ** words = (char **) malloc(sizeof(char *)*MAXSIZE) ; 
    int wordSize = 0; 
    FILE * fin = stdin ; // fopen(stdin, "r") ; 
    char temp[1000] ; 
    while (fscanf(fin, "%s", temp) != EOF) {
        int len = strlen(temp) ; 
        char * word = (char *)malloc(sizeof(char)*(len+1)) ;
        memcpy(word, temp, sizeof(char)*len) ; 
        word[len] = '\0' ;
        words[wordSize++] = word ; 
    }

    // printWords(words, wordSize, "Words:") ; // debug

    int returnSize ; 
    char ** result = findAllConcatenatedWordsInADict(\
            words, wordSize, &returnSize) ; 
    
    // debug print
    int i ; 
    for (i=0 ; i < returnSize ; i++) {
        printf("matched: %s\n", result[i]) ; 
    }

    // clean up
    free(result) ;
    for (i=0 ; i < wordSize ; i++) {
        free(words[i]) ; 
    }
    

    return 0 ;
}


/*******************
 * Helper Functions
 ********************/
void printPointers(char ** words, int size) {
    int i ; 
    for (i=0 ; i < size ; i++) {
        printf("word[%d] ptr=%p\n", i+1, (void *)words[i]) ; 
    }
}

void printWords(char ** wordList, int size, char * desc) 
{
    if (desc == NULL) {
        desc = "Words [%d in total]:" ;
    }
    int i ; 
    printf("%s\n", desc) ; 
    for (i=0 ; i < size ; i++) {
        printf("\t%s\n", wordList[i]); 
    }
}
