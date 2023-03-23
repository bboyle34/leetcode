#!/usr/bin/env python

def isValid(self, s: str) -> bool:
    answer = True
    Map = {"(":")", "{":"}", "[":"]"}
    if len(s) % 2 != 0:
        answer = False
    else:
        for char in range(0, len(s), 2):
            if Map[s[char]] != s[char+1]:
                answer = False
                break
            # assume that the ord of each matching char is +1
            #if ord(s[char]) != ord(s[char+1]) - 1:
            #    answer = False
            #    break
    """
    Map = {")": "(", "}":"{", "]":"["}
    stack = []
    for char in s:
        if char not in Map:
            stack.append(char)
            continue
        if not stack or stack[-1] != Map[char]:
            answer = False
        stack.pop()
    """
    return answer

if __name__ == "__main__":
    main()
