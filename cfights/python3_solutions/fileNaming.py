def fileNaming(names):
    array=[]
    for name in names:
        s=name
        i=1
        while s in array:
            s=name+"("+str(i)+")"
            i+=1
        array.append(s)
    return array