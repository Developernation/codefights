# You're given an arbitrary 32-bit integer n. Take its binary representation, split bits into it in pairs 
# (bit number 0 and 1, bit number 2 and 3, etc.) and swap bits in each pair. 
# Then return the result as a decimal number.

def swapAdjacentBits(n):
    return int(''.join(['{0:b}'.format(n).zfill(32)[i-2:i][::-1] for i in range(2,33,2)]),2)