class Shape:
    def __init__(self, q=0):
        self.q = q

    def area(self):
        area = self.q*self.q
        return area


class Square(Shape):
    def __init__(self, length):
        Shape. __init__(self)
        self.length = length

    def area(self, length):
        area = length*length
        return area


q = int(input("정사각형의 한 변의 길이를 입력하세요: "))

z = Square(q)
p = z.area(q)

print("정사각형의 면적: "+str(p))
