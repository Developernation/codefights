#Author: Sim Anderson
#Date: 1/15/2018
#Purpose: To search and access spreadsheets in google drive



import httplib2
import os
from sheets_quickstart import get_credentials
from quickstart import get_credentials
from apiclient import discovery
from oauth2client.file import Storage
from oauth2client.service_account import ServiceAccountCredentials
import pprint
#import pandas as pd
#https://wescpy.blogspot.com/2017/06/managing-team-drives-with-python-and.html
#https://www.any-api.com/googleapis_com/drive/docs/files/drive_files_list
class Sheets2Text:
    def __init__(self,getTdrive=True,includeTdrive=True,verbose=False):
        self.response = None
        self.client = None
        self.DRIVE = None
        self.item_dict = None
        self.getTdrive = getTdrive
        self.includeTdrive = includeTdrive
        self.verbose = verbose
        self.selection_value = ''
        self.SHEETS = None
        self.person_count = 0
    #---------------------------------------------------------------------------
    @property
    def gsheets_auth(self):
        """Shows basic usage of the Google Drive API.
        Creates a Google Sheets API service"""
        #scope = ['https://www.googleapis.com/auth/drive',
        #         'https://www.googleapis.com/auth/spreadsheets']
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
        self.SHEETS = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)
        return self.SHEETS
        #return self.client
    #---------------------------------------------------------------------------
    @property
    def make_drive_auth(self):
        """Gets valid user credentials from storage.
        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
        Returns:
            Validated credentials"""
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        print('******'+credential_dir+'**********')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)

        credential_path = os.path.join(credential_dir,
                                       'drive-python-quickstart.json')
        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            creadentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        self.DRIVE = discovery.build('drive', 'v3', http=http)
        return self.DRIVE
    #-------------------------------------------------------------------------
    @property
    def get_drive_files(self):
        #This is how to list items in a team drive----
        #https://www.any-api.com/googleapis_com/drive/docs/files/drive_files_list
        "This allows you to access drive files. It returns a json response object"
        self.response = self.DRIVE.files().list(supportsTeamDrives=self.getTdrive,
                                        includeTeamDriveItems=self.includeTdrive,fields=
                                        "nextPageToken,files(id, name,mimeType),kind"
                                        ).execute()
        return self.response
    #---------------------------------------------------------------------------
    def search_tdrive(self,in_mimeType='spreadsheet'):
        '''searches all files in the team drive for a string in the in_mimeType
        ex:
            for fle in self.response.get('files', []):
                if 'spreadsheet' in fle.get('mimeType'):
                    item_dict[str(cnt)] = fle.get('name')
        It returns a dictionary where the number of the file is the key
        and the value is a list containing the item name and id'''
        item_dict = {}
        cnt = 1
        for fle in self.response.get('files', []):
            # Process change
            if in_mimeType in fle.get('mimeType') and 'Responses' in fle.get('name'):
                item_dict[str(cnt)] = [fle.get('name'),fle.get('id')]
                if self.verbose:
                    print('{0} Found file: {1:^100s} {2:^20s} '.format(cnt,fle.get('name'), fle.get('id')))
                    cnt += 1
                else:
                    cnt += 1
            #move to the next page
            page_token = self.response.get('nextPageToken', None)
            if page_token is None:
                return "Search Complete"
        self.item_dict = item_dict
        return self.item_dict

    def select_file(self,selection:"string formated number"):
        '''Select an item from the dictionary to read'''
        selection = str(selection)
        if selection in self.item_dict:
            selection_value = self.item_dict[selection]
            self.selection_value = selection_value
            return self.selection_value
        else:
            return "Key not found: {}".format(selection)

    def getSheet(self):
        header = True
        '''Enter a google sheet name to read AFTER getting
        Google Sheets API SERVICE cerdentials'''
        spreadsheetId = self.selection_value[1]
        #gets all of the data from the spreadsheet
        result = self.SHEETS.spreadsheets().values().get(
            spreadsheetId=spreadsheetId,range='A1:F35').execute()
        values = result.get('values', [])
        if not values:
            print('No data found.')
        else:
            #print(self.selection_value[1])
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                if not header:
                    self.person_count += int(row[5])
                header = False
                print(row)
        return [self.person_count,self.selection_value[0]]
        #return values
    @property
    def reset_person_count(self):
        self.person_count = 0
#------------------------TEST-------------------------------
if __name__ == "__main__":
    print('__main__')
    checkProg = Sheets2Text(verbose=True)
    checkProg.make_drive_auth
    checkProg.gsheets_auth
    checkProg.get_drive_files
    checkProg.search_tdrive()
    selected = input("Select a file: ")
    print(checkProg.select_file(selected))
    checkProg.getSheet()
