import math
import random
from typing import List, Tuple, Set, Any, Dict
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


def is_subarray2(nums: List[int], k: int):
    left = 0
    temp_sum = 0
    for i in range(len(nums)):
        temp_sum += nums[i]
        while temp_sum > k:
            temp_sum -= nums[left]
            left += 1
        if temp_sum == k:
            return True
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
def golden_coins(coins: List[int]) -> bool:
    if coins is None or len(coins) in [0, 1, 2]:
        return True

    games = [[0] * len(coins) for _ in range(len(coins))]
    for i in range(len(coins)):
        games[i][i] = coins[i]

    for i in range(1, len(coins), 1):
        for j in range(0, len(coins)-i, 1):
            game_begin_idx = j
            game_end_idx = j + i
            first_option = coins[game_begin_idx] - games[game_begin_idx + 1][game_end_idx]
            second_option = coins[game_end_idx] - games[game_begin_idx][game_end_idx - 1]
            games[game_begin_idx][game_end_idx] = max(first_option, second_option)

    return games[0][-1] > 0


# print(golden_coins([5, 10, 3]))
# print(golden_coins([5, 10, 6]))
# ------------------------------------------------------------------------------------


"""
Mock interview with Eliraz Levi for Keren
Given an array with numbers and a number k, determine if there are 3 numbers in the array that sums up to k.  
"""
def sum2(nums: List[int], k: int, pivot_idx: int) -> bool:
    """
    The sum2 problem is usually solved for an unsorted array in o(n) time and o(n) space. here we have the array
    sorted, and we can utilize that to an o(n) time and o(1) space, by scanning from both sides.
    """
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
        if sum2(nums, k-nums[i], i):
            return True

    return False


# print(sum3([1, 4, 3, 9, -1, 12, -5], 6))
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


# olivess = [3, 7, 6, 1, 1, 10]
# print(max_olives_on_pizza(olivess))
# print(max_olives_on_pizza_rec(olivess))
# ------------------------------------------------------------------------------------


"""
Google screening interview from Doron's file (#7)
We define an alternative syntax for an arithmetic expression:
operator = + | *
expression = number | (operator expression+)
here are examples of valid expressions and their arithmetic value:
(+ 2 13) -> (2 + 13) -> 15
(+1(*2 3)4) -> (1 + (2 * 3) + 4) -> 11
412 -> 412
write a program that receives a valid expression as an input and returns its arithmetic value.
"""
def resolve_number(str_exp: str, idx: int) -> Tuple[int, int]:
    tmp_lst = []
    while idx < len(str_exp) and str_exp[idx] not in [' ', ')', '*', '+', '(']:
        tmp_lst.append(str_exp[idx])
        idx += 1

    value = 0
    mul = 1
    for i in range(len(tmp_lst) - 1, -1, -1):
        value += mul * int(tmp_lst[i])
        mul *= 10
    return value, idx


def resolve_expression(str_exp: str, idx: int) -> Tuple[int, int]:
    is_sum = True if str_exp[idx] == '+' else False
    values = []

    new_idx = idx + 1
    while not str_exp[new_idx] == ')':
        if str_exp[new_idx] == '(':
            value, new_idx = resolve_expression(str_exp, new_idx + 1)
            values.append(value)
        elif str_exp[new_idx] == ' ':
            new_idx += 1
        else:
            value, new_idx = resolve_number(str_exp, new_idx)
            values.append(value)

    result = sum(values) if is_sum else math.prod(values)
    return result, new_idx + 1


def new_math(str_exp: str, idx: int) -> int:
    if str_exp[idx] == '(':
        value, _ = resolve_expression(str_exp, idx + 1)
    else:
        value, _ = resolve_number(str_exp, idx)

    return value


def new_math_main(str_exp: str) -> int:
    if str_exp is None or len(str_exp) == 0:
        return 0

    res = new_math(str_exp, 0)
    return res


# print(new_math_main('412'))
# print(new_math_main('(+ 2 13)'))
# print(new_math_main('(+1(*2 3)4)'))
# print(new_math_main('(+1(*2 3)(+5 6))'))
# ------------------------------------------------------------------------------------


"""
Facebook mock interview with Lior Saddan for Keren - Q1
Given a list of words, return a list of lists grouping the words that are cezar code of each other
'abc'  <-> 'bcd' <-> 'cde' <-> ... 'zab'
f(['abc', 'bcd', 'bbb', 'eee', 'z']) -> [['abc', 'bcd'], ['bbb', 'eee'], ['z']]   cad -> ayb
a-z, 97-123
"""
def get_rep_word(word: str) -> str:
    """helper"""
    gap = ord(word[0]) - 97
    if gap == 0:
        return word

    new_word = []
    for c in word:
        n = ord(c) - gap
        n = n + 26 if n < 97 else n
        new_word.append(chr(n))
    print(new_word)
    return ''.join(new_word)


def cezar_code(words: List[str]) -> List[List[str]]:
    results = {}
    for word in words:
        rep = get_rep_word(word)
        if rep not in results:
            results[rep] = []
        results[rep].append(word)

    r = results.values()
    return r


