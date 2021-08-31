# Initialize a Custom Spreadsheet with LootBot
# Manipulate spreadsheets
import gspread
# authenticator
from oauth2client.service_account import ServiceAccountCredentials
# import pop_template function
from LSPop import pop_template
from LSMod import mod_new_ls
from LSid import get_LS_id


def new_loot_sheet(lsname, players):
    # authorize
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        '../../lootbot_secret.json', scope)
    client = gspread.authorize(creds)
    # create LootSheet
    template = client.copy(
        '1XjrB13TOj35aBA9Ayq8iHExcHO48xzOi0zEozBMUIA8',
        title=lsname, copy_permissions=True)
    # Function to get the WOrkseet ID
    sheetid = get_LS_id(template)
    # Build upon template
    mod_new_ls(players, sheetid)
    # populate players to sheet
    pop_template(template, lsname, players)
    # email sheet out, iterates through players dictionary
    for k, v in players.items():
        if v['role'] == 'gm':
            # sends sheet with owner privelege
            template.share(v['email'], perm_type='user', role='owner')
    # else email to player with reader value COULD CHANGE LATER
        else:
            template.share(
                v['email'], perm_type='user', role='reader')
