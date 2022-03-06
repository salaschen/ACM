'''
Prob: 142 - Medium
Author: Ruowei Chen
Date: 06/Mar/2022
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            if slow is None:
                return None
            if fast is None:
                return None
            fast = fast.next
            if slow == fast:
                break

        if slow is None or fast is None:
            return None

        result = 0
        slow = head
        while slow != fast:
            result += 1
            slow = slow.next
            fast = fast.next

        slow = head
        for i in range(result):
            slow = slow.next
        return slow
