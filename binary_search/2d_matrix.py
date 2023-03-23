#!/usr/bin/env python

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    answer = False
    # binary search the rows(m)
    l, r = 0, len(matrix)-1
    row = 0
    while l <= r:
        middle = l + ((r-1)//2)
        if target == matrix[middle][0]:
            answer = True
            break
        elif middle == 0:
            row = matrux[middle]
            break
        elif target < matrix[middle][0]:
            row = matrix[middle]
            r = middle - 1
        elif target > matrix[middle][0]:
            row = matrix[middle]
            l = middle + 1
    # binary search the columns(n)
    l, r = 0, len(row)-1
    while l <= r:
        middle = l + ((r-1)//2)
        if target == row[middle]:
            answer = True
            break
        elif target > row[middle]:
            l = middle + 1
        elif target < row[middle]:
            r = middle - 1

    return answer


if __name__ == "__main__":
    main()
