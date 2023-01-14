class Rectangle:
    def __init__(self,length,breadth):
        self._length=length
        self._breadth=breadth

    def __lt__(self,other):
        area1=self._length*self._breadth
        area2=other._length*other._breadth
        if area1<area2:
            print("rectangle 2 is larger")

        elif area1>area2:
            print("rectangle 1 is larger")

        else:
            print("both are equal")

l1=int(input("enter length of rectangle 1"))
b1=int(input("enter breadth of rectangle 1"))
l2=int(input("enter length of rectangle 2"))
b2=int(input("enter breadth of rectangle 2"))
rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)
rect1<rect2
