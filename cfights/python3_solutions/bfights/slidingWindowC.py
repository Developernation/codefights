#1) Partial solution
def losslessDataCompression(iString, w):
        if len(iString) < 2:
                return iString
        
        result = []
        win = []
        stInd = 0
        for i in range(0,len(iString)):
        
                if i >= w:
                        win = iString[i-w:i]
                        stInd = i-w
                else:
                        win = iString[0:i]
                        
                        print('--------------------------------------------------')
                        print('i: ',i,"inputString: ",iString[i], 'window: ',win)
                        try:
                                if iString[i] in win:
                                        sub_win = win[stInd:i-1]
                                        print(win, sub_win)
                                        print('Found ',iString[i])
                                        #print(sub_win.index(iString[i]),len(sub_win))
                                        result.append((sub_win.index(iString[i]),len(sub_win)))
                                        print(result)
                                        print('--------------------------------------------------')
                                        confusing_thing = iString[stInd:stInd + len(sub_win)-1]
                                        print(len(confusing_thing))
                                        if confusing_thing in win and len(confusing_thing)>0:
                                                print('turd')
                                                print('wierd',iString[stInd:stInd + len(sub_win)],'win', win)
                                                stInd += len(confusing_thing)
                        except:
                                print('...')
        #----------------------------------------------------------------------------------------
                if iString[i] not in win:
                        print('Not ',iString[i])
                        result+=iString[i]
                        print("result: ",result)
                
                        
        
        #startInd = iString.index(win[i],i)
        #win_len = len(win)
        #if iString[i:i + len(iString) - 1] == iString[startInd,startInd + ]
#2) Better partial solution to find length
def losslessDataCompression2(iString, width):
        #----------Variables------------
        result = []
        win = []
        fnd_such_lst = [] #tuples
        i = 1 #current char index
        len_sub_win = 0 #this is the length variable you want to use
        #-------------------------------
        if len(iString) < 2:
                return iString
        if len(list(set(iString))) == len(iString):
                return iString
        #-------------------------------
        while i-1 < len(iString):
                        
                if i < width: #if there are less than width chars before the current one
                        win = iString[0:i-1] #width of chars before the current one
                        len_win = len(win) #length
                        stInd = 0

                else:
                        win = iString[i-width:i-1] #width of chars before the current one
                        len_win = len(win) #length
                        stInd = i-width

                print(iString[stInd:stInd + len_win])
                print(stInd,len_win)
                #find such startIndex and length that.....
                if (iString[i:i + len_win-1] == iString[stInd:stInd + len_win-1]) and iString[stInd:stInd + len_win-1] in win:
                        tupe_to_append = (stInd,len_win)
                        fnd_such_lst.append(tupe_to_append)               
                
                        #---------------------------Eval fnd_such_lst--------------------------------------------
                        max_len = max([fnd_such_lst[i][1] for i in range(len(fnd_such_lst))]) #gets max len
                        max_len_tup = [fnd_such_lst[t] for t in range(len(fnd_such_lst)) if fnd_such_lst[t][1] == max_len]
                        if len(max_len_tup) > 1:
                                min_st = min([fnd_such_lst[i][0] for i in range(len(fnd_such_lst))]) #gets max len
                                select_tup = [tup for tup in fnd_such_lst if tup == (min_st,max_len)][0]
                        else:
                                select_tup = max_len_tup[0]
                        result.append(select_tup)
                        len_sub_win = select_tup[1]
                i += 1