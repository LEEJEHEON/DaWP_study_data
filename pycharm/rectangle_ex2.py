import rectangle



r= rectangle.Rectangle(5,4)
print("The first rectangle \n{} ".format(r.__str__()))

s= rectangle.Rectangle(4,4)
print("The second rectangle \n{} ".format(s.__str__()))

q= rectangle.Rectangle(5,4)
print("The third rectangle \n{} ".format(q.__str__()))


print("The diagram of the first rectangle is {0:0.2f}".format(r.diagonal()))
print("The first and the second {}".format(r.__eq__(s)))
print("The first and the third {}".format(r.__eq__(q)))