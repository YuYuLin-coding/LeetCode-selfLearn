'''
No: 101
Title: Symmetric Tree
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Difficulty: Easy
Date: 2023-06-20
Link: https://leetcode.com/problems/same-tree/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
'''

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        # Note 1: If both subtrees are empty, then they are mirror images of each other.
        if t1 is None and t2 is None:
            return True
        # Note 2: If only one of the subtree is empty, then they are not mirror images of each other.
        if t1 is None or t2 is None:
            return False
        # Note 3: Two subtrees are mirror images of each other if:
        #         1. Their root values are the same.
        #         2. The right subtree of one tree is a mirror reflection of the left subtree of the other tree.
        #         3. The left subtree of one tree is a mirror reflection of the right subtree of the other tree.
        return (t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
