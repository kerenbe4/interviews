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


print(permutations_with_dups('abc'))
