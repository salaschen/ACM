class Solution:
    def getDistances(self, arr: [int]) -> [int]:
        nums = set()
        pos = dict()
        result = [0 for i in range(len(arr))]
        for i in range(len(arr)):
            num = arr[i]
            nums.add(num)
            if num in pos:
                result[i] = i * len(pos[num][0]) - pos[num][1]
                pos[num][0].append(i)
                pos[num][1] += i
            else:
                pos[num] = [[i],i]

        for num in nums:
            queue = pos[num][0]
            qsum = pos[num][1]
            qlen = len(queue)
            for i in range(len(queue)):
                u = queue[i]   
                qsum -= u
                # print(queue)
                num_pair = qlen-(i+1)
                # print(u, qsum, num_pair)
                result[u] += (qsum) - num_pair * u
                
        return result


### test ###
s = Solution()
arr = [2,1,3,1,2,3,3]
print(s.getDistances(arr))

arr = [10,5,10,10]
print(s.getDistances(arr))


