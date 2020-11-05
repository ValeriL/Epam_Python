"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k > len(nums) or not nums or k == 0:
        return 404
    max_sum = nums[0]
    for i in range(1, k + 1):
        for j in range(len(nums) - i + 1):
            max_sum = max(max_sum, sum(nums[j : j + i]))
    return max_sum
