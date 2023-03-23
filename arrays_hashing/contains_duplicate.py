#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
hello = "contains_duplicate"

def containsDuplicate(nums: list[int], solution: bool) -> bool:
    answer = False
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            elif nums[i] == nums[j]:
                answer = True
                break
    """
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            answer = True
            break
    if answer == solution:
        print("Correct")
        return True
    else:
        print("Incorrect")
        return False

if __name__ == "__main__":
    print(hello)
    nums1 = [1, 2, 3, 1]
    containsDuplicate(nums1, True)
    nums2 = [1, 2, 3, 4]
    containsDuplicate(nums2, False)
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    containsDuplicate(nums3, True)
