def triple_step_rec(steps):
    """8.1.1"""
    print("triple_step_rec", steps)
    if steps < 1:
        return 0
    elif steps == 1:
        return 1
    elif steps == 2:
        return 2
    elif steps == 3:
        return 4
    return triple_step_rec(steps - 1) + triple_step_rec(steps - 2) + triple_step_rec(steps - 3)


def triple_steps_mem(steps):
    """8.1.2"""
    if steps < 1:
        return 0
    elif steps == 1:
        return 1
    elif steps == 2:
        return 2
    elif steps == 3:
        return 4

    all_steps = [0] * (steps + 1)
    all_steps[0] = 0
    all_steps[1] = 1
    all_steps[2] = 2
    all_steps[3] = 4

    for idx in range(4, steps + 1, 1):
        all_steps[idx] = all_steps[idx - 1] + all_steps[idx - 2] + all_steps[idx - 3]

    print("triple_steps_mem", all_steps)
    return all_steps[steps]


def triple_steps(steps):
    """8.1"""
    if steps < 1:
        return 0
    elif steps == 1:
        return 1
    elif steps == 2:
        return 2
    elif steps == 3:
        return 4

    a = 1
    b = 2
    c = 4
    d = 0

    for idx in range(steps - 3):
        d = c + b + a
        a = b
        b = c
        c = d

    print("triple_steps", d)
    return d


# print(triple_step_rec(5))
# triple_steps_mem(5)
# triple_steps(5)


def find_mi(ints: list, min_idx: int, max_idx: int) -> int:
    """8.3 helper"""
    print(f'min: {min_idx}, max: {max_idx}')
    if min_idx > max_idx:
        return -1

    mid_idx = (min_idx + max_idx) // 2
    mid_val = ints[mid_idx]
    if mid_idx == mid_val:
        return mid_idx

    # search left
    left_idx = min(mid_idx - 1, mid_val)
    left = find_mi(ints, min_idx, left_idx)
    if left > -1:
        return left

    # search right
    right_idx = max(mid_idx + 1, mid_val)
    return find_mi(ints, right_idx, max_idx)

    # if mid_idx < ints[mid_idx]:
    #     down = find_mi(ints, min_idx, mid_idx - 1)
    #     if down > -1:
    #         return down
    #     return find_mi(ints, ints[mid_idx], max_idx)
    # else:
    #     up = find_mi(ints, mid_idx + 1, max_idx)
    #     if up > -1:
    #         return up
    #     return find_mi(ints, min_idx, ints[mid_idx])


def magic_index(ints: list):
    """8.3"""
    if ints is None or len(ints) == 0:
        return -1
    return find_mi(ints, 0, len(ints) - 1)


# print(magic_index([2,2,3,4,6,6,6,8]))


def power_set(items: set) -> list:
    """8.4"""
    res_lst = []
    for item in items:
        for i in range(len(res_lst)):
            res = res_lst[i]
            res_lst.append({*res, item})

        res_lst.append({item})
    return res_lst


# print(power_set({3, 4, 6}))


def permutations_without_dups(string: str) -> list:
    """8.7"""
    if string is None or len(string) == 0:
        return []

    res = [[string[-1]]]
    for c in range(len(string) - 1):
        char = string[c]
        new_res = []
        for partial_result in res:
            for j in range(len(partial_result) + 1):
                new_p = partial_result.copy()
                new_p.insert(j, char)
                new_res.append(new_p)
        res = new_res

    result = []
    for char_arr in res:
        result.append(''.join(char_arr))
    return result


# t = permutations_without_dups('adcb')
# print(t)
# print(set(t))
# print(len(t))


def perm(chars: dict) -> list:
    """8.8 helper"""
    print('perm')
    if len(chars) == 0:
        return ['']

    all_permutations = []
    for char in chars:
        print('char: ', char)
        new_charset = chars.copy()
        if new_charset[char] == 1:
            del new_charset[char]
        else:
            new_charset[char] -= 1
        permutations_no_c = perm(new_charset)
        permutations_w_c = []
        for p in permutations_no_c:
            permutations_w_c.append(char + p)

        for permut in permutations_w_c:
            all_permutations.append(permut)

    return all_permutations


