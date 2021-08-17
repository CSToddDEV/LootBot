# os is for path for getenv
import os
# dotenv reads valu-key pairs from .env
from dotenv import load_dotenv
#authenticator
from oauth2client.service_account import ServiceAccountCredentials
# google spreadsheets
import gspread

#connects to sheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('LootBot_secret.json', scope)
client = gspread.authorize(creds)

def copy_transfer_template(gmemail, lsname) :
    template = client.copy('1XjrB13TOj35aBA9Ayq8iHExcHO48xzOi0zEozBMUIA8', title=lsname, copy_permissions=True)
    template.share(gmemail, perm_type='user', role='owner')

copy_transfer_template('lockeorion@gmail.com', 'TESTTESTTEST')

#fundsTemp = client.open('Copy of LootSheet Template').sheet1
#invTemp = client.open('Copy of LootSheet Template').Inventory
#clTemp = client.open('Copy of LootSheet Template').Change
#playersTemp = client.open('Copy of LootSheet Template').Players

#data1 = fundsTemp.get_all_records()
#data2 = invTemp.get_all_records()
#data3 = clTemp.get_all_records()
#data4 = playersTemp.get_all_records()

#print(fundsTemp, invTemp, clTemp, playersTemp, data1, data2, data3, data4)
