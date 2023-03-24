#!/usr/bin/env python

def maxSubArray(self, nums: List[int]) -> int:
    answer = 0
    l, r = 0, 0
    currSum = 0
    while r < len(nums):
        currSum += nums[r]
        answer = max(answer, currSum)
        if currSum < 0:
            currSum = 0
        r += 1
    return answer

if __name__ == "__main__":
    main()
