'''
Prob: Swap nodes in pairs. - medium
Author: Ruowei Chen
Date: 12/Mar/2022
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1, next=head)
        prev = dummy
        cur = head
        while cur is not None:
            if cur.next is None:
                break
            nex = cur.next
            cur.next, nex.next = nex.next, cur
            prev.next = nex
            prev = cur
            cur = cur.next

        return dummy.next
        

