'''
Prob: 160 Easy
Author: Ruowei Chen
Date: 06/Mar/2022
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        mem = set()
        a, b = headA, headB
        while a is not None or b is not None:
            if a is not None and a in mem:
                return a
            if a is not None:
                mem.add(a)
                a = a.next
            if b is not None and b in mem:
                return b
            if b is not None:
                mem.add(b)
                b = b.next

        return None



