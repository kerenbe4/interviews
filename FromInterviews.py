from typing import List, Tuple, Set

"""Given an array with non-negative numbers, and a number x, check if there is a subarray that sums to x"""
def is_subarray(nums: List[int], x: int) -> bool:
    if nums is None or len(nums) == 0 or x < 0:
        return False

    lower_idx = 0
    upper_idx = 0
    sums = nums[0]

    while lower_idx < len(nums) and upper_idx < len(nums):
        if sums == x:
            return True
        if sums < x:
            upper_idx += 1
            if upper_idx < len(nums):
                sums += nums[upper_idx]
        else:
            sums -= nums[lower_idx]
            lower_idx += 1

    return False


# print(is_subarray([8], 8))
# print(is_subarray([3], 8))
# print(is_subarray([1, 3, 4, 9], 8))
# print(is_subarray([1, 2, 7, 8], 8))
# ------------------------------------------------------------------------------------


"""Given a number x, calc the next bigger number with the same digits. (123->132)"""
def get_new_num(digits: List[int]) -> List[int]:
    """helper for next_big"""
    # find the smallest digit bigger than the last one
    last_one = digits[-1]
    smallest_bigger_than_last_one = digits[-2]
    idx_found = -2
    for i in range(0, len(digits) - 2, 1):
        if last_one < digits[i] < smallest_bigger_than_last_one:
            smallest_bigger_than_last_one = digits[i]
            idx_found = i

    del (digits[idx_found])
    digits.sort(reverse=True)
    digits.append(smallest_bigger_than_last_one)
    return digits


def next_big(x: int) -> int:
    if x // 10 == 0:
        return -1

    # for number 642 return list [2, 4, 6] which represents 2*10^0 + 4*10^1 + 6*10^2
    nums = []
    tmp = x
    while tmp > 0:
        nums.append(tmp % 10)
        tmp = tmp // 10

    # find breaking point
    i = 1
    while i < len(nums) and nums[i] >= nums[i - 1]:
        i += 1

    if i == len(nums):
        return -1

    new_num_list = get_new_num(nums[0:i + 1]) + nums[i + 1:]
    new_num = 0

    for i in range(len(new_num_list)):
        new_num += new_num_list[i] * pow(10, i)
    return new_num


# print(next_big(2))
# print(next_big(32))
# print(next_big(432))
# print(next_big(1234))
# ------------------------------------------------------------------------------------

"""
You want to move a note around the classroom. 
Moving it sideways (between columns) will have 90% to get caught on the first row, 45% on second row etc. 
Moving the note back/forth will have 50% to get caught on the first-second row, 25% on the second-third row etc.
"""
class Seat:
    def __init__(self, column, row):
        self.row = row
        self.column = column


class Move:
    def __init__(self, orig, to):
        self.orig = orig
        self.to = to

    def is_sideways(self) -> bool:
        return self.orig.column != self.to.column


def get_success_prob(get_caught_prob: list, row) -> float:
    if row >= len(get_caught_prob):
        for i in range(row - len(get_caught_prob) + 1):
            get_caught_prob.append(get_caught_prob[-1] / 2)

    return 1 - get_caught_prob[row]


def pass_note_chance(moves: List[Move]) -> float:
    prob = 1
    sideways_caught_prob = [0.9, 0.45]
    back_caught_prob = [0.5, 0.25]

    for move in moves:
        if move.is_sideways():
            prob *= get_success_prob(sideways_caught_prob, move.orig.row)
        else:
            prob *= get_success_prob(back_caught_prob, min(move.orig.row, move.to.row))

    return prob


# print(pass_note_chance([Move(Seat(0, 2), Seat(0, 1)), Move(Seat(0, 1), Seat(1, 1)), Move(Seat(1, 1), Seat(1, 0)), Move(Seat(1, 0), Seat(2, 0))]))
# print(pass_note_chance([Move(Seat(0, 2), Seat(1, 2))]))
# ------------------------------------------------------------------------------------


"""Build a function that returns a valid sudoku board. """
def get_min_max_of_box(x: int) -> Tuple[int, int]:
    if x <= 2:
        return 0, 2
    if x >= 6:
        return 6, 8
    return 3, 5


def get_available_options(board: List[List[int]], row: int, column: int) -> Set[int]:
    options = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    for i in range(9):
        options.discard(board[column][i])
        options.discard(board[i][row])

    row_min, row_max = get_min_max_of_box(row)
    col_min, col_max = get_min_max_of_box(column)

    for c in range(col_min, col_max + 1, 1):
        for r in range(row_min, row_max + 1, 1):
            options.discard(board[c][r])

    return options


def get_next_cell(row: int, column: int) -> Tuple[int, int]:
    if column == 8:
        return row + 1, 0
    else:
        return row, column + 1


def fill_sudoku_board(board: List[List[int]], row: int, column: int) -> Tuple[bool, List[List[int]]]:
    options = get_available_options(board, row, column)
    if len(options) == 0:
        return False, board
    if row == 8 and column == 8:
        board[column][row] = next(iter(options))
        return True, board

    # can possibly shuffle set results to gt a random board
    for option in options:
        board[column][row] = option
        n_row, n_col = get_next_cell(row, column)
        is_valid, b = fill_sudoku_board(board, n_row, n_col)
        if is_valid:
            return True, b
        else:
            board[column][row] = 0

    return False, board


def build_sudoku_board() -> List[List[int]]:
    empty_board = [[0]*9 for _ in range(9)]
    _, board = fill_sudoku_board(empty_board, 0, 0)
    return board


print(build_sudoku_board())
