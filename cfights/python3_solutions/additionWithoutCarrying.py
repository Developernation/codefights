# A little boy is studying arithmetics. He has just learned how to add
# two integers, written one below another, column by column. But he always
# forgets about the important part - carrying.
#
# Given two integers, find the result which the little boy will get.
#
# Note: the boy used this site as the source of knowledge, feel free to
# check it out too if you are not familiar with column addition.

def additionWithoutCarrying(param1, param2):
        p1, p2 = str(param1),str(param2) #string conversion
        len_p1,len_p2 = len(p1),len(p2) #use length for zfill
        len_to_use = 0

        if len_p1 >= len_p2:
                len_to_use = len(p1)
        else:
                len_to_use = len(p2)

        p1_z = p1.zfill(len_to_use) # makes both strings same length
        p2_z = p2.zfill(len_to_use) # makes both strings same length

        totals = list(map(lambda x,y: str(int(x) + int(y)), p1_z,p2_z)) #add each item and convert result to                                                                           #string

        smaller = int(''.join([elm[1] if len(elm) == 2 else elm for elm in totals])) #combines converts final                                                                                        #numbers
        return smaller
