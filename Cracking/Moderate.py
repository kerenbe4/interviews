"""
Moderate - 16
questions (book pages 181-185)
solutions (book pages )
"""
from typing import List, Tuple


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


# print(factorial_zeros(29))


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


def number_max(a, b):
    """16.7"""
    diff = abs(a - b)
    small = (a + b - diff) / 2
    big = small + diff
    return big


# print(number_max(2, 2.5))


def english_int_till_999(num) -> str:
    """16.8 helper"""
    predefined = {0: '', 1: 'one', 2: 'two', 7: 'seven', 10: 'ten', 15: 'fifteen', 20: 'twenty', 60: 'sixty',
                  70: 'seventy'}
    if num in predefined:
        return predefined[num]

    if num // 100 > 0:
        return predefined[num // 100] + ' hundred ' + english_int_till_999(num % 100)
    else:
        return predefined[num - (num % 10)] + ' ' + predefined[num % 10]


def english_int(num) -> str:
    """16.8"""
    if num == 0:
        return 'zero'

    tens = {1: '', 1000: 'thousand', 1000000: 'million', 1000000000: 'billion'}
    num_str = ''
    mul = 1
    while num > 0:
        tmp_str = english_int_till_999(num % 1000)
        num_str = tmp_str + ' ' + tens[mul] + ' ' + num_str
        num //= 1000
        mul *= 1000

    return num_str


# print(english_int(62100715))


def diving_board(shorter: int, longer: int, k: int) -> set:
    """16.11"""
    results = set()
    if shorter == longer:
        results.add(k * shorter)
    elif k > 0:
        for i in range(k + 1):
            results.add(shorter * i + longer * (k - i))

    return results


# print(diving_board(3, 7, 3))
# print(diving_board(3, 3, 3))
# print(diving_board(3, 7, 0))
# print(diving_board(3, 7, 1))


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Square:
    def __init__(self, bl: Point, tr: Point):
        self.bl = bl
        self.tr = tr

    def get_center_point(self):
        x_center = (self.tr.x + self.bl.x) / 2
        y_center = (self.tr.y + self.bl.y) / 2
        return Point(x_center, y_center)


class Line2:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b


def bisect_squares(sq1: Square, sq2: Square) -> Line2:
    """16.13"""
    # get center of squares
    center1 = sq1.get_center_point()
    center2 = sq2.get_center_point()

    if center1 == center2:
        return Line2(0, center2.y)

    # calculate line
    dy = center1.y - center2.y
    dx = center1.x - center2.x

    if dx == 0:
        a = float('inf')
    else:
        a = dy / dx
    b = center1.y - a * center1.x

    return Line2(a, b)


# res = bisect_squares(Square(Point(0, 0), Point(4, 4)), Square(Point(1, 1), Point(3, 3)))
# res = bisect_squares(Square(Point(0, 0), Point(4, 4)), Square(Point(3, -1), Point(5, 1)))
# print(res.a, res.b)


def generate_line(p1: Point, p2: Point) -> str:
    dy = p1.y - p2.y
    dx = p1.x - p2.x
    a = dy / dx
    b = p1.y - a * p1.x

    xpart = "{0:.2f}".format(a) + 'x' if a != 0 else ''
    ypart = "{0:.2f}".format(b)
    if xpart == '':
        return ypart
    if ypart == '':
        return xpart
    return xpart + ' + ' + ypart


def best_line(points: list) -> str:
    """16.4"""
    if points is None or len(points) == 0:
        return ''
    if len(points) == 1:
        return str(points[0].y)
    lines_count = {}
    for i in range(len(points)):
        for j in range(i+1, len(points), 1):
            line = generate_line(points[i], points[j])
            if line not in lines_count:
                lines_count[line] = 0
            lines_count[line] += 1

    print(lines_count.items())
    max_line = ''
    max_count = -1
    for line, count in lines_count.items():
        if count > max_count:
            max_count = count
            max_line = line
    return max_line


# pts = [Point(0, 0), Point(2, 2)]
# pts = [Point(0, 4), Point(3, 1), Point(2, 2), Point(7, 13)]
# print(best_line(pts))


def master_mind(guess: str, solution: str) -> list:
    """16.15"""
    guess_letters = {}
    solution_letters = {}
    res = []

    for i in range(len(solution)):
        if guess[i] == solution[i]:
            res.append('hit')
        else:
            if not guess[i] in guess_letters:
                guess_letters[guess[i]] = 0
            guess_letters[guess[i]] += 1

            if not solution[i] in solution_letters:
                solution_letters[solution[i]] = 0
            solution_letters[solution[i]] += 1

    for solution_letter in solution_letters:
        if solution_letter in guess_letters:
            letter_match_count = min(solution_letters[solution_letter], guess_letters[solution_letter])
            for _ in range(letter_match_count):
                res.append('p-hit')

    return res


# print(master_mind('GGGG', 'RRRR'))
# print(master_mind('GGGG', 'GGGG'))
# print(master_mind('RGBY', 'GGRR'))
# print(master_mind('RGBY', 'YRGB'))
# print(master_mind('RRRG', 'YYYR'))


def sub_sort(nums: list) -> tuple:
    """16.16"""
    nums_len = len(nums)
    if nums is None or 0 <= nums_len <= 1:
        return 0, 0

    # look for the range of the middle sequence - left side
    lp = 0
    while lp < nums_len - 1 and nums[lp] <= nums[lp + 1]:
        lp += 1

    # the array is already sorted
    if lp == nums_len - 1:
        return 0, 0

    min_index = lp

    # look for the range of the middle sequence - right side
    rp = nums_len - 1
    while rp > 0 and nums[rp] >= nums[rp - 1]:
        rp -= 1
    max_index = rp

    # we now need to go through the middle part, and move the left index back
    i = lp + 1
    while i <= rp:
        if nums[i] < nums[min_index]:
            # move min_index "back" until its the equivalent number
            while min_index > 0 and nums[i] < nums[min_index - 1]:
                min_index -= 1
        i += 1

    # we now need to go through the middle part, and move the right index up
    i = rp - 1
    while i >= lp:
        if nums[i] > nums[max_index]:
            # move max_index "up" until its the equivalent number
            while max_index < nums_len - 1 and nums[i] > nums[max_index + 1]:
                max_index += 1
        i -= 1

    return min_index, max_index


# print(sub_sort([2]))
# print(sub_sort([5, 2]))
# print(sub_sort([1, 2, 3, 4, 5]))
# print(sub_sort([0, 1, 2, 3, 4, 5, 7, 6, 8, 9]))
# print(sub_sort([7, 8, 9, 10, 3, 4, 5, 6]))
# print(sub_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))


def get_pond_size(matrix: list, column: int, row: int) -> int:
    """16.19 helper"""
    if column >= len(matrix) or row >= len(matrix[0]):
        return 0
    pond_size = 0
    cell = matrix[column][row]
    if cell == 0:
        matrix[column][row] = None
        pond_size += 1

        # for each one of the neighbors - get pond size
        pond_size += get_pond_size(matrix, column + 1, row)
        for i in range(-1, 2, 1):
            pond_size += get_pond_size(matrix, column + i, row + 1)

    return pond_size


def pond_sizes(matrix: list) -> list:
    """16.19"""
    ponds = []
    rows = len(matrix[0])
    columns = len(matrix)

    # scanning all cells
    for row_idx in range(rows):
        for column_idx in range(columns):

            cell = matrix[column_idx][row_idx]
            if cell == 0:
                new_pond_size = get_pond_size(matrix, column_idx, row_idx)
                ponds.append(new_pond_size)

    return ponds


# cola = [0, 0, 1, 0]
# colb = [2, 1, 1, 1]
# colc = [1, 0, 0, 0]
# cold = [0, 1, 1, 1]
# print(pond_sizes([cola, colb, colc, cold]))
# cole = [0, 1, 0, 0]
# colf = [1, 0, 1, 2]
# colg = [2, 3, 0, 0]
# colh = [1, 0, 1, 1]
# print(pond_sizes([cole, colf, colg, colh]))


def sum_swap(arr_a: List[int], arr_b: List[int]) -> Tuple[int, int]:
    """16.21"""
    sum_a = sum(arr_a)
    sum_b = sum(arr_b)
    diff = (sum_b - sum_a) / 2

    set_a = set(arr_a)

    for item in arr_b:
        if (item - diff) in set_a:
            return (item, item - diff)

    raise Exception('not found')


# print(sum_swap([3, 6, 3, 3], [1, 1, 1]))


def resolve_number(exp, idx) -> Tuple[int, int]:
    """16.26 helper"""
    res = []
    while idx < len(exp) and exp[idx] not in ['+', '-', '*', '/']:
        res.append(int(exp[idx]))
        idx += 1

    mul = 1
    n = 0
    for i in range(len(res)-1, -1, -1):
        n += mul * res[i]
        mul *= 10

    return n, idx


def calc_next(exp: str, idx: int) -> float:
    """16.26 helper"""
    num, idx = resolve_number(exp, idx)
    while idx < len(exp):
        if exp[idx] == '+':
            return num + calc_next(exp, idx + 1)
        elif exp[idx] == '-':
            return num - calc_next(exp, idx + 1)
        elif exp[idx] == '*':
            new_num, idx = resolve_number(exp, idx + 1)
            num *= new_num
        elif exp[idx] == '/':
            new_num, idx = resolve_number(exp, idx + 1)
            num /= new_num

    return num


def calculator(exp: str) -> float:
    """16.26"""
    if len(exp) == 0:
        return 0
    return calc_next(exp, 0)


print(calculator('2*3+5/6*3+15'))
