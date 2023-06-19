'''
No: 94
Title: Binary Tree Inorder Traversal
Tags: Stack, Tree, Depth-First Search, Binary Tree
Difficulty: Easy
Date: 2023-06-18
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []
        current = root

        # First, we traverse to the leftmost node
        while True:
            if current is not None:
                # If the node is not null, we add it to the stack and continue to its left child
                stack.append(current)
                current = current.left
            elif stack:
                # If the node is null, we've reached a leaf node. We get the node at the top of the stack
                current = stack.pop()
                # Append the value of the node to the result list
                result.append(current.val)
                # And move to the right child
                current = current.right
            else:
                break

        return result