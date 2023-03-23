#!/usr/bin/env python

def search(self, nums: List[int], target: int) -> int:
    answer = -1
    l, r = 0, len(nums) - 1

    while l <= r:
        middle = l + ((r-1)//2)
        if target == nums[middle]:
            answer = middle
            break
        elif target > nums[middle]:
            l = middle + 1
        elif target < nums[middle]:
            r = middle - 1
    return answer

if __name__ == "__main__":
    main()
