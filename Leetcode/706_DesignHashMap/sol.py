
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 997 # a large prime number
        self.map = [[] for n in range(self.size) ]
        self.factor = 97 # a small prime
        return
    
    def hashValue(self, key: int):
        return (key * self.factor) % self.size
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hv = self.hashValue(key)
        for pair in self.map[hv]:
            if pair[0] == key:
                pair[1] = value
                return
        # the key is not found, so just insert the value
        self.map[hv].append([key, value])
        return
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hv = self.hashValue(key)
        for pair in self.map[hv]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hv = self.hashValue(key)
        rindex = -1
        for i in range(len(self.map[hv])):
            pair = self.map[hv][i]
            if pair[0] == key:
                rindex = i
                break
        if rindex != -1:
            self.map[hv].pop(rindex)
        return

        
def getPrimeNum(upLimit: int):
    result = [2,3]
    num = 5
    while num <= upLimit:
        for p in result:
            if p*p > num:
                result.append(num)
                break
            elif num % p == 0:
                break
        num += 2
    return result[-1]

######### test ############3
import random
s = MyHashMap()
print(getPrimeNum(100))
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
numOp = 10 ** 5
# numOp = 10
i = 0 
while i < numOp:
    i += 1
    op = random.choice([0,1,2])
    key = random.randint(1, 10 ** 7)
    if op == 0:
        # put
        value = random.randint(1, 10 ** 7)
        s.put(key, value)
    elif op == 1:
        # get
        s.get(key)
    else:
        # remove
        s.remove(key)
print('finished')
