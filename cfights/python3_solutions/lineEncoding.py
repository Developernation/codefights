#Given a string, return its encoding defined as follows:

#First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
#for example, "aabbbc" is divided into ["aa", "bbb", "c"]
#Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
#for example, substring "bbb" is replaced by "3b"
#Finally, all the new strings are concatenated together in the same order and a new string is returned.

def lineEncoding(f):
    i = 0
    strang = ''
    for ind in range(1,len(f)):
        if f[ind] == f[ind-1]:   
            i += 1
        elif f[ind] != f[ind-1]:
            i += 1
            strang += str(i) + f[ind-1]
            i = 0 
        if ind == len(f)-1:
            i += 1
            strang += str(i) + f[ind]

    y = ''.join(item for item in strang if item is not "1")

    return y  