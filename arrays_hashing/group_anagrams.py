#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
hello = "group_anagrams"

def groupAnagrams(strs: list[str], solution) -> list[list[str]]:
        table = {}

        for word in strs:
            sorted_string = ''.join(sorted(word))
            if sorted_string not in table:
                table[sorted_string] = []
            table[sorted_string].append(word)

        answer = list(table.values())
        print("Testing")
        for correct in solution:
            if correct not in answer:
                print("Incorrect")
            else:
                print("Correct")

        return list(table.values())

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    solution = [["bat"],["nat","tan"],["ate","eat","tea"]]
    groupAnagrams(strs, solution)
    strs = [""]
    solution = [[""]]
    groupAnagrams(strs, solution)
    strs = ["a"]
    solution =[["a"]]
    groupAnagrams(strs, solution)
