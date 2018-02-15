# Given some integer, find the maximal number you can 
# obtain by deleting exactly one digit of the given number.

def deleteDigit(n):
    n = str(n)
    last_strang = 0
    for i in range(len(n)):
        strang = ''
        for item in range(len(n)):
            if n.index(n[item],item) != n.index(n[i],i):
                strang+=n[item]

        if last_strang < int(strang):
            last_strang = int(strang)

        strang = ''

    return last_strang