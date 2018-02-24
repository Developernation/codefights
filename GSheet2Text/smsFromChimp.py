from ChimpApiPull import *
from send_txt import *
import re,pprint
'''Main program for sending a custom text using mailchimp data via Twilio'''
#------------------------------------------------------------------------------
#Author: Developernation
#Date:2/24/2018
#-------------------------------------------------------------------------------

chmptkn = '<MailChimp Account Token>'
twilTkn = '<Twilio Token>'

info = """Enter text message here"""

#constructor
cmpTstic = ChimpTastic(chmptkn)

cmpTstic.get_ListID
listID = int(input('enter number of list id: '))
cmpTstic.set_ListID(listID)
cmpTstic.chimpJson



fnames = []
for item in cmpTstic.getDataFromJson:
    pprint.pprint(item)
    for key,value in item.items():
        msgOut = info.format(''.join(re.findall(r'\w+\s',key)).strip())
        print(msgOut)
        print(value)
        obj = Send_Txt(twilTkn,value,'<Twilio account number>')
        obj.sendTxt(msgOut)
        obj.logInfo
