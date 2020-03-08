class Solution:
    def numOfMinutes(self, n: int, headID: int, manager : [int], informTime: [int]) -> int:
        manages = dict()
        for i in range(0, len(manager)):
            man = manager[i]
            sub = i
            if man not in manages:
                manages[man] = []
            manages[man].append(sub)

        result = -1
        queue = [(headID, 0)]
        while len(queue) > 0:
            first = queue.pop(0)
            if first[1] > result:
                result = first[1]
            if first[0] in manages:
                childs = manages[first[0]]
                for child in childs:
                    queue.append((child, first[1]+informTime[first[0]]))
        return result


