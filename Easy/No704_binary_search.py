'''
No: 704
Title: Binary Search
Tags: Array, Binary Search
Difficulty: Easy
Date: 2023-06-28
Link: https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''


from typing import List


class Solution:
    def search1(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1

    def search(self, nums: List[int], target: int) -> int:
        # judge whether target in nums
        if target not in nums:
            return -1
        # consider the single element case
        if len(nums)==1 and target==nums[0]:
            return 0
        # consider the edge element equal case
        left, right = 0, len(nums)-1
        if nums[left]==target:
            return left
        if nums[right]==target:
            return right
        left, right = 0, len(nums)
        while left <right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left