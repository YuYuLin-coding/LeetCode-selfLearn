'''
No: 136
Title: Single Number
Tags: Array, Bit Manipulation
Difficulty: Easy
Date: 2023-06-25
Link: https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''


from typing import List


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        empty_list = []
        for i in nums:
            if i in empty_list:
                empty_list.remove(i)
            else:
                empty_list.append(i)
        return empty_list[0]
    
    def singleNumber(self, nums: List[int]) -> int:
        if not len(nums): return None
        if len(nums) == 1: return nums[0]

        nums = sorted(nums)
        pointer = 1
        
        while pointer < len(nums):
            if nums[pointer] == nums[pointer-1]:
                pointer += 2
            else:
                return nums[pointer-1]

        if nums[-1] != nums[-2]:
            return nums[-1]
