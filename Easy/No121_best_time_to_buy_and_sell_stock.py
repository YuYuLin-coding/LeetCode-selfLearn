'''
No: 121
Title: Best Time to Buy and Sell Stock
Tags: Array, Dynamic Programming
Difficulty: Easy
Date: 2023-06-23
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

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

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''


from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        profit = 0
        max_length = len(prices) - 1
        if max_length:
            for j in range(max_length):
                profit = max(profit, self.each_profit(prices[j:]))
        return profit
    
    def each_profit(self, each_list: List[int]) -> int:
        profit = 0
        each_list_length = len(each_list) - 1
        if each_list_length:
            start_price = each_list[0]
            for i in range(each_list_length):
                if each_list[i+1] > start_price:
                    profit = max(profit, each_list[i+1] - start_price)
        return profit
    
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
