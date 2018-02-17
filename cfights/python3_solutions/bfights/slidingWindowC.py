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