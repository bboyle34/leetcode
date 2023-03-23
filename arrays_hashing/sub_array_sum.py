#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

hello = "sub_array_sum"

class Solution:
    def subArraySum(self,arr, n, s): 
        #Write your code here
        l, r = 0, 0
        sumi = 0
        ans = []
        while r < n:
            sumi += arr[r]
            if sumi > s:
                while (sumi > s):
                    sumi -= arr[l]
                    l += 1
            if sumi == s:
                ans.extend([l+1, r+1])
                break
            r += 1
        if len(ans) == 0 or s == 0:
            return [-1]
        else:
            return ans
        """
        answer = []
        sorted_arr = sorted(arr)
        l, r = 0, 1
        sumi = []
        while l <= r:
            # start with first
            # if smaller, move to next element
            # expand until larger or equal
            # if larger, remove the first element
            if len(sumi) == 0:
                sumi.append(sorted_arr[0])
                continue
            if r > len(sorted_arr)-1:
                sumi.remove(sorted_arr[r])
                r -= 1
            if sum(sumi) == s:
                answer.extend([l+1, r+1])
                break
            elif sum(sumi) < s:
                sumi.append(sorted_arr[r])
                r += 1
            elif sum(sumi) > s:
                sumi.pop(0)
                l += 1
        return answer
        """

if __name__ == "__main__":
    main()
