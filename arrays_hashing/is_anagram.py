#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
hello = "is_anagram"

def isAnagram(s: str, t: str, solution) -> bool:
    """
    answer = True
    if len(s) != len(t):
        answer = False
    else:
        for letter in s:
            if letter not in t:
                answer = False
                break
    """
    """ 
    dict1, dict2 = {}, {}
    for item in s:
        dict1[item] = dict1.get(item, 0) + 1
    for item in t:
        dict2[item] = dict2.get(item, 0) + 1
    answer = dict1 == dict2
    
    """
    answer = sorted(s) == sorted(t)

    if answer == solution:
        print("Correct")
        return True
    else:
        print("Incorrect")
        return False


if __name__ == "__main__":
    s, t = "anagram", "nagaram"
    isAnagram(s, t, True)
    x, y = "rat", "car"
    isAnagram(x, y, False)
