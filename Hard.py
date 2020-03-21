from typing import List


def real_random(i):
    """17.2 helper"""
    return 0


def shuffle(cards: list) -> list:
    """17.2"""
    shuffled_cards = []
    cards_count = len(cards)

    for i in range(cards_count - 1, -1, -1):
        r = real_random(i)
        shuffled_cards.append(cards[r])
        if r != i:
            cards[i], cards[r] = cards[r], cards[i]

    return shuffled_cards


# print(shuffle([1, 2, 3, 4]))


def twos(number: int) -> int:
    """17.5"""
    mul = 1
    total_count = 0
    digits_left = number

    while digits_left > 0:
        count_for_digit = number // (mul * 10)
        current_digit = digits_left % 10
        if current_digit > 2:
            count_for_digit += 1
        total_count += count_for_digit * mul
        if current_digit == 2:
            total_count += number % (mul * 10) - (current_digit * mul)

        digits_left = digits_left // 10
        mul *= 10

    return total_count


# print(twos(20))


class Person:
    """17.8 helper"""
    def __init__(self, ht, wt):
        self.ht = ht
        self.wt = wt

    def can_hold(self, other: 'Person') -> bool:
        return self.ht > other.ht and self.wt > other.wt


def ct(ppl: list, ppl_count: int, current_person_idx: int, last_person_idx: int) -> int:
    """17.8 helper"""
    if current_person_idx >= len(ppl):
        return ppl_count

    max_without_p = ct(ppl, ppl_count, current_person_idx + 1, last_person_idx)
    if last_person_idx == -1 or ppl[last_person_idx].can_hold(ppl[current_person_idx]):
        max_with_p = ct(ppl, ppl_count + 1, current_person_idx + 1, current_person_idx)
    else:
        max_with_p = 0

    return max(max_with_p, max_without_p)


def circus_tower(ppl: list) -> int:
    """17.8 recursive"""
    if ppl is None or len(ppl) == 0:
        return 0

    ppl.sort(key=lambda p: p.ht, reverse=True)
    return ct(ppl, 0, 0, -1)


def circus_tower_dp(ppl: list) -> int:
    """17.8 iterative with memoization"""
    if ppl is None or len(ppl) == 0:
        return 0

    ppl.sort(key=lambda p: p.ht)
    max_ppl_arr = [0] * len(ppl)
    max_ppl_arr[0] = 1
    max_tower = 1

    for i in range(1, len(ppl), 1):
        max_val = 1
        for j in range(i - 1, -1, -1):
            if ppl[i].can_hold(ppl[j]):
                max_val = max(max_val, max_ppl_arr[j] + 1)
        max_ppl_arr[i] = max_val
        max_tower = max(max_tower, max_val)
    return max_tower


# print(circus_tower_dp([Person(1, 100), Person(2, 30), Person(3, 20), Person(4, 5)]))
# ppl1 = [Person(65, 100), Person(70, 150), Person(56, 90), Person(75, 190), Person(60, 95), Person(68, 110)]
# print(circus_tower_dp(ppl1))
# print(circus_tower(ppl1))


def kth_multiple(k: int) -> int:
    """17.9"""
    if k == 0:
        return 1

    three_idx = 0
    five_idx = 0
    seven_idx = 0
    res: List[int] = [1]

    while len(res) < k:
        new_number = min(res[three_idx] * 3, res[five_idx] * 5, res[seven_idx] * 7)
        if new_number == res[three_idx] * 3:
            three_idx += 1
        if new_number == res[five_idx] * 5:
            five_idx += 1
        if new_number == res[seven_idx] * 7:
            seven_idx += 1
        res.append(new_number)

    print(res)
    return res[k - 1]


# print(kth_multiple(25))


def majority_element(nums: list) -> int:
    """17.10"""
    begin_idx = 0
    end_idx = len(nums) - 1

    while begin_idx <= end_idx:
        nums_in_segment = end_idx - begin_idx + 1
        req_elements_for_maj = (nums_in_segment // 2) + 1

        searched_number = nums[begin_idx]
        matched_elements = 0
        unmatched_elements = 0
        i = begin_idx
        while i <= end_idx:
            if nums[i] == searched_number:
                matched_elements += 1
            else:
                unmatched_elements += 1
            if matched_elements == req_elements_for_maj:
                return searched_number
            i += 1
            if unmatched_elements >= matched_elements:
                break

        begin_idx = i

    return -1


# print(majority_element([1, 2, 5, 9, 5, 9, 5, 5, 5]))
# print(majority_element([1, 1, 1, 1, 5, 5, 5, 5, 5]))
# print(majority_element([1, 1, 5, 1, 5, 1, 5, 5, 5]))


class BiNode:
    """17.12 helper"""
    def __init__(self, data, node1=None, node2=None):
        self.node1 = node1
        self.node2 = node2
        self.data = data


def switch(prev, current):
    """17.12 helper"""
    if prev is not None and current is not None:
        prev.node2 = current
        current.node1 = prev


def bst_to_dll(root: BiNode, last_node: BiNode) -> BiNode:
    """17.12 helper"""
    last_node = bst_to_dll(root.node1, last_node) if root.node1 is not None else last_node
    switch(last_node, root)
    last_node = bst_to_dll(root.node2, root) if root.node2 is not None else root
    return last_node


def bi_node(root: BiNode) -> BiNode:
    """17.12"""
    return bst_to_dll(root, None)


# tree = BiNode(4, BiNode(2, BiNode(1), BiNode(3)), BiNode(6, BiNode(5), BiNode(7)))
# res = bi_node(tree)
# while res is not None:
#     print(res.data)
#     res = res.node1
