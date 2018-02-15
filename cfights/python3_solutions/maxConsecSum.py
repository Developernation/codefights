#Given array of integers, find the maximal possible sum of some of its k consecutive elements.

def arrayMaxConsecutiveSum(inputArray, k):
    max_sum = sum(inputArray[:k])
    cur_sum = max_sum
    for x in range(len(inputArray) - k):
        cur_sum = cur_sum - inputArray[x] + inputArray[x + k]
        max_sum = max(max_sum,cur_sum)
    return max_sum
    