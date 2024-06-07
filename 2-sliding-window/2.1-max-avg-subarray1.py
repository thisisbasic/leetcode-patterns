"""
source: https://leetcode.com/problems/maximum-average-subarray-i/description/

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        p1 = 0
        max_avg = float('-inf')
        current_window_sum = 0
        for p2 in range(len(nums)):
            current_window_sum += nums[p2]
            # calculate the avg if the window is equal to K
            if p2 - p1 + 1 == k:
                max_avg = max(max_avg, current_window_sum / k)
                current_window_sum -= nums[p1]
                p1 += 1
        return max_avg


if __name__ == "__main__":
    test_cases = (
        # nums, k, expected
        ([1,12,-5,-6,50,3], 4, 12.75000),
        ([5], 1, 5.00000),
    )
    for case in test_cases:
        nums, k, expected = case
        assert Solution().findMaxAverage(nums, k) == expected