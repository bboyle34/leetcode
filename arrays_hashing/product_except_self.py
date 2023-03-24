#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

hello = "product_except_self"

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ log(n^2)
        answer = []
        for k, v in enumerate(nums):
            count = 1
            for i, j in enumerate(nums):
                if k == i:
                    continue
                else:
                    count = count * j
            answer.append(count)
        return answer
        """
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result

if __name__ == "__main__":
    main()
