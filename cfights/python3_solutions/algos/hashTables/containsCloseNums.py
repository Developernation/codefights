# Given an array of integers nums and an integer k, determine whether there are
# two distinct indices i and j in the array where nums[i] = nums[j] and the
# absolute difference between i and j is less than or equal to k.

def containsCloseNums(nums, k):
    r = []
    s = 0
    for x in nums:
        r.append([x,s])
        s+=1
    r = sorted(r,key=lambda x:x[0])

    for x in range(1,len(r)):
        if r[x][0]==r[x-1][0]:
            if r[x][1]-r[x-1][1] <= k:
                return 1
    return 0
