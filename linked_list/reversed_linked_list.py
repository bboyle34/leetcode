#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

hello = "reversed_linked_list"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        head_copy = []
        answer = Optional[ListNode]
        for num in head:
            head_copy.append(num)
        head_back = head_copy.reverse()
        for i in range(0, len(head_back)-1):
            answer.add_node(head_back[i+1]. head_back[i])
            
        return answer
        """
        # initialize prev pointer as None
        prev = None
        # initialize the curr pointer as the head
        curr = head
        # run a loop till curr pointers to None
        while curr:
            # initialize next pointer as the next pointer of curr
            next = curr.next
            # assoign the prev pointer to curr's next pointer
            curr.next = prev
            #assign curr to prev, next to curr
            prev = curr
            curr = next
        # return the prec pointer to get the reversed linked list
        return prev

if __name__ == "__main__":
    main()
