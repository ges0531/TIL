# 파일명을 변경하지 마시오.
# 아래에 Point 클래스 및 Rectangle 클래스를 작성하시오.


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, p1, p2):
        self.p1 = [p1.x, p1.y]
        self.p2 = [p2.x, p2.y]

    def get_area(self):
        return abs((self.p2[0]-self.p1[0]) * (self.p2[1]-self.p1[1]))

    def get_perimeter(self):
        return abs((self.p2[0]-self.p1[0])) * 2 + abs((self.p2[1]-self.p1[1])) * 2

    def is_square(self):
        if abs((self.p2[0]-self.p1[0])) == abs((self.p2[1]-self.p1[1])):
            return True

        else:
            return False










# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    p1 = Point(1, 3)
    p2 = Point(3, 1)
    r1 = Rectangle(p1, p2)
    print(r1.get_area())
    print(r1.get_perimeter())
    print(r1.is_square())
    p3 = Point(3, 7)
    p4 = Point(6, 4)
    r2 = Rectangle(p3, p4)
    print(r2.get_area())
    print(r2.get_perimeter())
    print(r2.is_square())
