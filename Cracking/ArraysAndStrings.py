"""
Arrays and Strings
questions (pdf page 102-103, book page 90-91)
solutions (pdf page 204, book page 192)
"""


def max_vacation_days(year):
    total_weeks = len(year)
    schedule = [-1] * total_weeks

    for idx in range(total_weeks):
        week = year[idx]
        best_country = -1
        mvd = -1
        for country in range(len(week)):
            if week[country] > mvd:
                best_country = country
                mvd = week[country]
        schedule[idx] = best_country
    return schedule


# week1 = [0, 0, 1, 3, 0]
# week2 = [2, 0, 1, 1, 0]
# week3 = [0, 0, 1, 3, 4]
#
# print(max_vacation_days([week1, week2, week3]))
# -----------------------------------------------------------------------------


def is_unique(my_str):
    """1.1.1"""
    unique_chars = set()
    for s in my_str:
        if s in unique_chars:
            return False
        else:
            unique_chars.add(s)
    return True


def is_unique_no_buffer(my_str):
    """1.1.2"""
    for i in range(len(my_str)):
        for k in range(i + 1, len(my_str)):
            if my_str[i] == my_str[k]:
                return False
    return True


# print(is_unique_no_buffer('test'))
# -----------------------------------------------------------------------------

def check_permutations(str1, str2):
    """1.2"""
    if str1 is None or str2 is None:
        return False
    str_len = len(str1)
    if str_len != len(str2):
        return False

    is_used = [False] * str_len

    for char in str1:
        found_match = False
        for idx in range(str_len):
            if char == str2[idx] and is_used[idx] is False:
                is_used[idx] = True
                found_match = True
                break
        if found_match is False:
            return False

    return True


def check_permutation(str1, str2):
    """1.2 with sorted strings"""
    if str1 is None or str2 is None:
        return False
    str_len = len(str1)
    if str_len != len(str2):
        return False

    s1 = sorted(str1)
    s2 = sorted(str2)
    if s1 == s2:
        return True
    else:
        return False


# print(check_permutation('', ''))
# print(check_permutation('lge', 'qwrq'))
# print(check_permutation('boss', 'sobs'))
# print(check_permutation('bsss', 'sbss'))
# print(check_permutation('bsss', 'sbsb'))
# -----------------------------------------------------------------------------


def urlify(str_arr, str_len):
    """1.3"""
    p = len(str_arr) - 1
    # for idx in reversed(range(str_len)):
    for idx in range(str_len - 1, -1, -1):
        if str_arr[idx] == ' ':
            str_arr[p] = '0'
            str_arr[p - 1] = '2'
            str_arr[p - 2] = '%'
            p = p - 3
        else:
            str_arr[p] = str_arr[idx]
            p = p - 1


# arr = ['m', 'r', ' ', 'j', 'h', 'o', 'n', 's', '', '']
# urlify(arr, 8)
# arr2 = [' ', ' ', '', '', '', '']
# urlify(arr2, 2)
# print(arr2)
# -----------------------------------------------------------------------------


def one_way(str1, str2):
    """1.5"""
    if str1 is None or str2 is None:
        return False
    k = len(str1) - len(str2)
    if abs(k) > 1:
        return False

    longer = str1 if k == 1 else str2
    shorter = str2 if k == 1 else str1

    found_difference = False
    lp = 0
    sp = 0
    while lp < len(longer) and sp < (len(shorter)):
        if longer[lp] != shorter[sp]:
            if found_difference:
                return False
            else:
                found_difference = True
                lp = lp + 1
                if k == 0:
                    sp = sp + 1
        else:
            lp = lp + 1
            sp = sp + 1

    return True


# print(one_way('longggggggg', 'short'))
# print(one_way('short', 'longggggggg'))
# print(one_way('pale', 'ple'))
# print(one_way('pales', 'pale'))
# print(one_way('pale', 'bale'))
# print(one_way('pale', 'bake'))
# -----------------------------------------------------------------------------
