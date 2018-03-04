#-----------------------TASK------------------------
# We want to turn the given integer into a number that has only one non-zero digit
# using a tail rounding approach. This means that at each step we take the last
# non 0 digit of the number and round it to 0 or to 10.
# If it's less than 5 we round it to 0 if it's larger than or equal to 5 we round
# it to 10 (rounding to 10 means increasing the next significant digit by 1).
# The process stops immediately once there is only one non-zero digit left.
#----------------------------------------------------

#TODO: Get the string of the value and reverse it
#TODO: Iterate through it converting each digit to an int
#TODO: Check to see if the digit is greater than four
#TODO: if so make it 0 and add 1 to the next digit
#TODO: if not just make it zero

def rounders(value):
        intVal = [int(elm) for elm in str(value)[::-1]]
        for i in range(len(intVal)-1):
                if intVal[i] > 4:
                        intVal[i] = 0
                        intVal[i+1] += 1
                else:
                        intVal[i] = 0
        return int(''.join([str(elm) for elm in intVal[::-1]]))
