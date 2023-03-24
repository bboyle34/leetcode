#!/usr/bin/env python

def main():
    nums = [4, 2, 1, 1, 1, 1, 3, 3, 3, 2]

    l, r = 0, 1
    count = 1
    remove = False
    same = False
    while r <= len(nums)-1:
        #print("start", count)
        #print(nums[l], nums[r])
        if nums[l] == nums[r]:
            #same = True
            count += 1
            r += 1

        else:
            if count >= 3:
                #list_to_remove = nums[l:r+1]
                list1 = nums[:l] # [4, 2]
                list2 = nums[r:] # [3, 3, 3, 2]
                list1.extend(list2)# remove above lists from nums
                nums = list1
                l, r = 0, 1
                count = 1               
                #print("reset")
            else:
                l = r
                r += 1

    print(nums)

if __name__ == "__main__":
    main()
