from typing import List, Tuple, Set
from Cracking.StacksAndQueues import Queue

"""
Facebook mock interview by Chani Shubin for Eden:
Given an array with non-negative numbers, and a number x, check if there is a subarray that sums to x
"""
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


"""
Facebook screening interview for Eden:
Given a number x, calc the next bigger number with the same digits. (123->132)
"""
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
Google screening interview for Eden:
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


"""
Google screening interview for Eden:
Build a function that returns a valid sudoku board.
"""

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

    # can possibly shuffle set results to get a random board
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


# print(build_sudoku_board())
# ------------------------------------------------------------------------------------


"""
Mock interview with Dina Goldshtein for Keren
there is a 'world' witch is represented as a grid, with bikes and people, such that #b >= #p. 
you need to match the people to bikes, in a way that every person will want to take the closest bike near him
(if for example p1 is closer to b1 than p2, so p1 will match b1, and p2 will be matched to a different bike 
"""
class Point:
    def __init__(self, row, column):
        self.row = row
        self.column = column


class Match:
    def __init__(self, person, bike, distance):
        self.person = person
        self.bike = bike
        self.distance = distance


def best_match(bikes: List[Point], people: List[Point]) -> List[Match]:
    people_bikes_all = []
    for p in people:
        for b in bikes:
            d = abs(p.row - b.row) + abs(p.column - b.column)
            people_bikes_all.append(Match(p, b, d))

    people_bikes_all.sort(key=lambda potential_match: potential_match.distance)

    used_bikes = set()
    used_people = set()
    result_matches = []

    for match in people_bikes_all:
        if match.person not in used_people and match.bike not in used_bikes:
            used_bikes.add(match.bike)
            used_people.add(match.person)
            result_matches.append(match)
            if len(used_people) == len(people):
                return result_matches

    return result_matches
# ------------------------------------------------------------------------------------


"""
Google interview, long day, Keren 2017
Given 2 people, determine if they have a common ancestor (or if they are related, not sure)
"""
class Person:
    def __init__(self, parents, children):
        self.parents = parents
        self.children = children
        self.visited = False


def have_common_ancestor(person1: Person, person2: Person) -> bool:
    if person1 is None or person2 is None:
        return False
    if person1 is person2:
        return True

    q = Queue()
    person1.visited = True
    person2.visited = True
    q.add(person1)
    q.add(person2)

    while not q.is_empty():
        p = q.remove()
        for parent in p.parents:
            if parent.visited:
                return True
            else:
                parent.visited = True
                q.add(parent)

    return False
# ------------------------------------------------------------------------------------


"""
Google interview, long day, Keren 2017
You have a game of 2 players: there is a line of gold bags, with different amount of gold in them.
each player in his turn, can choose to select one of the outer bags of the line. 
can the first player win?
"""
def play_move(coins: List[int], first_idx: int, last_idx: int, is_first_player_turn: bool, suma: int, sumb: int) -> bool:
    # 1 item left - indices are same
    if first_idx == last_idx:
        if is_first_player_turn:
            suma += coins[first_idx]
        else:
            sumb += coins[first_idx]
        return True if suma > sumb else False

    # more than 1 item - 2 options
    if is_first_player_turn:
        new_suma = suma + coins[first_idx]
        new_sumb = sumb
    else:
        new_sumb = sumb + coins[first_idx]
        new_suma = suma
    first_coin_bag = play_move(coins, first_idx + 1, last_idx, not is_first_player_turn, new_suma, new_sumb)
    if first_coin_bag:
        return True

    if is_first_player_turn:
        new_suma = suma + coins[last_idx]
        new_sumb = sumb
    else:
        new_sumb = sumb + coins[last_idx]
        new_suma = suma

    last_coin_bag = play_move(coins, first_idx, last_idx - 1, not is_first_player_turn, new_suma, new_sumb)
    return last_coin_bag


def golden_coins_game(coins: List[int]) -> bool:
    if coins is None or len(coins) == 0:
        return True
    if len(coins) == 1 or len(coins) == 2:
        return True

    return play_move(coins, 0, len(coins) - 1, True, 0, 0)


# print(golden_coins_game([5]))
# print(golden_coins_game([5, 10]))
# print(golden_coins_game([5, 10, 3])) <<<<------
# print(golden_coins_game([5, 10, 6]))
# ------------------------------------------------------------------------------------


"""
Mock interview with Eliraz Levi for Keren
given an array with numbers and a number k, determine if there are 3 numbers in the array that sums up to k.  

note, that the sum2 problem is usually solved for an unsorted array in o(n) time and o(n) space. here we have the array 
sorted, and we can utilize that to an o(n) time and o(1) space.
"""
def sum2(nums: List[int], k: int, pivot_idx: int) -> bool:
    low_idx = pivot_idx + 1
    high_idx = len(nums) - 1

    while low_idx < high_idx:
        current_sum = nums[low_idx] + nums[high_idx]
        if current_sum == k:
            return True
        if current_sum > k:
            high_idx -= 1
        else:
            low_idx += 1
    return False


