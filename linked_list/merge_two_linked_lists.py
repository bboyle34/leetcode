#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

hello = "merge_two_linked_lists"

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        inital_value = ListNode()
        """
        while list1 is not None:
            if list1.val < list2.val:
                answer.val = list1.val
                list1 = list1.next
            elif list2.val < list1.val:
                answer.val = list2.val
                list2 = list2.next
            else list1.val == list2.val:
                answer.val = list1.val
                list1 = list1.next
                answer = answer.next
                answer.val = list2.val
                list2 = list2.next
            answer = answer.next
        """
        # initial value will be the linked list we return, but the first value is 0, so return next
        # tail will help us add to the initial value list
        tail = initial_value
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return initial_value.next


if __name__ == "__main__":
    main()
