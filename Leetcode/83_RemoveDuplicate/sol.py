'''
Problem: Remove Duplicates from Sorted List - Leetcode Easy
Author: Ruowei Chen
Date: 25/Feb/2021
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val ;
        self.next = next ;

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(None, None) ;
        cur = dummyHead ;
        while head is not None:
            if cur.val is None or cur.val != head.val:
                cur.next = ListNode(head.val) ;
                cur = cur.next ; 
            head = head.next ;
        return dummyHead.next ;

def listToNodes(numList: [int]) -> ListNode:
    if len(numList) == 0:
        return None;
    head = ListNode(numList[0]) ;
    cur = head ;
    for i in range(1, len(numList)):
        cur.next = ListNode(numList[i]);
        cur = cur.next ; 
    return head ;

def NodesToList(node: ListNode) -> [int]:
    result = [] ;
    while node is not None:
        result.append(node.val) ; 
        node = node.next ; 
    return result ; 

##### debug #####
s = Solution() ;
nums = [1,1,2,3,3,4] ;
print(nums) ; 
print(NodesToList(s.deleteDuplicates(listToNodes(nums)))) ; 
nums = [] ;
print(nums) ; 
print(NodesToList(s.deleteDuplicates(listToNodes(nums)))) ; 
nums = [1] ;
print(nums) ; 
print(NodesToList(s.deleteDuplicates(listToNodes(nums)))) ; 
nums = [1,1,2] ;
print(nums) ; 
print(NodesToList(s.deleteDuplicates(listToNodes(nums)))) ; 
nums = [1,1,1,1,1,1] ;
print(nums) ; 
print(NodesToList(s.deleteDuplicates(listToNodes(nums)))) ; 



