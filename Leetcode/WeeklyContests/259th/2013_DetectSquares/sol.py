'''
Prob: leetcode 2013 - Medium
Author: Ruowei Chen
Date: 26/Sep/2021
Note: 
    1) using map to store x-axis and y-axis points.
    2) Forgot that it's asking for SQUARES. 
'''
class DetectSquares:
    def __init__(self):
        self.pointCount= dict() ; 
        self.points = [] ; 
        return ;

    def add(self, point: [int]) -> None:
        if tuple(point) not in self.pointCount:
            self.pointCount[tuple(point)] = 0 ; 
        self.pointCount[tuple(point)] += 1 ;

        x,y = point ; 
        self.points.append((x,y)) ; 
        return ;

    def count(self, point: [int]) -> int:
        x, y = point ; 
        result = 0 ; 
        for point in self.points:
            px, py = point ; 
            if (px == x or py == y) or (abs(px-x) != abs(py-y)):
                continue ; 
            try: 
                result += self.pointCount[(px, y)] * self.pointCount[(x, py)] ; 
            except:
                result += 0 ; 
        return result ; 

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
detectSquares = DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
print(detectSquares.count([11, 10])); # return 1. You can choose:
                               #   - The first, second, and third points
print(detectSquares.count([14, 8]));  # return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    # Adding duplicate points is allowed.
print(detectSquares.count([11, 10])); # return 2. You can choose: