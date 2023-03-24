#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

hello = "max_depth"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0
        """
        while root:
            #parent = root
            answer += 1
            if root.left:
                root = root.left
            if root.right:
                root = root.right
            else:
                root = parent
        return answer
        """
        if not root:
            return 0
        return 1 + (max(self.maxDepth(root.left), self.maxDepth(root.right)))

if __name__ == "__main__":
    main()
