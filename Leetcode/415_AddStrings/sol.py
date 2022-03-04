'''
Prob: 415 - Easy
Author: Ruowei Chen
Date: 04/Mar/2022
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = num1[:], num2[:]
        l1, l2 = len(n1), len(n2)
        # make sure num1 is no longer than num2
        if l1 > l2:
            n1, n2 = n2, n1
            l1, l2 = l2, l1
        carry = 0
        i = 0
        result = ''
        while i < l1 and i < l2:
            cur1, cur2 = int(n1[l1-i-1]), int(n2[l2-i-1])
            temp = cur1 + cur2 + carry
            carry = 0
            if temp >= 10:
                carry = 1
                temp = temp % 10
            result = str(temp) + result
            i += 1

        ### handle the residual
        length = l2 - i
        t2 = n2[0:length]
        if len(t2) > 0:
            # print(result, t2)
            result = str(int(t2) + carry) + result
        elif carry > 0:
            result = str(carry) + result
        return result

### test 
def caseTest():
    s = Solution()
    num1, num2 = '11', '123'
    print(s.addStrings(num1, num2))

    num1, num2 = '456', '77'
    print(s.addStrings(num1, num2))

    num1, num2 = '0', '0'
    print(s.addStrings(num1, num2))

    num1, num2 = '4843', '5293'
    print(s.addStrings(num1, num2))


def randomTest():
    import random
    s = Solution()
    pas, times = 0, 100
    for i in range(times):
        num1, num2 = str(random.randint(1, 10**4)), str(random.randint(1, 10**4))
        actual = s.addStrings(num1, num2)
        expect = str(int(num1) + int(num2))
        if actual != expect:
            print(f'{num1} + {num2} =')
            print(f'actual: {actual}')
            print(f'expect: {expect}')
        else:
            pas += 1
    print(f'pass {pas}/{times}')
    return

randomTest()
# caseTest()





