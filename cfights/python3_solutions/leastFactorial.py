# Given an integer n, find the minimal k such that

# k = m! (where m! = 1 * 2 * ... * m) for some integer m;
# k >= n.
# In other words, find the smallest factorial which is not less than n.

def leastFactorial(n):
    x = 1
    for k in range(1,n+1):
        x*=k
        if x >= n:
            return x