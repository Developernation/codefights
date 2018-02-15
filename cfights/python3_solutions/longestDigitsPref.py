#Given a string, output its longest prefix which contains only digits.

def longestDigitsPrefix(ui):
    import re 
    x = re.findall(r'^\d+',ui)
    if len(x) > 0:
        return x[0]
    return ''