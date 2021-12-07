'''
Prob: Medium - Acceptance 4756/7812
Author: Ruowei Chen
Date: 07/Dec/2021
Note:
    1) Two pointers method (one single jump one double jump)
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: [ListNode]) -> [ListNode]:
        slowHead = head
        slow = head.next
        if slow is None:
            return None 
        fast = head
        fast = self.moveFast(fast)
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = self.moveFast(fast)
            slowHead = slowHead.next
        slowHead.next = slow.next # delete the middle node
        return head


    # move two steps
    def moveFast(self, node: ListNode) -> ListNode:
        if node is None:
            return None
        node = node.next
        if node is None:
            return node
        return node.next


        

