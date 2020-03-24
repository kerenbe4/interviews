from typing import List


def is_subarray(nums: List[int], x: int) -> bool:
    """Given an array with non-negative numbers, and a number x, check if there is a subarray that sums to x"""
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
    """Given a number x, calc the next bigger number with the same digits. (123->132)"""
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

