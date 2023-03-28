class BoundingRectangle:
    def __init__(self):
        self.points = []
        self.main1 = None
        self.main2 = None

    def add_point(self, x, y):
        self.points.append((x, y))
        if len(self.points) >= 2:
            self.main1 = (min(map(lambda el: el[0], self.points)), max(map(lambda el: el[1], self.points)))
            self.main2 = (max(map(lambda el: el[0], self.points)), min(map(lambda el: el[1], self.points)))

    def width(self):
        if len(self.points) < 2:
            return 0
        else:
            return self.main2[0] - self.main1[0]

    def height(self):
        if len(self.points) < 2:
            return 0
        else:
            return self.main1[1] - self.main2[1]

    def bottom_y(self):
        if len(self.points) < 2:
            return self.points[0][1]
        else:
            return self.main2[1]

    def top_y(self):
        if len(self.points) < 2:
            return self.points[0][1]
        else:
            return self.main1[1]

    def left_x(self):
        if len(self.points) < 2:
            return self.points[0][0]
        else:
            return self.main1[0]

    def right_x(self):
        if len(self.points) < 2:
            return self.points[0][0]
        else:
            return self.main2[0]


# rect = BoundingRectangle()
# rect2 = BoundingRectangle()
# rect.add_point(-1, 0)
# rect.add_point(0, 2)
# rect2.add_point(100, 100)
# rect.add_point(0, -3)
# rect.add_point(-4, 0)
#
# print(rect.left_x(), rect.right_x())
# print(rect.bottom_y(), rect.top_y())
# print(rect.width(), rect.height())
# print()
# print(rect2.left_x(), rect2.right_x())
# print(rect2.bottom_y(), rect2.top_y())
# print(rect2.width(), rect2.height())
# print()
#
# rect2.add_point(200, 200)
#
# print(rect.left_x(), rect.right_x())
# print(rect.bottom_y(), rect.top_y())
# print(rect.width(), rect.height())
# print()
# print(rect2.left_x(), rect2.right_x())
# print(rect2.bottom_y(), rect2.top_y())
# print(rect2.width(), rect2.height())
# print()
