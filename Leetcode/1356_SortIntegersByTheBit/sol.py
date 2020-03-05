class Solution:
    def sortByBits(self, arr: [int]) -> [int]:
        lst = list(map(lambda num: (num, self.countBits(num)), arr))

        # bubble sort
        for i in range(0, len(lst)-1):
            j = len(lst) - 1
            while j > i:
                front, rear = lst[j-1], lst[j]
                if front[1] > rear[1] or (front[1] == rear[1] and front[0] > rear[0]):
                    lst[j-1], lst[j] = rear, front
                j -= 1

        lst = list(map(lambda pair: pair[0], lst))
        return lst 
        

    def countBits(self, num):
        result = 0 
        while num > 0:
            result += num & 1
            num >>= 1
        return result


###### test #####
s = Solution()
arr = [0,1,2,3,4,5,6,7,8]
print(s.sortByBits(arr))
arr = [0]
print(s.sortByBits(arr))
