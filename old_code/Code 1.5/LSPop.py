# Populate Google template


def pop_template(template, lsname, players):
    data = dict(
        sorted(players.items(), key=lambda x: x[1]['player name']))
    print(data)
    print(type(data))
    # populate the Funds tabs
    pNameRow = 9
    pNameCol = 3
    pInfoRow = 12
    pInfoCol = 6
    template.sheet1.update_cell(2, 3, lsname)
    for cnt, character in data.items():
        if character['role'] == 'gm':
            template.worksheet('Players').update_cell(
                7, 3, character['player name'])
            template.worksheet('Players').update_cell(
                7, 6, character['email'])
            template.worksheet('Players').update_cell(
                9, 3, character['discord'])
        else:
            template.sheet1.update_cell(
                pNameRow, pNameCol, character['player name'])
            template.worksheet('Players').update_cell(
                pInfoRow, pInfoCol, character['email'])
            template.worksheet('Players').update_cell(
                (pInfoRow + 2), pNameCol, character['discord'])
            pNameRow = pNameRow + 1
            pInfoRow = pInfoRow + 5
