# Find the kth largest element in an unsorted array. This will be the kth
# largest element in sorted order, not the kth distinct element.

def kthLargestElement(nums, k):
    nums.sort()
    return nums[-k]
