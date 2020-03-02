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


c = [1, 1, 7, 10, 12, None, None]
d = [1, 2]
sorted_merge(c, d)
print(c)
