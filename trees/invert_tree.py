#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

hello = "invert_tree"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #mover = root
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right =  temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == "__main__":
    main()
