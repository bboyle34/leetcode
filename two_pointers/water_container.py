#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
hello = "water_container"

def maxArea(self, height: List[int]) -> int:
    answer = 0
    """
    water = 0
    f, b = 0, len(height) -1
    while f < b:
        if water > answer:
            answer = water
        if height[f] < height[b]:
            smaller = f
        else:
            smaller = b
        water = height[smaller] * (b-f)
        if smaller == f:
            f += 1
        elif smaller == b:
            b -= 1
    """
    l, r, area = 0, len(height)-1, 0
    while l < r:
        area = max(area, (r-l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return area

if __name__ == "__main__":
    main()
