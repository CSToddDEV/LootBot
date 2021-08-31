# Mods the LootSheet before sending it to players

from __future__ import print_function
import pickle
import os.path
from googleapiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

cellSelect = {
    "requests": [
        {"insertDimension":  # add two columns for player on inventory page
         {"range":
          {"sheetId": 0,
           "dimension": "COLUMNS",
           "startIndex": 8,
           "endIndex": 10
           },
             "inheritFromBefore": False
          }
         },
        {"insertDimension":  # add extra name line on top of funds page
         {"range":
          {"sheetId": 0,
           "dimension": "ROWS",
           "startIndex": 8,
           "endIndex": 9
           },
             "inheritFromBefore": False
          }
         },
        {"insertDimension":  # add Name/Last Change line on Funds Page
         {"range":
          {"sheetId": 0,
           "dimension": "ROWS",
           "startIndex": 13,
           "endIndex": 16
           },
             "inheritFromBefore": False
          }
         },
        {"copyPaste":  # Copy Paste Player on Inventory Page
         {"source":
          {"sheetId": 0,
           "startRowIndex": 5,
           "endRowIndex": 67,
           "startColumnIndex": 6,
           "endColumnIndex": 8
           },
             "destination":
             {"sheetId": 0,
              "startRowIndex": 5,
              "endRowIndex": 67,
              "startColumnIndex": 8,
              "endColumnIndex": 10
              },
             "pasteType": "PASTE_FORMAT",
             "pasteOrientation": "NORMAL"
          }
         },
        {"copyPaste":  # Copy Paste first Player line on funds Page
         {"source":
          {"sheetId": 0,
           "startRowIndex": 10,
           "endRowIndex": 11,
           "startColumnIndex": 2,
           "endColumnIndex": 8
           },
             "destination":
             {"sheetId": 0,
              "startRowIndex": 8,
              "endRowIndex": 9,
              "startColumnIndex": 2,
              "endColumnIndex": 8
              },
             "pasteType": "PASTE_FORMAT",
             "pasteOrientation": "NORMAL"
          }
         },
        {"copyPaste":  # Copy Paste second Player block on funds Page
         {"source":
          {"sheetId": 0,
           "startRowIndex": 16,
           "endRowIndex": 19,
           "startColumnIndex": 2,
           "endColumnIndex": 8
           },
             "destination":
             {"sheetId": 0,
              "startRowIndex": 13,
              "endRowIndex": 16,
              "startColumnIndex": 2,
              "endColumnIndex": 8
              },
             "pasteType": "PASTE_FORMAT",
             "pasteOrientation": "NORMAL"
          }
         },
        {"mergeCells":  # Merge top cells Invnentory Page
         {"range":
          {"sheetId": 0,
           "startRowIndex": 0,
           "endRowIndex": 5,
           "startColumnIndex": 8,
           "endColumnIndex": 10
           },
             "mergeType": "MERGE_ALL"
          }
         },
        {
            "mergeCells":  # Merge bottom black cells inventory page
            {"range":
             {"sheetId": 0,
              "startRowIndex": 67,
              "endRowIndex": 79,
              "startColumnIndex": 8,
              "endColumnIndex": 10
              },
                "mergeType": "MERGE_ALL"
             }
        },
        {"insertDimension":  # add character log lines on Players Page
         {"range":
          {"sheetId": 0,
           "dimension": "ROWS",
           "startIndex": 26,
           "endIndex": 31
           },
          "inheritFromBefore": True
          }
         },
        {"copyPaste":  # Copy Paste second Player block on funds Page
         {"source":
          {"sheetId": 0,
           "startRowIndex": 6,
           "endRowIndex": 11,
           "startColumnIndex": 1,
           "endColumnIndex": 7
           },
          "destination":
          {"sheetId": 0,
           "startRowIndex": 26,
           "endRowIndex": 31,
           "startColumnIndex": 1,
           "endColumnIndex": 7
           },
          "pasteType": "PASTE_FORMAT",
          "pasteOrientation": "NORMAL"
          }
         }
    ]
}


def mod_new_ls(players, sheetid):
    cnt = 3

    psize = -1
    for k, v in players.items():
        psize += 1
    while cnt < psize:
        SCOPES = ['https://www.googleapis.com/auth/drive',
                  'https://www.googleapis.com/auth/spreadsheets']
