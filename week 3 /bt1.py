import math 
class Point: 
    def __init__(self, x, y):
       self.x = x 
       self.y = y 
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
A = Point(5, 6)
O = Point(0, 0)
x = int(input("Nhap gia tri Bx: "))
y = int(input("Nhap gia tri By: "))
B = Point(x, y)
C = Point(-x, -y)
print("khoang cach tu diem A den diem B la:",A.distance(B))
print("khoang cach tu diem B den diem O la:",B.distance(O))
