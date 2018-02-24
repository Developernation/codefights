import pprint
import json
import re
import requests
import string
from random import shuffle
#https://pypi.python.org/pypi/mailchimp3
from mailchimp3 import MailChimp

class ChimpTastic:
    #headers = requests.utils.default_headers() --optional User Agent field in MailChimp()
    def __init__(self,cmptkn,uname):
        '''useage Token, Username'''
        self.cmptkn = cmptkn
        self.uname = uname
        self.lst_id = ''
        self.cust_name = " "
        self.choice_cust = {}
        self.client = MailChimp(self.cmptkn,self.uname,timeout=10.0)
        self. all_ListIDs = []
        self.name_phone_lst = []
        self.custName_num = []
        self.new_list_id = {'id':None,'name':None}

    @property
    def get_ListID(self):
        '''Veiw all the lists and list ids in a mailchimp. This returns a list of list IDs'''
        i = 1
        all_ListIDs = [item for item in self.client.lists.all(get_all=True, fields="lists.name,lists.id")['lists']]
        #all_ListIDs = [item for item in self.client.lists.all(get_all=True, fields="lists.name,lists.id")['lists']]
        for pairs in all_ListIDs:
            print(i,pairs)
            i+= 1
        self.all_ListIDs = all_ListIDs
        return self.all_ListIDs

    def set_ListID(self,choice_ListID:'number of list ID selection'):
        '''this allows you to set the list within the program. Call get_ListID first. Use it to change lists'''
        if self.all_ListIDs != []:
            try:
                choice_ListID = int(choice_ListID)
            #print(all_ListIDs[int(choice_ListID - 1)]['id'])
            except Exception as e:
                return('Please enter a number.')
            try:
            #all_ListIDs[int(choice_ListID - 1)]['id']
                self.lst_id = self.all_ListIDs[choice_ListID - 1]['id']
                return self.lst_id
            except Exception as e:
                return(str(e))
    @property
    def chimpJson(self):
        '''Write JSON response a file on the local host to prevent too many API calls'''
        jData = self.client.lists.members.all(self.lst_id, get_all=True,fields= """members.email_address,members.id,members.merge_fields""")#LNAME, members.merge_fields.FNAME""")
        with open('json_resp.py','w') as new_jDataPy:
            jDataPy = new_jDataPy.write("jDataPy = " + str(jData))

    @property
    def getDataFromJson(self):
        '''pulls from json file on the local host'''
        from json_resp import jDataPy
        custName_num = []

        for i in range(0,jDataPy['total_items']):
            #email = jDataPy['members'][i]['email_address']
            fname = jDataPy['members'][i]['merge_fields']['FNAME'].title()
            lname= jDataPy['members'][i]['merge_fields']['LNAME'].title()
            phone_num = jDataPy['members'][i]['merge_fields']['MMERGE4']
            phone_numReg ='+1' + ''.join(re.findall(r'[\d]',str(phone_num)))

            if len(phone_numReg) == 12:
                custName_num+=[{fname+' '+lname:phone_numReg}]
            else:
                print(phone_numReg + '-- error: not enought digits')
        #list of dictionaries
        self.custName_num = custName_num
        return custName_num
#-------------------------------------------------------------------------------
    def setCustName(self,name):
        '''select a specific customer by name'''
        self.cust_name = name
#-------------------------------------------------------------------------------
    @property
    def searchCust(self):
        '''search an approximated customer name. The name is set with setCustName'''
        name_phone_lst = []
        for name_phone in self.custName_num:
            if re.findall(self.cust_name,str(name_phone)):
                #creates a list of dictionaries
                name_phone_lst+= [name_phone]
        for pair in enumerate(name_phone_lst,start=1):
            print(pair)
        self.name_phone_lst = name_phone_lst
        return self.name_phone_lst
################################################################################

    def choiceCust(self,choice:'int'):
        '''Select a customer from a list of customers with similar names using
        the number next to thier names.  searCust returns a list of
        approximated names and numbers'''
        try:
            self.choice_num = int(choice)
            self.choice_cust = self.name_phone_lst[choice-1]
            return self.choice_cust
        except Exception as e:
            return str(e)
################################################################################
    @property
    def getNums(self):
        num_lst = []
        for item in [self.choice_cust]:
            # item.values().apppend(num_lst)
            num_lst += item.values()
            #num_lst += item.values()
        return num_lst[0]

    @property
    def getNames(self):
        name_lst = []
        for item in [self.choice_cust]:
            # item.keys().append(name_lst)
            name_lst += item.keys()
        return name_lst[0]

    def make_List(self,list_name):
        '''creates a new list in mailchimp and displays all of the lists'''
        info ={"name":list_name,
                "contact":{"company":"MailChimp",
                "address1":"675 Ponce De Leon Ave NE",
                "address2":"Suite 5000",
                "city":"Atlanta","state":"GA",
                "zip":"30308",
                "country":"US","phone":""},
                "permission_reminder":"You'\''re receiving this email because you signed up for updates about Freddie'\''s newest hats.",
                "campaign_defaults":{"from_name":"Freddie","from_email":"freddie@freddiehats.com","subject":"","language":"en"},
                "email_type_option":True}

        try:
            thing = self.client.lists.create(info)
            #self.get_ListID
            return thing
        except Exception as e:
            print('List creation error: ',e)


    def add_members(self,list_member_info:"list containing email,name,fname,lname,phone number"):
        '''adds a member to a list manually. YOU MUST CALL getListID and then set the ID with set_ListID.
           After the ID is set in set_ListID you can add this method to a for loop and add multiple customers at one time.
           It returns the servers response.'''
        email_address,fname,lname,mmerge4 = list_member_info
        #print(self.lst_id)
        resp = self.client.lists.members.create(self.lst_id,data={
                            'email_address': email_address,
                            'status': 'subscribed',
                            'merge_fields': {
                            'FNAME': fname,
                            'LNAME': lname,
                            'PHONE': mmerge4
                                },
                            })
        return resp


if __name__ == "__main__":
    print('main')
