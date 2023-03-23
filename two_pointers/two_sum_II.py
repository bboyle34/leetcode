#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
hello = "two_sum_II"

def twoSum(numbers: list[int], target: int, solution) -> list[int]:
    answer = []
    """
    for i in range(len(numbers)):
        r = target - numbers[i]            
        if r in numbers:
            answer.append(i+1)
            answer.append(numbers.index(r)+1)
            break
    """
    nums = numbers
    l, r = 0, len(nums)-1
    while l < r:
        if nums[l] + nums[r] == target:
            answer.extend([l + 1, r + 1])
            break
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            l += 1

    if answer == solution:
        print("Correct")
    else:
        print("Incorrect")

    return answer

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    twoSum(nums, target, [1, 2])
    nums = [2, 3, 4]
    target = 6
    twoSum(nums, target, [1, 3])
    nums = [-1, 0]
    target = -1
    twoSum(nums, target, [1, 2])
