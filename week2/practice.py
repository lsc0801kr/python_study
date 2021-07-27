class Shape:
    def __init__(self, q):
        self.q = int(q)

    def area(self):
        area = self.q*self.q
        return area


class Square(Shape):
    def __init__(self, q, length):
        Shape. __init__(self, q)
        self.length = length

    def area(self, area):
        self.area = area
        print("정사각형의 면적: "+str(self.area))


q = input("정사각형의 한 변의 길이를 입력하세요: ")
r = Shape(q)
a = r.area()


z = Square(q, a)
p = z.area(a)
