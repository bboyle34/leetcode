#!/usr/bin/env python

def trap(self, height: List[int]) -> int:
    answer = 0
    # for each node, move left and right and find where  min(l and r are greater than node)
    # then move right to R
    # when l moves, r needs to move to a higher value or equal
    for i in range(1, len(height)-1):
        left = max(height[:i])
        right = max(height[i+1:])
        if left < height[i] or right < height[i]:
            continue
        diff = min(left, right)
        answer += diff - height[i]
    return answer

if __name__ == "__main__":
    main()
