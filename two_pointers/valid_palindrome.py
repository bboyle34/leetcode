#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
# Given a string s, return true if it is a palindrome, or false otherwise.
hello = "valid_palindrome"

def isPalindrome(s: str, solution) -> bool:
    answer =  True
    """
    phrase = ""
    for letter in s:
        if 64 < ord(letter) < 91:
            # its upper case
            phrase += letter.lower()
        elif 96 < ord(letter) < 123:
            phrase += letter
    
    backwards = ""
    for i in range(len(phrase)):
        backwards += phrase[len(phrase)-i-1]

    if backwards == phrase:
        answer = True
    """
    phrase = s
    # i starts at the beginning of prhase, and j starts at the end
    i, j = 0, len(phrase) - 1
    # while i is still less than j
    while i < j: 
        # if i is not alpha numeric character, advance 1
        if not phrase[i].isalnum():
            i += 1
        # if j is not alpha numeric character, advance 1
        elif not phrase[j].isalnum():
            j -= 1
        # both i and j are alpha numeric, so now if they do not match, it is not a palindrome
        elif phrase[i].lower() != phrase[j].lower():
            # if there is one unmatched pair, we exit
            answer = False
            break
        # otherwise the characters matched and we should look to the next pair
        else:
            i, j = i + 1, j - 1

    if answer == solution:
        print("Correct")
    else:
        print("Incorrect")
    return answer

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    solution = True
    isPalindrome(s, solution)
    s = "race a car"
    solution = False
    isPalindrome(s, solution)
    s = " "
    solution = True
    isPalindrome(s, solution)
