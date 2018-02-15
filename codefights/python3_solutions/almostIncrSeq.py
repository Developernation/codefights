def almostIncreasingSequence(sequence):

    count = 0
    if len(sequence) < 2: 
        return True
    if len(sequence) == 2:
        return True
    for i in range(len(sequence)):
        if i == 0:
            if sequence[i] >= sequence[i+1]:
                count += 1
        elif i !=0 and i != (len(sequence)-1):
            if sequence[i] >= sequence[i+1]:
                count +=1 
                if i != (len(sequence)-2):
                    if sequence[i] >= sequence[i+2] and sequence[i+1] <= sequence[i-1]:
                        count += 1
        elif i == len(sequence)-1:
            break
    if count <2:
        return True
    elif count >= 2:
        return False
        
        