# store = file.Storage('storage.json')
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)

        SHEET_ID = sheetid

        # function to retrieve SheetID for Inventory SHeet
        ranges = []
        include_grid_data = False
        service = discovery.build('sheets', 'v4', credentials=creds)
        action = service.spreadsheets().get(
            spreadsheetId=SHEET_ID, ranges=ranges,
            includeGridData=include_grid_data)
        shtid = action.execute()
        sheets = shtid.get('sheets', '')
        # Stotes sheet ID as int
        sheet_idI = int(sheets[1].get(
            "properties", {}).get("sheetId", 0))
        sheet_idF = int(sheets[0].get(
            "properties", {}).get("sheetId", 0))
        sheet_idP = int(sheets[3].get(
            "properties", {}).get("sheetId", 0))
        # print(type(sheet_id), sheet_id)
        # inserts sheetID in to dictionary
        cellSelect['requests'][0]['insertDimension']['range']['sheetId'] \
            = sheet_idI
        cellSelect['requests'][1]['insertDimension']['range']['sheetId'] \
            = sheet_idF
        cellSelect['requests'][2]['insertDimension']['range']['sheetId'] \
            = sheet_idF
        cellSelect['requests'][3]['copyPaste']['source']['sheetId'] \
            = sheet_idI
        cellSelect['requests'][3]['copyPaste']['destination']['sheetId'] \
            = sheet_idI
        cellSelect['requests'][4]['copyPaste']['source']['sheetId'] \
            = sheet_idF
        cellSelect['requests'][4]['copyPaste']['destination']['sheetId'] \
            = sheet_idF
        cellSelect['requests'][5]['copyPaste']['source']['sheetId'] \
            = sheet_idF
        cellSelect['requests'][5]['copyPaste']['destination']['sheetId'] \
            = sheet_idF
        cellSelect['requests'][6]['mergeCells']['range']['sheetId'] \
            = sheet_idI
        cellSelect['requests'][7]['mergeCells']['range']['sheetId'] \
            = sheet_idI
        cellSelect['requests'][8]['insertDimension']['range']['sheetId'] \
            = sheet_idP
        cellSelect['requests'][9]['copyPaste']['source']['sheetId'] \
            = sheet_idP
        cellSelect['requests'][9]['copyPaste']['destination']['sheetId'] \
            = sheet_idP

        request = service.spreadsheets().batchUpdate(
            spreadsheetId=SHEET_ID, body=cellSelect)
        request.execute()

        # UPDATE JSON tree values for where the copy/paste and
        # insert dimension flags move too because of the addition of the
        # name line
        cnt = cnt + 1
        cellSelect['requests'][5]['copyPaste']['source']['startRowIndex'] \
            += 1
        cellSelect['requests'][5]['copyPaste']['source']['endRowIndex'] \
            += 1
        cellSelect['requests'][5]['copyPaste']['destination']['startRowIndex'] \
            += 1
        cellSelect['requests'][5]['copyPaste']['destination']['endRowIndex'] \
            += 1
        cellSelect['requests'][2]['insertDimension']['range']['startIndex'] \
            += 1
        cellSelect['requests'][2]['insertDimension']['range']['endIndex'] \
            += 1

    if psize > 3:
        # UPDATE CELLS
        FRValue = 14 + (psize - 3)
        charlogValue = 12
        llValue = 9
        ffvari = 9
        itValue = 6
        itColVal = 'C'
        itColVal2 = ''

        lootline = {'values': [['0', '0', '0', '0', '0']]}

        i = 0
        while i < psize:
            llRange = 'D' + str(llValue)
            req2 = service.spreadsheets().values().update(
                spreadsheetId=SHEET_ID, range=llRange,
                body=lootline, valueInputOption='USER_ENTERED')
            req2.execute()
            llValue += 1
            # increases the range for the funds page when itereated over
            fundform = {'values': [['=C' + str(ffvari), '=D' + str(ffvari),
                                    '=E' + str(ffvari), '=F' +
                                    str(ffvari), '=G'
                                    + str(ffvari), '=H' + str(ffvari)],
                                   ['Last Change:', '0', '0', '0', '0', '0']]}
            FRange = 'C' + str(FRValue) + ':H' + str(FRValue + 1)
            req2 = service.spreadsheets().values().update(
                spreadsheetId=SHEET_ID, range=FRange, body=fundform,
                valueInputOption='USER_ENTERED')
            req2.execute()
            FRValue += 3

            invform = {'values': [['=Funds!C' + str(ffvari)]]}
            itColTot = itColVal2 + itColVal
            itRange = 'Inventory!' + str(itColTot) + str(itValue)
            itRange2 = 'Inventory!' + \
                str(itColTot) + str(itValue + 15)
            itRange3 = 'Inventory!' + \
                str(itColTot) + str(itValue + 38)
            req3 = service.spreadsheets().values().update(
                spreadsheetId=SHEET_ID, range=itRange, body=invform,
                valueInputOption='USER_ENTERED')
            req3.execute()
            req3 = service.spreadsheets().values().update(
                spreadsheetId=SHEET_ID, range=itRange2, body=invform,
                valueInputOption='USER_ENTERED')
            req3.execute()
            req3 = service.spreadsheets().values().update(
                spreadsheetId=SHEET_ID, range=itRange3, body=invform,
                valueInputOption='USER_ENTERED')
            req3.execute()
            if ord(itColVal) != 90:
                itColVal = ord(itColVal) + 2
                itColVal = chr(itColVal)
            elif itColVal2 == '':
                itColVal = 'C'
                itColVal2 = 'A'
            else:
                itColVal = 'C'
                itColVal2 = ord(itColVal2) + 1
                itColVal2 = chr(itColVal2)

            # print(ffvari)
            charlog = {'values': [['Character:', '=Funds!C' + str(
                ffvari), '',  'E-Mail:'], ['', '', '', ''],
                ['Discord:', '', '', '']]}
            charlogRange = 'Players!B' + \
                str(charlogValue) + ':E' + str(charlogValue + 2)
            req4 = service.spreadsheets().values().update(
                spreadsheetId=SHEET_ID, range=charlogRange, body=charlog,
                valueInputOption='USER_ENTERED')
            req4.execute()
            charlogValue += 5

            ffvari += 1

            i += 1

        # update Total Line
        totvalue = 8 + psize
        totRange = 'D' + str(totvalue + 1)
        totLine = {'values': [['=SUM(C9:D' + str(totvalue) + ')', '=SUM(D9:E'
                               + str(totvalue) + ')', '=SUM(E9:F' +
                               str(totvalue) + ')',
                               '=SUM(F9:G' + str(totvalue) + ')',
                               '=SUM(G9:H' + str(totvalue) + ')']]}
        req3 = service.spreadsheets().values().update(
            spreadsheetId=SHEET_ID, range=totRange, body=totLine,
            valueInputOption='USER_ENTERED')
        req3.execute()
