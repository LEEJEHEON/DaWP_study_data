
class Rectangle:

    def __init__(self,width=1,height=1):
        self.width = width
        self.height = height

    def setWidth(self,width):
        self.width= width

    def setHeight(self,height):
        self.height=height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def area(self):
        value = self.width * self.height
        return value

    def perimeter(self):
        value = (self.width+self.height)*2
        return value

    def __str__(self):
        return "Width : " + str(self.width) + "\nHeigt : " + str(self.height)

    def diagonal(self):
        value = (self.width ** 2 + self.height ** 2) ** 0.5
        return value

    def __eq__(self, num):
        if (self.width == num.width) & (self.height == num.height):
            return "rectangle is the same"
        else:
            return "rectangle is different"
class Square(Rectangle):

    def __init__(self,width):
        self.width=width
        self.height=width

    def __str__(self):
        return "The Square's Width = Height = "+str(self.width)
