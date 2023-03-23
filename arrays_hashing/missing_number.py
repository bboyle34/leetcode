#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

hello = "missing_number"

class Solution:
    def MissingNumber(self,array,n):
        # code here
        for i in range(1, n+1):
            if i not in array:
                return i
        return -1

if __name__ == "__main__":
    main()
