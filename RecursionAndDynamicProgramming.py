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

    all_steps = [0] * (steps+1)
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


print(triple_step_rec(5))
triple_steps_mem(5)
triple_steps(5)
