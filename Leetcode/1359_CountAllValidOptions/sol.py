class Solution:
    def countOrders2(self, n: int) -> int:
        modNum = (10 ** 9) + 7
        result = 1
        isEven = 0
        for i in range(1, 2*n+1):
            result *= i
            if isEven == 1:
                result //= 2
            isEven = (isEven + 1) % 2
        return result % modNum 

    def countOrders(self, n: int) -> int:
        modNum = (10 ** 9) + 7
        result = 1
        for i in range(1, 2*n+1):
            result *= i
        result = result >> n
        return result % modNum 



###### test ######3
s = Solution()
print(s.countOrders(1))
print(s.countOrders(2))
print(s.countOrders(3))
print(s.countOrders(500))