# print(cezar_code(['abc', 'bcd', 'bbb', 'eee', 'z', 'cad', 'ayb']))
# ------------------------------------------------------------------------------------


"""
Facebook mock interview with Lior Saddan for Keren - Q2
Given a sorted list of positive integers, with duplicates, and a number, return the amount of time that number 
appear in the list. example: f([1, 1, 1, 2, 5, 7, 8, 8, 8, 8, 9, 14, 17, 21], 8) -> 4
"""
def find_max_idx(nums: List[int], start_idx: int, end_idx: int, num: int) -> int:
    if start_idx > end_idx:
        return -1

    pivot_idx = (start_idx + end_idx) // 2
    if nums[pivot_idx] > num:
        return find_max_idx(nums, start_idx, pivot_idx - 1, num)
    elif nums[pivot_idx] < num:
        return find_max_idx(nums, pivot_idx + 1, end_idx, num)
    else:
        if pivot_idx == len(nums) - 1 or nums[pivot_idx + 1] > num:
            return pivot_idx
        else:
            return find_max_idx(nums, pivot_idx + 1, end_idx, num)


def find_min_idx(nums: List[int], start_idx: int, end_idx: int, num: int) -> int:
    if start_idx > end_idx:
        return -1

    pivot_idx = (start_idx + end_idx) // 2
    if nums[pivot_idx] > num:
        return find_min_idx(nums, start_idx, pivot_idx - 1, num)
    elif nums[pivot_idx] < num:
        return find_min_idx(nums, pivot_idx + 1, end_idx, num)
    else:
        if pivot_idx == 0 or nums[pivot_idx - 1] < num:
            return pivot_idx
        else:
            return find_min_idx(nums, start_idx, pivot_idx - 1, num)


def find_scope(nums: List[int], num) -> int:
    if nums is None or len(nums) == 0:
        return 0

    min_idx = find_min_idx(nums, 0, len(nums) - 1, num)
    if min_idx == -1:
        return 0

    max_idx = find_max_idx(nums, 0, len(nums) - 1, num)
    return max_idx - min_idx + 1


# print(find_scope([1, 1, 1, 2, 5, 7, 8, 8, 8, 8, 9, 14, 17, 21], 1))
# ------------------------------------------------------------------------------------


"""
Facebook screening interview with Orit Mussel
Given a group of ints and an int k, return the number of subgroups such that s: min{s} + max{s} <= k
Example: input: [4 2 5 7], k=8 => output: 5. ([4 2 5], [4 2], [2 5], [4], [2])
"""
def subgroup_count(nums: List[int], k: int) -> int:
    if len(nums) == 0:
        return 0

    start_idx = 0
    end_idx = len(nums) - 1
    total_count = 0

    nums.sort()

    while start_idx <= end_idx:
        if nums[start_idx] + nums[end_idx] <= k:
            group_len = end_idx - start_idx + 1
            total_count += pow(2, group_len - 1)
            start_idx += 1
        else:
            end_idx -= 1

    return total_count


# print(subgroup_count([4, 2, 5, 7], 8))
# ------------------------------------------------------------------------------------


"""
Facebook full day interview from Doron's file (#5)
Detect whether an integer number is strobomorphic - remains the same when flipped horizontally AND vertically. ex: 101, 986.
(strobogrammatic number is a number that is the same when rotated180 degrees (69, 96, 1001)
"""


def num_to_digits_lst(num: int) -> List[int]:
    #  [int(d) for d in str(n)]
    res = []
    while num > 0:
        res.insert(0, num % 10)
        num //= 10

    return res


