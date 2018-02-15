# You're given two integers, n and m. 
# Find position of the rightmost pair of equal bits in their
# binary representations (it is guaranteed that such a pair exists), 
# counting from right to left.

# Return the value of 2position_of_the_found_pair (0-based).

def equalPairOfBits(n, m):
    return [2**i for i in range(len(bin(n)[2:].zfill(len(bin(max(n,m)))))) if bin(n)[2:].zfill(len(bin(max(n,m))))[::-1][i] == bin(m)[2:].zfill(len(bin(max(n,m))))[::-1][i]][0]