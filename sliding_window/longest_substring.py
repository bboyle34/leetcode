#!/usr/bin/env python
def lengthOfLongestSubstring(self, s: str) -> int:
    answer = 0
    """
    count = 0
    prev_letter = ""
    prev_phrase = []
    for k, v in enumerate(s):
        if v not in prev_phrase:
            count += 1
            prev_phrase.append(v)
        else:
            if count > answer:
                answer = count
            count = 0
            prev_phrase = []
    """
    """
    seen = {}
    l = 0
    output = 0
    for k, v in enumerate(s):
        # if v not in seen, we can keep increasing the window size by moving the right pointer
        if v not in seen:
            answer = max(answer, k-l+1)
        # there are two cases if k is in seen
        else:
            # if v is inside the current window, change left pointer to  seen[v] + 1     
            if seen[v] < l:
                answer = max(answer, k-l+1)
            # if v is not inside the current window, we can keep increasing the window
            else:
                l = seen[v] + 1
        seen[v] = k
    """
    charSet = set()
    l = 0
    for k, v in enumerate(s):
        while v in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(v)
        answer = max(answer, len(charSet))

    return answer


if __name__ == "__main__":
    main()
