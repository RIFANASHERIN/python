class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

    def area(self):
        return self.length*self.breadth

l1=int(input("enter length of rectangle 1:"))
b1=int(input("enter breadth of rectangle 1"))
l2=int(input("enter length of rectangle 2:"))
b2=int(input("enter breadth of rectangle 2"))

r1=Rectangle(l1,b1)
r2=Rectangle(l2,b2)
if r1.area()>r2.area():
    print("rectangle 1 id larger")

else:
    print("rectangle 2 is larger")

        
