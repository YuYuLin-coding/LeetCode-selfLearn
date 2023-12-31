'''
No: 104
Title: Maximum Depth of Binary Tree
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Difficulty: Easy
Date: 2023-06-21
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.next_depth(root, 0)

    def next_depth(self, root: TreeNode, current_depth: int) -> int:
        if root:
            current_depth = max(self.next_depth(root.left, current_depth+1), self.next_depth(root.right, current_depth+1), current_depth)
        return current_depth
    

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        else: 
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1