class Solution:
    def kIncreasing(self, arr: [int], k: int) -> int:
        alen = len(arr)
        result = 0
        for i in range(0, k):
            if i >= alen:
                break
            cur = i
            temp = [arr[cur]]
            cur += k
            while cur < alen:
                temp.append(arr[cur])
                cur += k
            # longest = self.find(temp)
            longest = self.bisectFind(temp)
            result += len(temp) - longest
        return result

    # use binary search to construct the longest non-decreasing subsequence
    def bisectFind(self, lst:[int]) -> int:
        from bisect import bisect_right
        sub = [lst[0]]
        for i in range(1, len(lst)):
            cur = lst[i]
            if cur >= sub[-1]:
                # extend the subsequence if possible
                sub.append(cur)
            else:
                # do substitution.
                pos = bisect_right(sub, cur)
                sub[pos] = cur
        return len(sub)


    # return the length of the longest non-decreasing
    def findLongestNonDecreasing(self, lst:[int]) -> int:
        llen = len(lst)
        d = dict()
        d[llen-1] = 1
        result = 0

        for i in range(llen-2, -1, -1):
            d[i] = 1
            for k in range(i+1, llen):
                if lst[i] <= lst[k]:
                    d[i] =  max(d[i], 1+d[k])
            result = max(result, d[i])
        return result

    def find(self, lst:[int]) -> int:
        Len = len(lst)
        queue = [[lst[Len-1], 1, False]] # (number, longestLength, toDelete)
        for i in range(Len-2, -1, -1):
            cur = lst[i]
            temp = 1
            for j in range(len(queue)):
                comp = queue[j]
                if cur <= comp[0]:
                    temp = max(temp, comp[1] + 1)

                if temp >= comp[1] and cur >= comp[0]:
                    comp[2] = True

            newQueue = [[cur, temp, False]]

            for q in queue:
                if not q[2]:
                    newQueue.append(q)
            queue = newQueue

        result = 0
        for q in queue:
            result = max(result, q[1])

        return result 
        
    # Wrong: try to use greedy algorithm from the left and from the right.
    def calculate(self, lst: [int]) -> int:
        t1,t2 = lst[:], lst[:]
        tlen = len(t1)
        left, right = 0, 0
        for i in range(1, tlen):
            if t1[i-1] > t1[i]:
                t1[i] = t1[i-1]
                left += 1

        for i in range(tlen-1, 0, -1):
            if t2[i] < t2[i-1]:
                t2[i-1] = t2[i]
                right += 1

        print(t1, left)
        print(t2, right)
        return min(left, right)


### test ###
s = Solution()
arr = [5,4,3,2,1]
k = 1
print(s.kIncreasing(arr, k))

arr = [4,1,5,2,6,2]
k = 2
print(s.kIncreasing(arr, k))

arr = [4,1,5,2,6,2]
k = 3
print(s.kIncreasing(arr, k))

arr = [12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3]
k = 1
print(s.kIncreasing(arr, k))

