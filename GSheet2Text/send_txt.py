#sending a text from Twilio
#https://www.twilio.com/docs/libraries/python
#https://twilio-python.readthedocs.io/en/latest/
#https://www.twilio.com/console/sms/getting-started/build/appointment-reminders


from twilio.rest import Client
import twilio.rest.messaging as twilmes
import logging as lg
import time,csv
import os

class Send_Txt:
    def __init__ (self, atkn:'account token as a str', toCell:'cell number as a str', accSID, twlNum):
        self.atkn = atkn
        self.accSID = accSID
        self.twlNum = twlNum
        self.toCell = toCell


    def sendTxt(self,info_msg:'str'):
        '''Uses the Client() class from the twilio package to send a text.
        The usage is Send_Txt.sendTxt("string of data")'''
        try:
            twilioCli = Client(self.accSID,self.atkn)
            self.twilioCli = twilioCli
            x = twilioCli.messages.create(body=info_msg ,from_=self.twlNum, to=self.toCell)
            print(x)
            self.x = x
            print(type(self.x))
        except Exception as e:
            return str(e)

    @property
    def logInfo(self):
        '''logs the sms that was sent to the current working directory. Syntax is Send_Txt.logInfo'''
        with open(os.path.join(os.getcwd(),'msg_log.csv'),'a',newline='') as new_csv:
            myCsv = csv.writer(new_csv)
            myCsv.writerow([self.x.date_created,self.x.to,self.x.from_,self.x.body])

    # @property
    # def msgStatus(self):
    #     #lg.basicConfig(level='DEBUG',filename='test_text.log')
    #     get_lgr = lg.getLogger('send_txt.py')
    #     get_lgr.debug(self.x.status)

#--------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print('main')