def is_strobogrammatic(num: int) -> bool:
    strobo = {0: 0, 1: 1, 8: 8, 6: 9, 9: 6}
    symmetric = {0, 1, 8}
    digits = num_to_digits_lst(num)
    digit_count = len(digits)
    if digit_count % 2 != 0 and digits[digit_count // 2] not in symmetric:
        return False

    for i in range(digit_count // 2):
        if digits[i] != strobo[digits[digit_count-1-i]]:
            return False
    return True


# print(is_strobogrammatic(111))
# ------------------------------------------------------------------------------------


"""
Google full day - interview with Oren Bernstein 
A car, with a tank of volume K liters, and a constant fuel consumption of 1 liter per kilometer, starts driving in a 
straight line from the origin towards a destination D kilometers away.
Along the road, there are N fuel stations, each at a distance di away from the origin. The cost of fuel at each fuel station is pi.
Write a function to compute the cheapest cost of fuel to reach the destination. Assume that the car starts with a full tank.
"""
def minimal_partial(tank_volume: int, fuel_dist: List[int], fuel_price: List[float], min_gas_idx: int, max_gas_idx:int,
                    dest: int, distance_passed: int, gas_available: int) -> Tuple[float, int]:
    total_price = 0
    if dest <= gas_available:
        return total_price, gas_available - dest

    if min_gas_idx > max_gas_idx:
        raise Exception

    # find cheapest gas station
    cheapest_gas_station_idx = min_gas_idx
    for idx in range(min_gas_idx + 1, max_gas_idx + 1, 1):
        if fuel_price[idx] < fuel_price[cheapest_gas_station_idx]:
            cheapest_gas_station_idx = idx

    # get result till the cheapest gas station
    distance_for_first_part = fuel_dist[cheapest_gas_station_idx] - distance_passed
    price_till_cheapest, gas_left = minimal_partial(tank_volume, fuel_dist, fuel_price, min_gas_idx,
                                                    cheapest_gas_station_idx - 1, distance_for_first_part,
                                                    distance_passed, gas_available)

    total_price += price_till_cheapest
    new_distance_passed = fuel_dist[cheapest_gas_station_idx]

    distance_left = dest - distance_for_first_part
    if distance_left > gas_left:
        # decide how much to fuel in cheapest gas station
        gas_to_fuel = min(distance_left - gas_left, tank_volume - gas_left)
        gas_left += gas_to_fuel
        total_price += gas_to_fuel * fuel_price[cheapest_gas_station_idx]

    # get cheapest price from here to the end
    cheapest_price_for_rest, gas_left = minimal_partial(tank_volume, fuel_dist, fuel_price, cheapest_gas_station_idx + 1,
                                                        max_gas_idx, distance_left,
                                                        new_distance_passed, gas_left)
    total_price += cheapest_price_for_rest

    return total_price, gas_left
# ------------------------------------------------------------------------------------


"""
Facebook full day - From Doron's file #17
Write a minesweeper generator (receiving columns, rows, number of mines) 
"""
def update_numbers(ms_board: List[List[Any]], m: int, n: int):
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if 0 <= m + i < len(ms_board) and 0 <= n + j < len(ms_board[0]) and ms_board[m + i][n + j] != 'm':
                ms_board[m + i][n + j] += 1


def randomize_mine(rows: int, columns: int):
    x = random.randint(0, rows - 1)
    y = random.randint(0, columns - 1)
    return y, x


def minesweeper(rows: int, columns: int, mines: int) -> List[List[Any]]:
    # initialize
    ms_board = [[0] * rows for _ in range(columns)]

    # randomize mines, add numbers
    mines_count = mines
    while mines_count > 0:
        m, n = randomize_mine(rows, columns)
        if ms_board[m][n] != 'm':
            mines_count -= 1
            ms_board[m][n] = 'm'
            update_numbers(ms_board, m, n)

    return ms_board


# b = minesweeper(4, 6, 5)
# for r in b:
#     print(r)
# ------------------------------------------------------------------------------------


"""
Facebook full day - From Doron's file #6
Given an array of words, and an alternative alphabet - return true/false indicating whether the words array is sorted
based on the alternative alphabet. 
"""
def is_words_ordered(first: str, last:str, mapping: Dict[str, int]) -> bool:
    for f, l in zip(first, last):
        if mapping[f] < mapping[l]:
            return True
        elif mapping[f] > mapping[l]:
            return False

    # i = 0
    # while i < len(first) and i < len(last):
    #     if mapping[first[i]] == mapping[last[i]]:
    #         i += 1
    #     elif mapping[first[i]] < mapping[last[i]]:
    #         return True
    #     else:
    #         return False

    if len(last) < len(first):
        return False
    return True


def is_valid(new_alpha: List[str], words: List[str]) -> bool:
    mapping = {c: v for v, c in enumerate(new_alpha)}

    for i in range(len(words) - 1):
        if not is_words_ordered(words[i], words[i+1], mapping):
            return False

    return True


# alph = ['b', 'c', 'a']
# print(is_valid(alph, ['ca', 'cab']))


"""
Facebook full day - interview with Asaf ziv
you are given 2 lists of intervals (each one is ordered and doesn't dissect itself).
you need to write a function that will return all the common parts of the intervals from the 2 lists.
Example: 
A = [(1, 2), (3, 4), (7, 10)]
B = [(0, 2), (3, 8), (9, 12)]

Result = [(1, 2) (3, 4) (7, 8) (9, 10)] 
"""
def compare_intervals(interval_a: Tuple[int, int], interval_b: Tuple[int, int]) -> Tuple[bool, Tuple[int, int]]:
    interval_begin = max(interval_a[0], interval_b[0])
    interval_end = min(interval_a[1], interval_b[1])

    if interval_begin < interval_end:
        return True, (interval_begin, interval_end)
    else:
        return False, (0, 0)


def common_intervals(intervals_a: List[Tuple[int, int]], intervals_b: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    results = []
    a_idx = 0
    b_idx = 0

    while a_idx < len(intervals_a) and b_idx < len(intervals_b):
        found_interval, new_interval = compare_intervals(intervals_a[a_idx], intervals_b[b_idx])
        if found_interval:
            results.append(new_interval)

        end_a = intervals_a[a_idx][1]
        end_b = intervals_b[b_idx][1]

        if end_a <= end_b:
            a_idx += 1

        if end_b <= end_a:
            b_idx += 1

    return results


# print(common_intervals([(1, 2), (4, 5)], [(0, 3), (4, 5)]))
# print(common_intervals([(1, 2)], [(8, 9)]))
# print(common_intervals([(1, 2), (3, 4), (7, 10)], [(0, 2), (3, 8), (9, 12)]))
