"""
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        l = r = 0
        max_profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                local_profit = prices[r] - prices[l]
                max_profit = max(max_profit, local_profit)
            # means we found a better buy price
            else:
                l = r
            r += 1
        return max_profit



if __name__ == "__main__":
    test_cases = (
        # prices, expected
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
    )
    for case in test_cases:
        nums, expected = case
        assert Solution().maxProfit(nums) == expected
        assert Solution().maxProfit2(nums) == expected
