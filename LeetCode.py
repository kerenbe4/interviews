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


print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


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