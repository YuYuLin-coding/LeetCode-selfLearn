'''
No: 844
Title: Backspace String Compare
Tags: Two Pointers, String, Stack, Simulation
Difficulty: Easy
Date: 2023-06-27
Link: https://leetcode.com/problems/backspace-string-compare/

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = []
        for i in s:
            if i != '#':
                new_s.append(i)
            else:
                if new_s:
                    new_s.pop()

        new_t = []
        for j in t:
            if j != '#':
                new_t.append(j)
            else:
                if new_t:
                    new_t.pop()
        return new_s == new_t