"""
source: https://leetcode.com/problems/container-with-most-water/description/
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time complexity: O(n)
        # Space complexity: O(1)
        pointer_1 = 0
        pointer_2 = len(height) - 1
        max_area = 0
        while pointer_1 < pointer_2:
            distance = pointer_2 - pointer_1
            current_area = min(height[pointer_1], height[pointer_2]) * distance
            max_area = max(max_area, current_area)
            
            # which pointer to move? The one pointing to the shortest line
            if height[pointer_1] < height[pointer_2]:
                pointer_1 += 1
            else:
                pointer_2 -= 1
        return max_area

if __name__ == "__main__":
    test_cases = (
        # height, expected
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,2], 1),
        ([2,3,4,5,18,17,6], 17),
    )
    for case in test_cases:
        height, expected = case
        assert Solution().maxArea(height) == expected