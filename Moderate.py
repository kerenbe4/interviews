def number_swapper(a: int, b: int) -> tuple:
    """16.1"""
    a = a + b
    b = a - b
    a = a - b
    return a, b


# x = 3
# y = 5
# number_swapper(x, y)
# print(x, y)


class Point:
    """16.3 helper"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Section:
    """16.3 helper"""
    def __init__(self, point_a: Point, point_b: Point):
        self.start = point_a if point_a.x <= point_b.x else point_b
        self.end = point_a if point_a.x > point_b.x else point_b

    def is_point_in_section(self, p: Point) -> bool:
        in_x_range = self.start.x <= p.x <= self.end.x
        in_y_range = False
        if self.start.y < self.end.y:
            if self.start.y <= p.y <= self.end.y:
                in_y_range = True
        else:
            if self.end.y <= p.y <= self.start.y:
                in_y_range = True

        return in_x_range and in_y_range


class Line:
    """16.3 helper"""
    def __init__(self, s: Section):
        dy = (s.end.y - s.start.y)
        dx = (s.end.x - s.start.x)
        if dx == 0:
            self.slope = float('inf')
        else:
            self.slope = dy / dx
        self.extra = s.start.y - (self.slope * s.start.x)
        print(self.slope, self.extra)

    @staticmethod
    def get_intersection_point(line_a: 'Line', line_b: 'Line') -> Point:
        slopes = line_a.slope - line_b.slope
        extras = line_b.extra - line_a.extra
        res_x = extras / slopes
        res_y = line_a.slope * res_x + line_a.extra
        return Point(res_x, res_y)


def intersection(section_a: Section, section_b: Section) -> Point:
    """16.3"""
    line_a = Line(section_a)
    line_b = Line(section_b)

    if line_a.slope == line_b.slope:
        # parallel lines
        if line_a.extra == line_b.extra:
            print('this is the same line!')
            if section_a.is_point_in_section(section_b.start):
                return section_b.start
            elif section_a.is_point_in_section(section_b.end):
                return section_b.end
            else:
                print('got same line but different sections')
                return Point(None, None)
        print('got parallel (but not same) lines')
        return Point(None, None)
    else:
        intersection_point = Line.get_intersection_point(line_a, line_b)
        if section_a.is_point_in_section(intersection_point) and section_b.is_point_in_section(intersection_point):
            return intersection_point
        else:
            return Point(None, None)


# res = intersection(Section(Point(1, 7), Point(6, 2)), Section(Point(3, 1), Point(7, 5))) # intersecting lines
# res = intersection(Section(Point(2, 2), Point(3, 3)), Section(Point(3, 2), Point(4, 3))) # parallel horizontal lines
# res = intersection(Section(Point(1, 1), Point(1, 6)), Section(Point(2, 1), Point(2, 6)))  # parallel vertical lines
# res = intersection(Section(Point(2, 2), Point(3, 3)), Section(Point(5, 5), Point(6, 6))) # same line, sections do not intersect
# res = intersection(Section(Point(2, 2), Point(2, 3)), Section(Point(2, 5), Point(2, 6))) # same line, vrtical, sections do not intersect
# print(res.x, ', ', res.y)


def factorial_zeros(n: int) -> int:
    """16.5"""
    if n < 1:
        return 0
    trailing = 1
    trailing_zeros = 0
    for i in range(2, n + 1, 1):
        trailing *= i
        while trailing % 10 == 0:
            trailing = trailing // 10
            trailing_zeros += 1
        trailing = trailing % 10
    return trailing_zeros


print(factorial_zeros(29))


def smallest_difference(a: list, b: list) -> float:
    """16.6"""
    smallest_diff = float('inf')
    a.sort()
    b.sort()
    idx_a = 0
    idx_b = 0

    while idx_a < len(a) and idx_b < len(b):
        diff = a[idx_a] - b[idx_b]
        if diff >= 0:
            if diff < smallest_diff:
                smallest_diff = diff
            idx_b += 1
        else:
            idx_a += 1
    return smallest_diff


# print(smallest_difference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))
# print(smallest_difference([23, 127, 235, 19, 8], [1, 3, 15, 11, 2]))