import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width=0, height=0, corner=None):
        self.width = width
        self.height = height
        self.corner = corner if corner else Point()

class Circle:
    def __init__(self, center=None, radius=0):
        self.center = center if center else Point()
        self.radius = radius

def distance_between_p1_p2(p1,p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def point_in_circle(circle, point):
    dist = distance_between_p1_p2(circle.center, point)
    return dist <= circle.radius

def rect_in_circle(circle, rect):

    p1 = rect.corner 
    p2 = Point(rect.corner.x + rect.width, rect.corner.y)
    p3 = Point(rect.corner.x, rect.corner.y + rect.height) 
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height) 

    return (point_in_circle(circle, p1) and 
            point_in_circle(circle, p2) and 
            point_in_circle(circle, p3) and 
            point_in_circle(circle, p4))

def rect_circle_overlap(circle, rect):
    closest_x = max(rect.corner.x, min(circle.center.x, rect.corner.x + rect.width)
    closest_y = max(rect.corner.y, min(circle.center.y, rect.corner.y + rect.height))
    
    closest_point = Point(closest_x, closest_y)
    return distance_between_points(circle.center, closest_point) <= circle.radius

if __name__ == "__main__":
    my_circle = Circle(Point(150, 100), 75)
  
    p_inside = Point(160, 110)
    p_outside = Point(250, 250)
    print(f"Điểm {p_inside.x, p_inside.y} trong hình tròn: {point_in_circle(my_circle, p_inside)}") # True
    print(f"Điểm {p_outside.x, p_outside.y} trong hình tròn: {point_in_circle(my_circle, p_outside)}") # False

    rect_in = Rectangle(20, 20, Point(140, 90))
    rect_out = Rectangle(100, 100, Point(100, 100)) 
    print(f"HCN nằm hoàn toàn trong hình tròn: {rect_in_circle(my_circle, rect_in)}") # True
    print(f"HCN (lớn) nằm hoàn toàn trong hình tròn: {rect_in_circle(my_circle, rect_out)}") # False

    rect_overlap = Rectangle(200, 10, Point(50, 95))
    print(f"HCN có chồng lấn với hình tròn: {rect_circle_overlap(my_circle, rect_overlap)}") # True
