/**
 * Prob: Walk
 * Author: Ruowei Chen
 * Date: 18/Dec/2019
 * Note: 
 *  1) Use Kruskal's algorithm to find MST.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 7501

typedef struct edge {
    int v1 ; 
    int v2 ; 
    long long weight ; 
} edge ; 

int cowSet[MAXN] ; 
int N, K ; 
edge edgeList[MAXN][MAXN]  ; 

void printEdge(edge * e) {
    printf("[Edge]: (%d,%d) -> %lld\n", e->v1, e->v2, e->weight) ; 
}

int edgeCmp(const void * e1, const void * e2) {
    edge * ee1 = *(edge **)(e1); 
    edge * ee2 = *(edge **)(e2); 
    int result= 0 ; 
    if (ee1-> weight > ee2->weight) {
        result = 1 ; 
    }
    else if (ee1->weight == ee2->weight) {
        result = 0 ; 
    }
    else {
        result = -1 ; 
    }
    return result ; 
}

int findUnion(int c) {
    while (cowSet[c] != c) {
        c = cowSet[c] ; 
    }
    return c ; 
}

int merge(int parent, int child) {
    int cont = 1 ;
    while (cont == 1) {
        int pc = cowSet[child] ;
        if (pc == child) cont = 0 ; 
        cowSet[child] = parent ; 
        child = pc ; 
    }
    return 0 ; 
}

long long kruskal(edge ** edgePtrs, int numEdge) {
    // initialize the set number for each cow.
    int i ; 
    for (i=1 ; i <= N ; i++) {
        cowSet[i] = i ; 
    }

    printf("numEdge=%d\n", numEdge) ; // debug
    edge ** MST = (edge **)malloc(sizeof(edge *)*numEdge) ; 
    int num = 0; 

    // walk through all the edges and try to make the MST.
    int numCmp = N ;
    for (i=0 ; i < numEdge ; i++) {
        edge * cur = edgePtrs[i] ; 
        int u = cur->v1 ; 
        int v = cur->v2 ; 
        int pu = findUnion(u) ; 
        int pv = findUnion(v) ;
        
        if (pu != pv) {
            MST[num++] = cur;
            merge(pu, v) ; 
            numCmp -= 1 ; 
        }

        if (numCmp == 1) {
            break; 
        }
    }
    
    long long result = MST[num-K+1]->weight ;
    free(MST) ; 
    return result ; 
}

int longCmp(const void *l1, const void *l2) {
    long long *ll1 = (long long *)l1 ; 
    long long *ll2 = (long long *)l2 ; 
    if (*ll1 > *ll2) return 1 ;
    else if (*ll1 == *ll2) return 0 ; 
    else return -1; 
}

long long prim(long long ** edge, long long * MSTEdge) {
    int parent[N+1] ; // record the MST edges.
    long long key[N+1] ; 
    int added[N+1] ; 

    // initialize
    int i ; 
    for (i=0 ; i <= N ; i++) {
        key[i] = 2019201998ll ; // set to infinite.
        parent[i] = -1 ; // not set
        added[i] = 0 ; // meaning not added to the MST yet
    }
    
    int cur = 1 ; 
    key[cur] = 0 ; 
    parent[i] = 0 ; 

    // keep adding nodes until number of connected components reduced to 1.
    int num = N ; 
    int next = 2 ; 
    while (num > 1) {
        added[cur] = 1 ;
        for (i=1 ; i <= N ; i++) {
            if (added[i] == 0 && edge[cur][i] < key[i]) {
                key[i] = edge[cur][i] ; 
                parent[i] = cur ; 
            }

            if (added[i] == 0 && (added[next] == 1 || key[next] > key[i])) {
                next = i ; 
            }
        }

        cur = next ; 
        num -= 1 ; 
    }

    num = 0 ; 
    for (i=2 ; i <= N ; i++) {
        MSTEdge[num++] = edge[i][parent[i]] ; 
    }

    return 0 ; 
}

long long solveByPrim() 
{
    // create the edges
    long long ** edge = (long long **)malloc(sizeof(long long *)*(N+1)) ; 
    int i,j ; 
    for (i=0 ; i <= N ; i++) {
        edge[i] = (long long *)malloc(sizeof(long long)*(N+1)) ; 
    }

    for (i=1 ; i <= N; i++) {
        edge[i][i] = 0 ; 
        for (j=i+1 ; j <= N ; j++) {
            edge[i][j] = (2019201913ll*i+2019201949ll*j) % 2019201997ll ; 
            edge[j][i] = edge[i][j] ; 
        }
    }

    long long * MSTEdge = (long long *)malloc(sizeof(long long)*(N)) ; 
    prim(edge, MSTEdge) ; 

    qsort(MSTEdge, N-1, sizeof(long long), longCmp) ; 
    
    return MSTEdge[N-K] ; 
}

int solveByKruskal(FILE * fout) 
{
    edge ** edgePtrs = (edge **) malloc(sizeof(edge *)*(N+1)*(N+1))  ;
    int numEdge = 0 ; 
    int i,j ; 
    for (i=1 ; i <= N ; i++) {
        for (j=i+1 ; j <= N ; j++) {
            
            edgeList[i][j].v1 = i ; 
            edgeList[i][j].v2 = j ; 
            edgeList[i][j].weight = (2019201913ll*i+2019201949ll*j) % 2019201997 ;
            edgePtrs[numEdge++] = &edgeList[i][j] ; 
        }
    }
    // sort the edges.
    qsort(edgePtrs, numEdge, sizeof(edge *), edgeCmp) ; 

    // run the kruskal algorithm and find the answer
    long long result = kruskal(edgePtrs, numEdge) ; 
    // printf("%lld\n", result) ; // debug
    fprintf(fout, "%lld\n", result) ; 
    free(edgePtrs) ; 
    return 0 ;
}

int main(void) {
    FILE *fin; 
    FILE *fout ; 
    fin = fopen("walk.in", "r") ; 
    fout = fopen("walk.out", "w") ; 
    fscanf(fin, "%d %d\n", &N, &K) ; 
    // printf("N=%d, K=%d\n", N, K) ; // debug

    // solveByKruskal(fout) ; 
    long long result = solveByPrim() ; 
    fprintf(fout, "%lld\n", result) ; 
    fclose(fout) ; 
    fclose(fin) ; 
    return 0  ;
}

