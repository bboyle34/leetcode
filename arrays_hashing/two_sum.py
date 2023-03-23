#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
hello = "two_sum"

def twoSum(nums: list[int], target: int, solution) -> list[int]:
    answer = []
    """
    for i in range(len(nums)):
        if len(answer) > 0:
            break
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    break
    """
    """
    dict1 = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in dict1:
            answer.append(dict1[r])
            answer.append(i)
            break
        dict1[j] = i
    """
    prev_map = {}
    for i, n in enumerate(nums):
        r = target - n
        if r in prev_map:
            answer = [prev_map[r], i]
            """
            if i == nums.index(r):
                continue
            elif i > nums.index(r):
                answer = [nums.index(r), i]
            else:
                answer = [i, nums.index(r)]
            break
            """
        prev_map[n] = i
            

    if answer == solution:
        print("Correct")
        return True
    else:
        print("Incorrect")
        print(answer, solution)
        return False

if __name__ == "__main__":
    nums, target = [2, 7, 11, 15], 9
    twoSum(nums, target, [0, 1])
    nums, target = [3, 2, 4], 6
    twoSum(nums, target, [1,2])
    nums, target = [3, 3], 6
    twoSum(nums, target, [0, 1])

