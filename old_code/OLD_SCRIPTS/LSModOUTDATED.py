#Mods the LootSheet before sending it to players

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os
import discord
import time
from gspread_formatting import *

playersdict1 = {1: {'player name': 'Calvin Todd', 'email': 'cstodd88@gmail.com', 'role': 'gm', 'discord': 'LockeX'}, 2: {'player name': 'Lolan Spiritwolf', 'email': 'FreePourPod@gmail.com', 'role': 'player', 'discord': 'LolanS'}, 3: {'player name': 'Locke Orion', 'email': 'lockeorion@gmail.com', 'role': 'player', 'discord': 'Locke'}, 4: {'player name': 'Clockwork Coyote', 'email': 'wallenprog@gmail.com', 'role': 'player', 'discord': 'ClockworkCoyote'}}

def mod_new_ls(players):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('LootBot_secret.json', scope)
    client = gspread.authorize(creds)
    #set open SS to sheet
    sheet = client.open('Loot Dance Party').worksheet('Inventory')

    data = get_user_entered_format(sheet, 'G6:H67')
    data2 = get_user_entered_format(sheet, 'I')
    print(data2)
    format_cell_range(sheet, "J1:J79", data2)
    cellSelect = {
  "requests": [
     {
      "appendDimension": {
        "sheetId": 1,
        "dimension": "COLUMNS",
        "startColumnIndex": 7,
        "length": 2
      }
    },
    {
      "copyPaste": {
        "source": {
          "sheetId": 1,
          "startRowIndex": 5,
          "endRowIndex": 67,
          "startColumnIndex": 6,
          "endColumnIndex": 8
        },
        "destination": {
          "sheetId": 1,
          "startRowIndex": 5,
          "endRowIndex": 67,
          "startColumnIndex": 8,
          "endColumnIndex": 10
        },
        "pasteType": "PASTE_FORMAT",
        "pasteOrientation": "NORMAL"
      }
    }
  ]
}
    #gspread.models.Spreadsheet(sheet).batch_update(cellSelect)
mod_new_ls(playersdict1)
