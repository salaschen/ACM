'''
Prob: Medium - Reverse Nodes in Even Length Groups
Author: Ruowei Chen
Date: 15/Nov/2021

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def addList(self, numList: [int]):
        cur = self
        while cur.next is not None:
            cur = cur.next
        for i in range(len(numList)):
            cur.next = ListNode(numList[i])
            cur = cur.next

    
def readOutList(node) -> [int]:
    result = []
    cur = node 
    while cur is not None:
        result.append(cur.val)
        cur = cur.next
    return result

def readInList(numList:[int]) -> ListNode:
    if len(numList) == 0:
        return None
    head = ListNode(numList[0])
    head.addList(numList[1:])
    return head

class Solution: 
    def reverseEvenLengthGroups(self, head: [ListNode]) -> [ListNode]: 
        if head is None:
            return None

        dummy = ListNode()
        dummy.next = head
        curHead = head
        prevTail = dummy
        groupSize = 1
        while curHead is not None:
            newTail, count = self.getTailInGroup(curHead, groupSize)
            if count % 2 == 0:
                newHead, newTail = self.reverseInGroup(curHead, count)
            else:
                newHead = curHead

            prevTail.next = newHead
            groupSize += 1
            curHead, prevTail = newTail.next, newTail

        return dummy.next


    def getTailInGroup(self, groupHead: ListNode, groupSize: int) -> (ListNode, int):
        if groupHead is None:
            return None
        end = groupHead
        count = 1
        while count < groupSize and end.next is not None:
            end = end.next
            count += 1
        return (end,count)
    
    # reverse the nodes within the group of size [groupSize].
    # limit is the maximum number of nodes to be reversed.
    # returns the new head node of the reversed group, and the head node for the next group.
    def reverseInGroup(self, groupHead: ListNode, limit: int) -> (ListNode,ListNode):
        stack = []
        cur = groupHead
        count = 0
        tail = None
        while count < limit:
            if cur is None:
                break
            else:
                stack.append(cur)
                count += 1
                cur = cur.next

        # tail is the head for the next group.
        tail = cur
        groupHead = stack.pop()
        cur = groupHead 
        while len(stack) > 0:
            cur.next = stack.pop()
            cur = cur.next

        # now cur is the last node of the current group.
        cur.next = tail
        groupTail = cur

        # print('head', groupHead, 'tail', groupTail) # debug
        return (groupHead, groupTail)


### test ### 
s = Solution()
numList = [1,1,0,6]
head = readInList(numList)
print(readOutList(head))
head = s.reverseEvenLengthGroup(head)
print(readOutList(head))

numList = [5,2,6,3,9,1,7,3,8,4]
head = readInList(numList)
print(readOutList(head))
head = s.reverseEvenLengthGroup(head)
print(readOutList(head))

numList = [2,1]
head = readInList(numList)
print(readOutList(head))
head = s.reverseEvenLengthGroup(head)
print(readOutList(head))

numList = [8]
head = readInList(numList)
print(readOutList(head))
head = s.reverseEvenLengthGroup(head)
print(readOutList(head))

numList = [0,4,2,1,3]
head = readInList(numList)
print(readOutList(head))
head = s.reverseEvenLengthGroup(head)
print(readOutList(head))


