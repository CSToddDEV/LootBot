# google spreadsheets
import gspread
# authenticator
from oauth2client.service_account import ServiceAccountCredentials


def loot_convert(money):
    money = money.split()
    # print(money)
    gold = 0
    silver = 0
    for loot in money:
        # looks for gold
        if 'gp' in loot:
            gold = loot[:-2]
            gold = int(gold)
    # print(gold)
    # looks for silver
        elif 'sp' in loot:
            silver = loot[:-2]
            silver = int(silver)
    # print(silver)
    # breaks if nothing
        else:
            break
    return gold, silver


def find_player(player):
    # connect
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'lootbot_secret.json', scope)
    client = gspread.authorize(creds)
    # set open SS to sheet
    sheet = client.open('LootBot Test').sheet1
    # find players cell
    cell = sheet.find(player)
    # print(cell.value, cell.row, cell.col)
    row = cell.row
    goldc = cell.col + 1
    silverc = cell.col + 2
    # print(row, goldc, silverc)
    return row, goldc, silverc


def add_money(money, player):
    gold, silver = loot_convert(money)
    # print(gold, silver)
    row, goldc, silverc = find_player(player)
    # print(row, goldc, silverc)
    # connect
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'lootbot_secret.json', scope)
    client = gspread.authorize(creds)
    # set open SS to sheet
    sheet = client.open('LootBot Test').sheet1

    # graps gp and sp from sheet for player, adds funds to it, creats gp/sp
    # variables
    if sheet.cell(row, goldc).value == '':
        gp = gold
    else:
        gp = int(sheet.cell(row, goldc).value) + gold

    if sheet.cell(row, silverc).value == '':
        sp = silver
    else:
        sp = int(sheet.cell(row, silverc).value) + silver
    # print(gp, sp)

    sheet.update_cell(row, goldc, gp)
    sheet.update_cell(row, silverc, sp)