def permutations_with_dups(string: str) -> list:
    """8.8"""
    if string is None or len(string) == 0:
        return []
    chars = {}
    for s in string:
        if s not in chars.keys():
            chars[s] = 0
        chars[s] += 1

    return perm(chars)


# print(permutations_with_dups('abc'))


def p(close: int, opens: int, prefix: str):
    """8.9 helper"""
    if close == 0 and opens == 0:
        print(prefix)
        return
    if opens > 0:
        p(close, opens - 1, prefix + '(')
    if opens < close:
        p(close - 1, opens, prefix + ')')


def parentheses(n: int):
    """8.9"""
    if n < 1:
        return
    p(n, n, '')


# parentheses(4)

def pf(screen: list, x, y, new_color, old_color):
    """8.10 helper"""
    if x < 0 or y < 0 or y > len(screen[0]) - 1 or x > len(screen) - 1 or screen[x][y] != old_color:
        return

    old_color = screen[x][y]
    screen[x][y] = new_color
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            pf(screen, x + i, y + j, new_color, old_color)


def paint_fill(screen: list, x, y, new_color):
    """8.10"""
    pf(screen, x, y, new_color, screen[x][y])


# col1 = ['b', 'w', 'w']
# col2 = ['b', 'w', 'w']
# col3 = ['w', 'w', 'w']
# s = [col1, col2]
# paint_fill(s, 0, 1, 'g')
# print(s)


def c(n: int, coins: list, max_coins_idx: int, memo: dict) -> int:
    if max_coins_idx < 0:
        return 0
    if max_coins_idx == 0 or 0 <= n < 5:
        return 1
    if (n, max_coins_idx) in memo:
        return memo[(n, max_coins_idx)]

    total_combinations = 0
    max_coin = coins[max_coins_idx]
    res = n // max_coin
    for i in range(res + 1):
        total_combinations += c(n - i * max_coin, coins, max_coins_idx - 1, memo)

    memo[(n, max_coins_idx)] = total_combinations
    return total_combinations


def coins_options(n: int) -> int:
    """8.11"""
    if n < 0:
        return -1
    memo = {}
    return c(n, [1, 5, 10, 25], 3, memo)


# print(coins_options(100))

class Cell:
    """8.12 helper"""
    def __init__(self, row, column):
        self.row = row
        self.column = column


def is_valid_placement(row: int, column: int, placements: list) -> bool:
    """8.12 helper"""
    # For each placement, check row, col and diagonals
    for cell in placements:
        if cell.row == row or cell.column == column:
            return False
        for i in range(1, 8, 1):
            if (cell.row - i == row and cell.column - i == column) or (cell.row - i == row and cell.column + i == column) or (cell.row + i == row and cell.column -i == column) or (cell.row + i == row and cell.column + i == column):
                return False

    return True


def eq(placements: list, row: int, res: list):
    """8.12 helper"""
    if row == 8:
        res.append(placements)
        return

    for column in range(8):
        if is_valid_placement(row, column, placements):
            pm = placements.copy()
            pm.append(Cell(row, column))
            eq(pm, row + 1, res)


def eight_queens():
    """8.12"""
    res = []
    return eq([], 0, res)


# eight_queens()


class Box:
    """8.13 helper"""
    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d

    def can_stack(self, other) -> bool:
        return self.w >= other.w and self.h >= other.h and self.d >= other.d


def sob_recurse(boxes: list, stack_height: int, current_box_idx: int, top_box: int) -> int:
    """8.13 helper"""
    if current_box_idx == len(boxes):
        return stack_height
    maximum = sob_recurse(boxes, stack_height, current_box_idx + 1, top_box)
    if top_box == -1 or boxes[top_box].can_stack(boxes[current_box_idx]):
        maximum = max(maximum, sob_recurse(boxes, stack_height + boxes[current_box_idx].h, current_box_idx + 1, current_box_idx))

    return maximum


def stack_of_boxes(boxes: list) -> int:
    """8.13"""
    if boxes is None or len(boxes) == 0:
        return 0
    boxes.sort(key=lambda box: box.w, reverse=True)
    return sob_recurse(boxes, 0, 0, -1)


b = [
    Box(5, 6, 7),
    Box(1, 3, 3),
    Box(8, 4, 1)
]
# print(stack_of_boxes(b))
print(stack_of_boxes(b))
