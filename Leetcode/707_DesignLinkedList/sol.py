'''
Prob: 707 Design Linked List - Medium
Author: Ruowei Chen
Date: 12/Mar/2022
Note: 
    1) 
'''
class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    
    def __init__(self):
        self.dummy = Node(-1)

        # first elment
        self.head = None 

        # last element
        self.tail = None 

        self.size = 0
        

    def get(self, index:int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur, i = self.head, 0
        while i < index:
            i += 1
            cur = cur.next
            if cur is None:
                return -1
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.dummy.next = node
            self.head.prev = self.dummy
            self.tail = node
        else:
            node.prev = self.dummy
            self.head.prev = node
            self.dummy.next = node
            node.next = self.head
            self.head = node
        self.size += 1
        return

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.tail is None:
            self.tail = node
            self.dummy.next = node
            self.head = node
            node.prev = self.dummy
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            prev = self.dummy
            cur = 0
            while cur < index:
                prev = prev.next
                cur += 1
            
            node = Node(val)
            nex = prev.next
            prev.next = node
            node.prev = prev
            node.next = nex
            nex.prev = node
            self.size += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        cur = self.head
        i = 0 
        while i != index:
            i += 1
            cur = cur.next

        prev, nexT = cur.prev, cur.next
        # print(f'delete cur: {cur.val}') # debug
        # print(f'prev: {prev.val}, next: {nexT.val}') # debug

        prev.next = nexT
        if nexT is not None:
            nexT.prev = prev

        # update the head
        if index == 0:
            self.head = nexT

        # update the tail
        if index == self.size-1:
            self.tail = prev

        self.size -= 1
        return

def printList(desc='', myList=None):
    result = []
    for i in range(myList.size):
        result.append(myList.get(i))
    print(desc, result, f'size: {myList.size}') 

### test ###
ll = MyLinkedList()
ll.addAtHead(1)
ll.addAtTail(10)
ll.addAtHead(2)
printList('initial:', ll)
ll.deleteAtIndex(0)
printList('deleted index 0:', ll)
ll.addAtTail(12)
printList('add at tail 12:', ll)
ll.addAtHead(5)
printList('add at head 5:', ll)
ll.addAtIndex(-1, 4)
printList('invalid add:', ll)
ll.addAtIndex(5, 4)
printList('invalid add:', ll)
ll.addAtIndex(0, 4)
printList('add 4 at 0:', ll)
ll.addAtIndex(5, 6)
printList('add 6 at 5:', ll)
ll.deleteAtIndex(-1)
printList('invalid delete:', ll)
ll.deleteAtIndex(6)
printList('invalid delete:', ll)
ll.deleteAtIndex(3)
printList('delete at index 3:', ll)
ll.deleteAtIndex(0)
printList('delete at index 0:', ll)
ll.deleteAtIndex(3)
printList('delete at index 3:', ll)
ll.addAtIndex(1, 3)
printList('add 3 at index 1:', ll)
ll.addAtIndex(3, 8)
printList('add 8 at index 3:', ll)











