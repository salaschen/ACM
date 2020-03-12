'''
Prob: Leetcode 460 LFU Cache - Hard
Author: Ruowei Chen
Date: 08/Mar/2020
'''
import random
import heapq

class LFUCache:
    def __init__(self, capacity: int):
        self.round = 0

        # heap item: (key, count, lastRound)
        self.heap = Heap((lambda e1,e2: 1 if e1[1]>e2[1] or (e1[1]==e2[1] and e1[2]>e2[2]) else -1),\
                         (lambda elem: elem[0]))
        
        self.cache = dict()
        self.capacity = capacity
        self.size = 0
        return

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.round += 1
            self.heap.update(key, self.round)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 

        self.round += 1

        # the key is not in the cache
        if key not in self.cache:
            # if cache is full, pop the least frequent item first.
            if self.size == self.capacity:
                oldKey = self.heap.pop()
                self.cache.pop(oldKey)
                self.size -= 1
                # print('poping {0}'.format(oldKey)) # debug
            
            # now insert the key
            self.cache[key] = value
            self.heap.push([key, 1, self.round])
            self.size += 1

        # the key is in the cache, then just need to update the key.
        else:
            self.cache[key] = value
            self.heap.update(key, self.round)
        return

# need to write a min-heap by hand
class Heap:
    def __init__(self, compareFunc, getKeyFunc):
        self.queue = [] # item is (key, num1, num2)
        self.position = dict() # dict is key:int -> pos:int
        self.size = 0
        self.compFunc = compareFunc # the function used to compare two items.
        self.getKeyFunc = getKeyFunc # the function that extract the key in the item.
        return 
    
    # swap the two elements in pos1 and pos2
    def swap(self, pos1, pos2):
        # boundary check
        if pos1 < 0 or pos1 >= self.size or pos2 < 0 or pos2 >= self.size:
            return 

        # swap the element
        k1, k2 = self.getKeyFunc(self.queue[pos1]), self.getKeyFunc(self.queue[pos2])
        self.queue[pos1], self.queue[pos2] = self.queue[pos2], self.queue[pos1]

        # update the positions
        self.position[k1], self.position[k2] = pos2, pos1
        return 

    # remove and return the least frequent element in the queue
    # return the key.
    def pop(self) -> int:
        if self.size == 0:
            return None
        
        # swap the first and the last element
        self.swap(0, self.size-1)

        # do a heapify down for the first element
        key = self.getKeyFunc(self.queue[self.size-1])
        self.position.pop(key)

        self.size -= 1
        self.heapifyDown(0)

        # remove and return the wanted key
        self.queue.pop(self.size) 

        return key 

    def push(self, item) -> None:
        self.queue.append(item)
        key = self.getKeyFunc(item)
        self.size += 1
        self.position[key] = self.size - 1
        self.heapifyUp(self.size-1)
        return

    # update the count and the round counter when the key is access.
    def update(self, key, rd):
        if key not in self.position:
            return 
        pos = self.position[key] 
        item = self.queue[pos]
        item[1] += 1
        item[2] = rd
        self.heapifyDown(pos)
        return


    def child(self, index) -> (int, int):
        return [2*index+1, 2*index+2]

    def heapifyDown(self, pos):
        if pos < 0:
            return 

        # keep going down when possible.
        while pos < self.size - 1:
            childs = list(filter(lambda n: n >= 0 and n < self.size, self.child(pos)))
            # print(childs) # debug
            needSwap = False
            target = pos 
            for child in childs:
                a, b = self.queue[target], self.queue[child]
                temp = self.compFunc(self.queue[target], self.queue[child])
                # print('a={0},b={1},cmp={2}'.format(a,b,temp)) # temp
                
                if self.compFunc(self.queue[target], self.queue[child]) > 0:
                    needSwap = True
                    target = child

            if needSwap:
                self.swap(pos, target)
                pos = target
            else:
                break
        return 

    def heapifyUp(self, pos):
        # boundary check
        if pos <= 0 or pos > self.size-1:
            return

        while pos > 0:
            parent = (pos-1)//2
            if self.compFunc(self.queue[parent], self.queue[pos]) > 0:
                self.swap(parent, pos)
                pos = parent
            else:
                break
        return

###### test ######3
def testHeap():
    down,up = -1*(2**31), 2**31
    size = 10000
    nums = [random.randint(down, up) for n in range(size)]
    
    heap = Heap((lambda n1, n2: -1 if n1 < n2 else (0 if n1 == n2 else 1)), \
                (lambda n1: n1))

    for num in nums:
        heap.push(num)

    heapList = []
    while heap.size > 0:
        item = heap.pop()
        heapList.append(item)

    # print(heapList) # debug
    nums = sorted(nums)   
    for i in range(0, size):
        if nums[i] != heapList[i]:
            print("test failed")
            return 
    print("test passed")
    return

def testCache():
    cache = LFUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    temp = cache.get(1)
    print(temp, cache.cache, cache.heap.queue)
    cache.put(3,3)
    temp = cache.get(2)
    print(temp, cache.cache, cache.heap.queue)
    temp = cache.get(3)
    print(temp, cache.cache, cache.heap.queue)
    cache.put(4,4)
    temp = cache.get(1)
    print(temp, cache.cache,cache.heap.queue)
    temp = cache.get(3)
    print(temp, cache.cache,cache.heap.queue)
    temp = cache.get(4)
    print(temp, cache.cache,cache.heap.queue)
    return

def testCacheRandom():
    cache = LFUCache(10)
    down, up = 0, 100
    rd = 1000
    for i in range(rd):
        temp = random.randint(0,10)
        if temp >= 2:
            cache.put(random.randint(down, up), random.randint(down, up))
        else:
            print(cache.get(random.randint(down,up)))
    return

#### main #####
testCacheRandom()
