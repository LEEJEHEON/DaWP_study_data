import rectangle

a = rectangle.Rectangle()

a.setWidth(4)
a.setHeight(5)

print("Width is {}".format(a.getWidth()))
print("Height is {}".format(a.getHeight()))

print("Area is {}".format(a.area()))
print("Perimeter is {}".format(a.perimeter()))
print("rectangle info \n{}".format(a.__str__()))

