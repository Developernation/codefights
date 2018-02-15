def messageFromBinaryCode(c):
        j = 8
        i = 0
        message = ''
        for item in range(len(c)//8):
                message += chr(int(c[i:j],2))
                i += 8
                j += 8
        return message