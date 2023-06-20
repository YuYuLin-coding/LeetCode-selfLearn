'''
No: 67
Title: Add Binary
Tags: Math, String, Bit Manipulation, Simulation
Difficulty: Easy
Date: 2023-06-15
Link: https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''


class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        new_a_list = list(a)
        new_b_list = list(b)
        a_length = len(new_a_list)
        b_length = len(new_b_list)
        max_length = max(a_length, b_length)
        new_c_list = [0 for _ in range(max_length+1)]  # Adding +1 to handle a potential carry in the final addition

        new_a_list.reverse()
        new_b_list.reverse()

        for i in range(max_length):
            if i < a_length:
                new_c_list[i] += int(new_a_list[i])
            if i < b_length:
                new_c_list[i] += int(new_b_list[i])
            if new_c_list[i] >= 2:
                new_c_list[i] -= 2
                new_c_list[i+1] += 1

        new_c_list.reverse()

        # Remove leading zeros
        while len(new_c_list) > 1 and new_c_list[0] == 0:
            new_c_list.pop(0)

        # Convert the integers in new_c_list to strings to use the join operation
        new_c_list = [str(i) for i in new_c_list]

        return ''.join(new_c_list)
    
    def addBinary(self, a: str, b: str) -> str:
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]