# A string is said to be beautiful if b occurs 
# in it no more times than a; c occurs in it no more times than b; etc.
# Given a string, check whether it is beautiful.

def isBeautifulString(ui):
    from collections import Counter
    from collections import OrderedDict
    from string import ascii_lowercase as al
    let = al
    dict_al = {letter:0 for letter in let}
    for item in ui:
        dict_al[item] += 1
    x = OrderedDict(sorted(Counter(dict_al).items(), key=lambda t: t[0]))
    return [val for val in x.values()] == sorted((val for val in x.values()),reverse=True)
