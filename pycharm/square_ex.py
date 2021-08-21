import rectangle



a = rectangle.Square(3)
b = rectangle.Square(5)

print(a.__str__())
print(b.__str__())
print("Width is {}".format(a.getWidth()))
print("Height is {}".format(a.getHeight()))
print("The area of the square is {}" .format((a.area())))
print("The perimeter of the square is {}" .format(a.perimeter()))
print("The first and the second {}".format(a.__eq__(b)))

