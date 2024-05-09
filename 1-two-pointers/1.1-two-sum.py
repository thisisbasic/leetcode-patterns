"""
Source: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""
from typing import List

class Solution:

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        # O(n2) solution
        for pointer_1 in range(len(nums)):
            for pointer_2 in range(1, len(nums)):
                if nums[pointer_1] + nums[pointer_2] == target:
                    return [pointer_1 + 1, pointer_2 +1] # solution is 1-indexed


    def twoSumOptimal(self, nums: List[int], target: int) -> List[int]:
        # O(n) solution
        pointer_1 = 0
        pointer_2 = len(nums) - 1
        while pointer_1 < pointer_2:
            sum_ = nums[pointer_1] + nums[pointer_2]
            if sum_ == target:
                return [pointer_1 + 1, pointer_2 + 1] # solution is 1-indexed
            elif sum_ < target:
                pointer_1 += 1
            else:
                pointer_2 -= 1



if __file__ == "__main__":
    test_cases = (
        # (nums, target, expected_output)
        ([2,7,11,15], 9, [1,2]),
        ([2,3,4], 6, [1,3]),
        ([-1,0], -1, [1,2]),
    )
    for case in test_cases:
        nums, target, expected_output = case
        assert Solution().twoSumBruteForce(nums, target) == expected_output
        assert Solution().twoSumOptimal(nums, target) == expected_output