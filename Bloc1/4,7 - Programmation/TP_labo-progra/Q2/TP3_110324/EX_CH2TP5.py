def calculate(x1, x2, y1, y2):
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** (1 / 2)


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def distance_from_xy(self, xp, yp):
        return calculate(
            self.__x,
            xp,
            self.__y,
            yp
        )

    def distance_from_point(self, point):
        return calculate(
            self.__x,
            point.x(),
            self.__y,
            point.y()
        )


point1 = Point(0, 0)
point2 = Point(1, 1)


print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
