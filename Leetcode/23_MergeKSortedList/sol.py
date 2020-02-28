import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode: 
        heap = []
        for i in range(0, len(lists)):
            node = lists[i]
            if node == None:
                continue
            else:
                heapq.heappush(heap, (node.val, i, node))
        result = ListNode(-1) # dummy
        pointer = result
        
        cur = len(lists)
        while len(heap) > 0:
            head = heapq.heappop(heap)
            pointer.next = head[2]
            pointer = pointer.next
        
            if head[2].next is not None:
                heapq.heappush(heap, (head[2].next.val, cur, head[2].next))
                cur += 1
        return result.next 