def sum3(nums: List[int], k: int) -> bool:
    if nums is None or len(nums) < 3:
        return False

    nums.sort()
    for i in range(len(nums)):
        res = sum2(nums, k-nums[i], i)
        if res:
            return True

    return False

# ------------------------------------------------------------------------------------


"""
Mock interview with Romi Gelman for Keren
Given a list of couples of synonyms, and 2 sentences, determine if the sentences are the same.
example: synonyms: [(movie, film), (rating, score)]
sentence1: The rating of the film was good
sentence1: The score of the movie was good
"""


def are_syno_words(word_a: str, word_b: str, syno_set: Set[str]) -> bool:
    key = word_a + ' ' + word_b
    if key in syno_set:
        return True

    key = word_b + ' ' + word_a
    if key in syno_set:
        return True

    return False


def is_syno(sent_a: str, sent_b: str, syno: List[Tuple[str, str]]) -> bool:
    syno_words = set()
    for words in syno:
        syno_words.add(words[0] + ' ' + words[1])

    # split sentence into words
    s1 = sent_a.split(' ')
    s2 = sent_b.split(' ')

    if len(s1) != len(s2):
        return False
    # iterate over both, and compare
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if not are_syno_words(s1[i], s2[i], syno_words):
                return False

    return True


# s = [('movie', 'film'), ('rating', 'score')]
# sen1 = 'The rating of the film was good'
# sen2 = 'The score of the movie was good'
# print(is_syno(sen1, sen2, s))
# ------------------------------------------------------------------------------------


"""
Google screening interview from Doron's file (#9)
You have a matrix of booleans, False-sea, True-land. if the land doesn't touch the frame of the matrix it's an island
Write a function that receives a matrix and removes all the islands. 
"""
def is_island(land: List[List[bool]], m: int, n: int) -> bool:
    if m == len(land)-1 or n == len(land[0])-1:
        return False

    for i in [-1, 1]:
        for j in [-1, 1]:
            if land[m + i][n + j]:
                if not is_island(land, m + i, n + j):
                    return False

    return True


def remove_island(land: List[List[bool]], m: int, n: int):
    if not land[m][n]:
        return
    land[m][n] = False
    for i in [-1, 1]:
        for j in [-1, 1]:
            remove_island(land, m + i, n + j)


def find_and_remove_islands(land: List[List[bool]]):
    m = len(land)
    n = len(land[0])

    for i in range(1, m - 1, 1):
        for j in range(1, n - 1, 1):
            if land[i][j] and not land[i - 1][j] and not land[i][j - 1]:
                if is_island(land, i, j):
                    remove_island(land, i, j)


# a = [False, False, False, True, True]
# b = [False, True, False, False, True]
# c = [False, False, False, True, True]
# d = [False, False, False, True, False]
# e = [False, False, False, False, False]
# matrix = [a, b, c, d, e]
# find_and_remove_islands(matrix)
# print(matrix)
# ------------------------------------------------------------------------------------


"""
Google screening interview from Doron's file (#10)
you have a pizza of n slices with olives on it. each slice with a different amount of olives
what is the maximum olives you can have, if you can't select 2 adjacent slices?
"""
def calc_max_olives(olives: List[int], idx: int, can_use_last_slice: int, memo: dict) -> int:
    """recursive solution helper"""
    if idx > len(olives) - 1:
        return 0

    if idx == len(olives) - 1:
        return olives[-1] if can_use_last_slice else 0

    if idx in memo:
        return memo[idx]

    use_slice = olives[idx] + calc_max_olives(olives, idx + 2, can_use_last_slice, memo)
    not_use_slice = calc_max_olives(olives, idx + 1, can_use_last_slice, memo)

    memo[idx] = max(use_slice, not_use_slice)
    return memo[idx]


def max_olives_on_pizza_rec(olives: List[int]) -> int:
    """recursive solution"""
    if olives is None or len(olives) == 0:
        return 0

    memo_first_used = {}
    memo_first_not_used = {}
    with_first_slice = olives[0] + calc_max_olives(olives, 2, False, memo_first_used)
    without_first_slice = calc_max_olives(olives, 1, True, memo_first_not_used)
    return max(with_first_slice, without_first_slice)


def max_olives_on_pizza(olives: List[int]) -> int:
    if olives is None or len(olives) == 0:
        return 0

    last_one_with = olives[-1]
    last_two_with = 0
    last_one_without = 0
    last_two_without = 0

    # with is with the last one
    sum_with = olives[-1]
    sum_without = 0
    for i in range(len(olives) - 2, 0, -1):
        sum_with = max(olives[i] + last_two_with, last_one_with)
        sum_without = max(olives[i] + last_two_without, last_one_without)
        last_two_with = last_one_with
        last_one_with = sum_with
        last_two_without = last_one_without
        last_one_without = sum_without

    sum_without = max(olives[0] + last_two_without, last_one_without)
    result = max(sum_without, sum_with)
    return result


olivess = [3, 7, 6, 1, 1, 10]
print(max_olives_on_pizza(olivess))
print(max_olives_on_pizza_rec(olivess))

