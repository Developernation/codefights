import getDriveData
import send_txt
'''This program sends a text notification of how many registrations
are in this spreadsheet associated with a google form. Modification may be
necessary depending on the layout of your google spreadsheet'''
#------send_txt variables--------
tkn = '<add twilio_token_here>'
phone_number = '<add phone number here>'

checkProg = getDriveData.Sheets2Text(verbose=True)
checkProg.make_drive_auth
checkProg.gsheets_auth
checkProg.get_drive_files
response_sheets = checkProg.search_tdrive()
print(len(response_sheets))
for selected in range(1,len(response_sheets)+1):
    print(checkProg.select_file(selected))
    total_students = checkProg.getSheet()

    print(total_students[0])
    if total_students[0] >= 15:
        notification = send_txt.Send_Txt(tkn,phone_number)
        notification.sendTxt('<add message here>')
        checkProg.reset_person_count
