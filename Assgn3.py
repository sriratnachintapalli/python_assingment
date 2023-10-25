class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def compare_area(self, other_rectangle):
        area1 = self.area()
        area2 = other_rectangle.area()
        
        if area1 > area2:
            return "Rectangle 1 is larger."
        elif area1 < area2:
            return "Rectangle 2 is larger."
        else:
            return "Both rectangles have the same area."

# Create two rectangle objects
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(7, 7)

# Calculate and display the area and perimeter for each rectangle
print("Rectangle 1 - Area:", rectangle1.area())
print("Rectangle 1 - Perimeter:", rectangle1.perimeter())

print("Rectangle 2 - Area:", rectangle2.area())
print("Rectangle 2 - Perimeter:", rectangle2.perimeter())

# Compare the two rectangles based on their areas
comparison_result = rectangle1.compare_area(rectangle2)
print(comparison_result)
