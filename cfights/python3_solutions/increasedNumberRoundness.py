# Define an integer's roundness as the number of trailing zeroes in it.
#
# Given an integer n, check if it's possible to increase n's roundness by
# swapping some pair of its digits.

def increaseNumberRoundness(n):
    n = str(n)[::-1]
    cnt = 0
    while n[cnt] == '0':
        cnt+=1
    if '0' in n[cnt:]:
        return True
    return False
