from typing import List


def sorted_merge(a: list, b: list):
    """10.1"""
    p_idx = len(a) - 1
    b_idx = len(b) - 1
    a_idx = p_idx - len(b)

    while b_idx >= 0 and a_idx >= 0:
        if a[a_idx] > b[b_idx]:
            a[p_idx] = a[a_idx]
            a_idx -= 1
        else:
            a[p_idx] = b[b_idx]
            b_idx -= 1
        p_idx -= 1

    while b_idx >= 0:
        a[p_idx] = b[b_idx]
        b_idx -= 1
        p_idx -= 1


# c = [1, 1, 7, 10, 12, None, None]
# d = [1, 2]
# sorted_merge(c, d)
# print(c)


def group_anagrams(words: list) -> None:
    """10.2"""
    buckets = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in buckets.keys():
            buckets[sorted_word] = []
        buckets[sorted_word].append(word)

    p = 0
    for bucket, anagrams in buckets.items():
        for anagram in anagrams:
            words[p] = anagram
            p += 1


# w = ['abdc', 'hey', 'asasas', 'eyh', 'bacd']
# group_anagrams(w)
# print(w)


def sra(items: list, item: int, low: int, high: int) -> int:
    """10.3 helper"""
    if low > high:
        return -1

    mid_idx = (high + low) // 2
    if items[mid_idx] == item:
        return mid_idx
    if high == low:
        return -1

    if items[high] >= items[mid_idx + 1]:
        if items[mid_idx + 1] <= item <= items[high]:
            return sra(items, item, mid_idx + 1, high)
        else:
            return sra(items, item, low, mid_idx)
    else:  # other range is ratzif items[low] <= items[mid_idx]
        if items[low] <= item <= items[mid_idx]:
            return sra(items, item, low, mid_idx)
        else:
            return sra(items, item, mid_idx + 1, high)


def search_in_rotated_array(items: list, item: int) -> int:
    """10.3"""
    if items is None or len(items) == 0:
        return -1
    return sra(items, item, 0, len(items)-1)


# print(search_in_rotated_array([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 160))
# print(search_in_rotated_array([2, 2, 2, 3, 3, 4, 2], 2))


def binary_search(lst: list, x: int, low: int, high: int):
    """10.4 helper"""
    if low > high:
        return -1
    mid_idx = (low + high) // 2
    mid_val = lst[mid_idx]
    if x == mid_val:
        return mid_idx
    if x > mid_val != -1:
        return binary_search(lst, x, mid_idx + 1, high)
    else:
        return binary_search(lst, x, low, mid_idx - 1)


def listys(lst: list, x: int) -> int:
    """10.4"""
    if lst[0] == -1:
        return -1
    low = 0
    high = 1
    found_range = False
    while not found_range:
        if lst[high] == -1 or lst[high] >= x:
            found_range = True
        else:
            low = high
            high *= 2

    return binary_search(lst, x, low, high)


# test = [0, 2, 2, 4, 7, 21, 22, 32, 43, 45, 47, 47, 47, 50, -1, -1, -1, -1, -1, -1]
# print(listys(test, 460))


def sbs(strings: list, word: str, low: int, high: int) -> int:
    """10.5 helper"""
    if low > high:
        return -1
    mid_idx = (low + high) // 2
    mid_val = strings[mid_idx]
    upper_bound = mid_idx
    lower_bound = mid_idx
    if mid_val == '':
        upper_bound += 1
        lower_bound -= 1
        found = False
        while not found:
            if upper_bound > high and lower_bound < low:
                return -1
            if upper_bound <= high and strings[upper_bound] != '':
                mid_idx = upper_bound
                lower_bound += 1
                found = True
            elif lower_bound >= low and strings[lower_bound] != '':
                mid_idx = lower_bound
                found = True
            else:
                upper_bound += 1
                lower_bound -= 1
    mid_val = strings[mid_idx]
    if mid_val == word:
        return mid_idx
    if mid_val > word:
        return sbs(strings, word, low, lower_bound - 1)

    else:
        return sbs(strings, word, upper_bound + 1, high)


def sparse_search(strings: list, word: str) -> int:
    """10.5"""
    if strings is None or len(strings) == 0 or word is None or word == '':
        return -1
    return sbs(strings, word, 0, len(strings)-1)


# print(sparse_search(['', 'as', '', '', 'aa'], 'as'))
# print(sparse_search(['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''], 'at'))


def merge(arr: List[int], helper: List[int], start_idx: int, mid_idx: int, end_idx: int):
    current = start_idx
    left_p = start_idx
    right_p = mid_idx + 1

    for i in range(start_idx, end_idx + 1, 1):
        helper[i] = arr[i]

    while left_p <= mid_idx and right_p <= end_idx:
        if helper[left_p] <= helper[right_p]:
            arr[current] = helper[left_p]
            left_p += 1
        else:
            arr[current] = helper[right_p]
            right_p += 1
        current += 1

    for i in range(mid_idx - left_p + 1):
        arr[current + i] = helper[left_p + i]


def merge_sort(arr: List[int], helper: List[int], start_idx: int, end_idx: int):
    if start_idx < end_idx:
        mid = (start_idx + end_idx) // 2
        merge_sort(arr, helper, start_idx, mid)
        merge_sort(arr, helper, mid + 1, end_idx)
        merge(arr, helper, start_idx, mid, end_idx)


def merge_sort_main(arr: List[int]):
    if arr is None or len(arr) == 0:
        return
    helper = arr[:]
    merge_sort(arr, helper, 0, len(arr) - 1)


# a = [3, 8, 1, 6, 0, 1, 2, 7]
# merge_sort_main(a)
# print(a)
