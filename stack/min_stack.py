#!/usr/bin/env python

class MinStack:

    def __init__(self):
        self.my_list = []

    def push(self, val: int) -> None:
        self.my_list.append(val)
        return None        

    def pop(self) -> None:
        self.my_list.pop()
        return None        

    def top(self) -> int:
        return self.my_list[len(self.my_list)-1]        

    def getMin(self) -> int:
        return min(self.my_list)

if __name__ == "__main__":
    main()
