# Given an integer product, find the 
# smallest positive (i.e. greater than 0) integer 
# the product of whose digits is equal to product. 
# If there is no such integer, return -1 instead.

def digitsProduct(prod):
    from functools import reduce
    for first_elm in range(1,9999):
        first_elm_str = [int(item) for item in str(first_elm)]
        first_elm_prd  = reduce(lambda x, y: x*y, first_elm_str)
        if (first_elm_prd) == prod:
            return(first_elm)
    else:
        return - 1