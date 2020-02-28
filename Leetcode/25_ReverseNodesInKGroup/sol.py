'''
Prob: 25 - Hard - Reverse Nodes in K-Group
Author: Ruowei Chen
Date: 28/Feb/2020
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def transform(lst: [int]) -> ListNode:
    head = ListNode(-1) # dummy
    cur = head
    for i in range(0, len(lst)):
        cur.next = ListNode(lst[i])
        cur = cur.next
    return head.next
    
def printListNode(node: ListNode):
    if node is None:
        print(None)
    cur = node
    result = "{0}".format(cur.val)
    cur = cur.next
    while cur is not None:
        result += " -> {0}".format(cur.val)
        cur = cur.next
    print(result)

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        newHead,newTail,result = self.reverseFrom(dummy, k)
        dummy.next = newHead
        while result:
            nh,nt, result = self.reverseFrom(newTail, k)
            newTail.next = nh
            newTail = nt
        return dummy.next

    # reverse the next k nodes only from head (not included)
    # return the newHead and newTail and the reverse result in the new list
    # in the format of (newHead, newTail, result)
    def reverseFrom(self, head: ListNode, k: int) -> (ListNode, bool):
        if head is None:
            return (None, None, False)

        newTail = head.next
        # special case: if the list is of length 1, then no reverse is
        # required.
        if newTail is None or newTail.next is None:
            return (newTail, None, False)
        newHead = None
        prev = None
        cur = head.next
        count = 0
        neXt = cur.next
        while count < k:
            if cur is None:
                # not enough nodes to be reversed
                # handle later
                dummy = ListNode(-1)
                dummy.next = prev
                oldHead,oldTail, result = self.reverseFrom(dummy, count)
                # print(oldHead, result) # debug
                return (oldHead,oldTail,False)
            else:
                cur.next = prev
                prev = cur
                cur = neXt
                count += 1
                if cur is not None:
                    neXt = cur.next

        # now the newTail's next should be pointing to the next 'block'
        # verify by printing the node
        newTail.next = cur
        return (prev,newTail, True)


# debug function
def printNode(node):
    if node is None:
        print('None')
    else:
        print('val: {0}, next: {1}'.format(node.val, \
                None if node.next is None else node.next.val))
    return 

###### Test ########
lst = [1,2,3,4,5,6,7,8]
s = Solution()
head = ListNode(-1) # dummy
head.next = transform(lst)

node = s.reverseKGroup(head.next, 3)
printListNode(node)

'''
printListNode(head.next)
newHead, newTail, result = s.reverseFrom(head, 2)
head.next = newHead 
printNode(newHead) ; printNode(newTail)
while result:
    nh, nt, result = s.reverseFrom(newTail,2)
    printNode(nh) ; printNode(nt)
    newTail.next = nh
    newTail = nt
printListNode(head.next)
'''


