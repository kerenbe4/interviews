from collections import deque
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    """https://leetcode.com/problems/min-cost-climbing-stairs/"""
    oneBefore = 0
    twoBefore = 0
    m = 0

    for i in range(len(cost) - 1, -1, -1):
        stairCost = cost[i]
        m = min(stairCost + oneBefore, stairCost + twoBefore)
        twoBefore = oneBefore
        oneBefore = m

    return min(m, twoBefore)


# print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


def maxSubArray(nums: List[int]) -> int:
    """https://leetcode.com/problems/maximum-subarray/"""
    maximumSum = nums[0]
    sum_so_far = 0

    for i in range(len(nums)):
        if sum_so_far < 0:
            sum_so_far = 0
        sum_so_far += nums[i]

        if sum_so_far > maximumSum:
            maximumSum = sum_so_far

    return maximumSum


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTreePartial(nums: List[int], left: int, right: int) -> TreeNode:
    """https://leetcode.com/problems/maximum-binary-tree/ helper"""
    if left > right:
        return None

    max_idx = left
    for i in range(left + 1, right + 1, 1):
        if nums[i] > nums[max_idx]:
            max_idx = i

    root_node = TreeNode(nums[max_idx])
    root_node.left = constructMaximumBinaryTreePartial(nums, left, max_idx - 1)
    root_node.right = constructMaximumBinaryTreePartial(nums, max_idx + 1, right)
    return root_node


def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    """https://leetcode.com/problems/maximum-binary-tree/"""
    return constructMaximumBinaryTreePartial(nums, 0, len(nums) - 1)


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    """https://leetcode.com/problems/all-paths-from-source-to-target/"""
    partial_paths = [[0]]
    paths = []

    while len(partial_paths) > 0:
        pp = partial_paths.pop(0)
        last_node = pp[-1]
        if last_node == len(graph) - 1:
            paths.append(pp)
        next_nodes = graph[last_node]
        for node in next_nodes:
            new_path = pp.copy()
            new_path.append(node)
            partial_paths.append(new_path)

    return paths


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    """https://leetcode.com/problems/all-paths-from-source-to-target/"""
    partial_paths = deque([[0]])
    full_paths = []

    while len(partial_paths) > 0:
        pp = partial_paths.popleft()
        last_node = pp[-1]
        if last_node == len(graph) - 1:
            full_paths.append(pp)
        next_nodes = graph[last_node]
        for node in next_nodes:
            partial_paths.append(pp + [node])

    return full_paths


# grap = [[1, 2], [3], [3], []]
# print(allPathsSourceTarget(grap))


def checkPattern(word: str, pattern: str) -> bool:
    if len(word) != len(pattern):
        return False

    pattern_to_c = {}
    c_to_pattern = {}
    for i in range(len(word)):
        c = word[i]
        p = pattern[i]
        if c in c_to_pattern and c_to_pattern[c] != p:
            return False
        elif p in pattern_to_c and pattern_to_c[p] != c:
            return False
        else:
            pattern_to_c[p] = c
            c_to_pattern[c] = p

    return True


def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
    """https://leetcode.com/problems/find-and-replace-pattern/"""
    """24 ms, faster than 97.40% of Python3 online submissions f .. 14 MB, less than 11.11% of Python3 o"""
    match = []
    for word in words:
        if checkPattern(word, pattern):
            match.append(word)

    return match


def singleNonDuplicate(self, nums: List[int]) -> int:
    """https://leetcode.com/problems/single-element-in-a-sorted-array/"""
    left = 0
    right = len(nums) - 1

    while right > left:
        mid = (left + right) // 2
        if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
            return nums[mid]

        half_items_size = mid - left
        if half_items_size % 2 == 0:
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid - 2
        else:
            if nums[mid] == nums[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1

    if right == left:
        return nums[left]


def minSubArrayLen(s: int, nums: List[int]) -> int:
    """https://leetcode.com/problems/minimum-size-subarray-sum/"""
    min_subarray_size = len(nums) + 1
    tmp_sum = 0
    left = 0

    for right, num in enumerate(nums):
        tmp_sum += num

        while tmp_sum >= s:
            min_subarray_size = min(min_subarray_size, right - left + 1)
            tmp_sum -= nums[left]
            left += 1

    return min_subarray_size if min_subarray_size < len(nums) + 1 else 0


def permute(nums: List[int]) -> List[List[int]]:
    """https://leetcode.com/problems/permutations/"""
    results = [[]]
    for num in nums:
        new_permutations = []
        for partial_permute in results:
            for i in range(len(partial_permute) + 1):
                new_partial_permute = partial_permute[:i] + [num] + partial_permute[i:]
                new_permutations.append(new_partial_permute)
        results = new_permutations
    return results


print(permute([1, 2, 3]))
