'''
No: 28
Title: Find the Index of the First Occurrence in a String
Tags: Two Pointers, String, String Matching
Difficulty: Easy
Date: 2023-06-14
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        list_of_string = haystack.split(needle)
        if len(list_of_string) == 1:
            return -1
        else:
            return len(list_of_string[0])
