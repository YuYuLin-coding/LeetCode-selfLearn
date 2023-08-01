'''
No: 231
Title: Power of Two
Tags: Math, Bit Manipulation, Recursion
Difficulty: Easy
Date: 2023-08-01
Link: https://leetcode.com/problems/power-of-two/

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false

Constraints:

-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        value = bin(n)[2:]
        z = 0
        for i in value:
            z += int(i)
            if z > 1:
                return False
        
        return True

