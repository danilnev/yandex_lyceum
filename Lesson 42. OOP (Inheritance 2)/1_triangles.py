class Triangle:
    def __init__(self, s1, s2, s3):
        self.area = [s1, s2, s3]

    def perimeter(self):
        return sum(self.area)


class EquilateralTriangle(Triangle):
    def __init__(self, s):
        super().__init__(s, s, s)
