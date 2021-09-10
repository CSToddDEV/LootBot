# Author: Calvin Todd
# Project: LootBot - text_variables.py
# Description : This file holds the text responses for LootBot

# Text variables for lb.py
text = {
    'lb': {
        'bot_desc':  'LootBot is a Discord bot designed to help manage your Loot and Inventory for Online Table Top '
                     'Role Playing Games!',
        'create_desc': 'The Create Command will request LootBot to create a new LootSheet for use in your online Table '
                       'Top Game!'
    },
    'create': {
        'start_1': 'Check your DMs ',
        'start_2': 'LootBot has just started a new LootSheet with ',
        'start_3': ' LootBot will be unavailable until it is finished.',
        'creator_1': 'Hello! Please wait for directions!',
        'creator_2': 'You will be receiving directions on how to set up your '
                     'LootSheet here shortly.  Please make sure you have all '
                     'your player\'s Character Names, emails, and Discord handles'
                     ' ready.  Also ensure that your GM\'s email account is'
                     ' linked to a Google Account',
        'creator_3': 'Please type **ready** if you are ready to begin your '
                     'Loot Sheet or **stop** to cancel LootSheet creation. '
                     ' NOTE:  LootBot will '
                     'not be available in your channel chat during the '
                     'LootSheet creation process.',
        'template_1': 'Currently LootBot offers two templates for easy LootSheet '
                      'design!\n',
        'template_2': 'You may choose between either a 5e based LootSheet designed for '
                      'Dungeons and Dragons 5th edition games, or a LootSheet designed for '
                      'Starfinder games!\n',
        'template_3': 'Please respond with **5e** for the 5th edition D&D template or '
                      '**starfinder** for the Starfinder template!\n',
        'error': 'Your input was invalid, please try again or type **quit** to quit!\n',
        'email_error': 'Your input does not contain a gmail address which is needed for the LootSheet\n',
        'num_players': 'How many players would you like the LootList set up for?  Do **NOT**\n'
                       'include the DM in this number **Example:** for 4 player characters, respond to this '
                       'message with 4',
        'char_prep': 'Please get ready to input your GM\'s and character\'s information.  You will '
                     'need their character (or GM) name, gmail email address, and full Discord handle\n',
        'gm_request': 'What is your Game Master\'s name, google email, and Discord handle '
                      'seperated by commas.  **Example:** Loot Bot, LootBot@gmail.com, LootBot#1234\n',
        'player_request': 'What is character #{}\'s character name, google email, and '
                          'Discord handle seperated by commas.  **Example:** Frodo Baggins, NotAFanOfEagles@gmail.com, '
                          'Baggins#1234\n',
        'name_request': 'What is the name for your LootSheet, some recommendations '
                        'could be the adventuring party name, or name of the adventure being run!\n',
        'confirm_name': '\n     Your LootSheet\'s name is: **{}**',
        'confirm_gm': '\n\n     Your GM\'s name is: **{}**\n     Your GM\'s email is: **{}**\n     '
                      'Your GM\'s Discord handle is: **{}**',
        'confirm_player': '\n\n     Character #{player}\'s name is: **{name}**\n     Character #{player}\'s '
                          'email is: **{email}**\n     Character #{player}\'s Discord handle is: **{discord}**',
        'confirm_request': '\n\nPlease respond with **correct** if this information is correct, or respond with either '
                           '**name** to change the LootSheet\'s name, **GM** to change the GM\'s information, '
                           'or **character X** where **X** is the corresponding character\'s number you would like to '
                           'change!',
        'creating_ls': '\n\nCreation of the LootSheet, **{}**, has begun!  Please be patient, this will take a '
                       'few minutes.  I will let you know when it is completed!',
        'created_ls': 'The LootSheet, **{}**, has been created!  Please check your email for a link to the LootSheet',
        'description': 'This is a {} LootSheet for {}.',
        'quit': '**(╯°□°）╯︵ ┻━┻**'
    }
}
