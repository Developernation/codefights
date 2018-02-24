#Author: Developernation
#Date:2/24/2018

from getDriveData import Sheets2Text
from ChimpApiPull import ChimpTastic
'''This program connects to a team drive, allows you to select a spreadsheet from
the team drive, and uses the name of the spreadsheet to create a list of subscribers
in Mailchimp'''
#---------------VARIABLES--------------------------
chmptkn = '<mailchimp token>'
#--------------------------------------------------
#-----------CONSTRUCTORS---------------------------
checkProg = Sheets2Text(verbose=True)
cmpTstic = ChimpTastic(chmptkn)
#--------------------------------------------------

#TODO Connect to google team drive
checkProg.make_drive_auth
checkProg.gsheets_auth
checkProg.get_drive_files
checkProg.search_tdrive()

#TODO Search for spread sheet response lists
selected = input("Select a file: ")
sel_file = checkProg.select_file(selected)[0]
print(sel_file)

#TODO create a list in mailchimp with the same name as the google sheets list

print('Creating ' + sel_file + ' in MailChimp...')
cmpTstic.make_List(sel_file)

cmpTstic.get_ListID
myId = input('list id')
cmpTstic.set_ListID(myId)
#TODO Extract customer info from each list in the google spreadsheet
print('Adding subsribers...')

#TODO Add customer entries to mailchimp in a for loop
cnt = 0
for item in checkProg.getSheet()[2]:
    cmpTstic.add_members(item[1:5])
    cnt += 1

print(str(cnt) + ' subscribers have been added to ' + sel_file +'.')
