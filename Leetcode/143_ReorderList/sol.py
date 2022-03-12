'''
Prob: 143 Reorder List - Medium
Author: Ruowei Chen
Date: 12/Mar/2022
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        mem = dict()
        cur = head.next
        size = 1
        while cur is not None:
            neXt = cur.next
            mem[size] = cur
            cur.next = None
            size += 1
            cur = neXt 

        cur = head
        j, i = size-1, 1
        isJ = True
        added = set()
        while (i in mem and j in mem) and (j not in added or i not in added):
            if isJ:
                cur.next = mem[j]
                added.add(j)
                j -= 1
            else:
                cur.next = mem[i]
                added.add(i)
                i += 1
            isJ = not isJ
            # print(f'inserting {cur.next.val}, (i,j)={(i,j)}') # debug
            cur = cur.next
        return

def printList(lst):
    result = []
    cur = lst
    while cur is not None:
        result.append(cur.val)
        cur = cur.next
    print(result)    

def createList(numList):
    if len(numList) == 0:
        return None
    head = ListNode(numList[0])
    cur = head
    for i in range(1, len(numList)):
        cur.next = ListNode(numList[i])
        cur = cur.next
    return head

### test ###
s = Solution()
lst = [1,2,3,4,5]
head = createList(lst)
printList(head)
s.reorderList(head)
printList(head)

