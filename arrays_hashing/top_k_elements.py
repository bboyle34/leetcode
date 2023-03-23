#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
hello = "top_k_elements"

def topKFrequent(nums: list[int], k: int, solution) -> list[int]:
    #answer = []
    #test = {}
    #for i in range(len(nums)):
    #    if nums[i] in list(test.keys()):
    #        continue
    #    test[nums[i]] = 1
    #    for j in range(len(nums)):
    #        #print(i, j)
    #        #print(nums.index(i), nums.index(j))
    #        if i == j:
    #            continue
    #        elif nums[i] == nums[j]:
    #            test[nums[i]] += 1
    #
    #desired_list = list(sorted(test.values(), reverse=True))
    #reordered = {k: test[k] for k in desired_list}
    #for result in range(k):
    #    answer.append(reordered[result])
    #for i in test:
    #    if len(answer) == 0:
    #        answer.append(i)
    #    for j in range(len(answer)):
    #        if test[i] > answer[j]:
    #            answer.insert(j, i)
    #        else:
    #            answer.append(i)
    frequency = {}

    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] = frequency[num] + 1
    frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
    answer = list(frequency.keys())[:k]

    if answer == solution:
        print("Correct")
    else:
        print("Incorred")
    
    return answer

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    topKFrequent(nums, k, [1, 2])
    nums [1]
    k = 1
    topKFrequent(nums, k, [1])
