#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
hello = "three_sum"

def threeSum(self, nums: List[int]) -> List[List[int]]:
    answer = []
    """
    pos = []
    zero = []
    neg = []
    for num in nums:
        if num > 0:
            pos.append(num)
        elif num == 0:
            zero.append(num)
        elif num < 0:
            neg.append(num)
    # pos + zero + neg
    if len(pos) > 0 and len(zero) > 0 and len(neg) > 0:
        for num in pos:
            if num * -1 in neg:
                answer.append([num, 0, num*-1])
    # pos + pos + neg
    if len(pos) > 0 and len(neg) > 0:
        for i in range(len(pos)):
            for j in range(len(pos)):
                if i == j:
                    continue
                target = (pos[i] + pos[j]) * -1
                if target in neg:
                    answer.append([pos[i], pos[j], target]) 
    # pos + neg + neg
    if len(pos) > 0 and len(neg) > 0:
        for i in range(len(neg)):
            for j in range(len(neg)):
                if i == j:
                    continue
                target = (neg[i] + neg[j]) * -1
                if target in pos:
                    answer.append([neg[i], neg[j], target])
    # zero + zero + zero
    """
    res = set()
    # split nums into negative list, positive list, and zero list
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num  == 0:
            z.append(num)
        elif num < 0:
            n.append(num)
    # create a separate set for negatives and positives
    N, P = set(n), set(p)
    # if there is at least 1 zero in the list, add all cases where -1*p in N
    if z:
        for num in P:
            if -1*num in N:
                res.add((-1*num, 0, num))
    # if there are at east 3 zeros in the list, then include that
    if len(z) >= 3:
        res.add((0,0,0))
    # for all pairs of negative numbers, check to see if their positive sum is in P
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            target = -1*(n[i]+n[j])
            if target in P:
                res.add(tuple(sorted([n[i],n[j],target])))
    # for all pairs of positive numbers, check to see if their negative sum is in N
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            target = -1*(p[i]+p[j])
            if target in N:
                res.add(tuple(sorted([p[i], p[j], target])))

    return res

if __name__ == "__main__":
    main()
