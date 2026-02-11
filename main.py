class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def contains_point(self, point):
        x_axis = point.get_x()
        y_axis = point.get_y()
        condition_one = x_axis >= self.x1
        condition_two = x_axis <= self.x2
        condition_three = y_axis >= self.y1
        condition_four = y_axis <= self.y2

        if condition_one and condition_two and condition_three and condition_four:
            return True
        else:
            return False

        print(f"DEBUG: x-axis = {x_axis}")
        print(f"DEBUG: y-axis = {y_axis}")



point_one = Point(5, 4)
rectangle = Rectangle(4, 3, 9, 4)

print(rectangle.contains_point(point_one))