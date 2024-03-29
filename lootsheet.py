# Author: Calvin Todd
# Project: LootBot - lootsheet.py
# Description : Class for creating a new Loot List

# Import Statements
import asyncio
from player import GM, FifthEditionPlayer, StarFinderPlayer
from googleapiclient import discovery
from creds import SheetsCreds
from text_variables import text as t


class LootList:
    """
    Loot List created by LootBot
    """
    def __init__(self, ctx, bot):
        """
        Init for LootList
        """
        # Booleans/Attributes for setup
        self._started = False
        self._template_chosen = False
        self._num_players_requested = False
        self._gm_requested = False
        self._name_requested = False
        self._confirmation_requested = False
        self._edit_ls = False
        self._to_edit = None
        self._edit_player_num = 0
        self.text = t['create']

        # Template
        self._template = None
        self._template_type = None
        self._templates = {'5e': '1XjrB13TOj35aBA9Ayq8iHExcHO48xzOi0zEozBMUIA8',
                           'starfinder': '1-SfI8ynZMvH_jjzFOkSfPUwZXjnhS4W7WiFz5iFVxjk'}

        # Creator/Channel Info
        self._ctx = ctx
        self._creator = ctx.message.author
        self._creator_channel = None
        self._bot = bot
        self._creds = SheetsCreds()

        # LootSheet Info
        self._ls_id = None
        self._sheet_ids = {}
        self._players = {}
        self._num_players = 0
        self._recorded_players = 0
        self._ls_info = {'gm': None,
                         'players': [None],
                         'name': None}

    # Get Functions
    def get_id(self):
        """
        This method returns the Loot List ID
        """
        return self._ls_id

    def get_context(self):
        """
        This method returns the ctx for the creating command
        """
        return self._ctx

    def get_available_templates(self):
        """
        This method returns all the available templates for LootBot
        """
        return self._templates

    def get_creator(self):
        """
        This method gets the information of the creator of the LootList
        """
        return self._creator

    def get_bot(self):
        """
        This method returns passed Bot object
        """
        return self._bot

    def get_channel(self):
        """
        This function returns the creator's DM channel once it has been set,
        it will return None if it has not been set.
        """
        return self._creator_channel

    def get_started(self):
        """
        This method returns the boolean of self._started
        """
        return self._started

    def get_template(self):
        """
        This method returns self._template
        """
        return self._template

    def get_template_chosen(self):
        """
        This method returns the boolean fo template chosen
        """
        return self._template_chosen

    def get_creds(self):
        """
        This method returns self._creds
        """
        self._creds.refresh_creds()
        return self._creds.get_creds()

    def get_num_players_requested(self):
        """
        This method returns self._get_num_players_requested
        """
        return self._num_players_requested

    def get_gm_requested(self):
        """
        This method returns self._gm_requested
        """
        return self._gm_requested

    def get_recorded_players(self):
        """
        This method returns self._recorded_players
        """
        return self._recorded_players

    def get_ls_info(self):
        """
        This method returns self._ls_info
        """
        return self._ls_info

    def get_num_players(self):
        """
        This method returns self._num_players
        """
        return self._num_players

    def get_name_requested(self):
        """
        This method returns self._name_requested
        """
        return self._name_requested

    def get_confirmation_requested(self):
        """
        This method returns self._confirmation_requested
        """
        return self._confirmation_requested

    def get_ls_edit(self):
        """
        This method returns self._edit_ls
        """
        return self._edit_ls

    def get_to_edit(self):
        """
        This method returns self._to_edit
        """
        return self._to_edit

    def get_edit_player_num(self):
        """
        This method returns self._edit_player_num
        """
        return self._edit_player_num

    def get_template_type(self):
        """
        This method returns self.template_type
        """
        return self._template_type

    def get_ls_id(self):
        """
        This method returns self._ls_id
        """
        return self._ls_id

    def get_gm_info(self):
        """
        This method returns the dictionary for creating the GM class
        """
        ls_info = self.get_ls_info()
        char = {
            'info': ls_info['gm'],
            'party_chest': False,
            'ls_id': self.get_ls_id(),
            'ls_name': ls_info['name'],
            'cells': {
                'players': ['C7', 'F7', 'C9']
                    }
                }

        return char

    def get_sheet_ids(self):
        """
        This method returns self._sheet_ids
        """
        return self._sheet_ids

    def get_players(self):
        """
        This method returns self._players
        """
        return self._players

    def get_player_info(self, player_num):
        """
        This method returns the dictionary for creating the GM class
        """
        ls_info = self.get_ls_info()
        char = {
            'info': ls_info['players'][player_num],
            'party_chest': False,
            'ls_id': self.get_ls_id(),
            'ls_name': ls_info['name'],
            'cells': {
                'funds': self.get_funds_cells(player_num),
                'players': self.get_players_cells(player_num)
                    }
                }

        return char

    def get_funds_cells(self, player_num):
        """
        This method provides the correct Funds cells based on the passed player_number
        """
        return ['C{}'.format(9 + player_num),          # Name on Funds Page
                'D{}'.format(9 + player_num),          # 5e: Platinum, Starfinder: Credits
                'E{}'.format(9 + player_num),          # 5e: Gold
                'F{}'.format(9 + player_num),          # 5e: Electrum
                'G{}'.format(9 + player_num),          # 5e: Silver
                'H{}'.format(9 + player_num)]          # 5e: Copper

    def get_players_cells(self, player_num):
        """
        This method provides the correct Players cells based on the passed player_number
        """
        return ['C{}'.format(7 + (5 * player_num)),    # Name on Players Page
                'F{}'.format(7 + (5 * player_num)),    # Email on Players Page
                'C{}'.format(9 + (5 * player_num))]    # Discord on Players Page

    def get_party_chest_info(self):
        """
        This method returns the info for the Party Loot Chest
        """
        ls_info = self.get_ls_info()

        char = {
            'info': [None, None, None],
            'party_chest': True,
            'ls_id': self.get_ls_id(),
            'ls_name': ls_info['name'],
            'cells': {
                'funds': self.get_funds_cells(0),
                'players': [None, None, None]
            }
        }

        return char

    # Set Functions
    def set_template(self, template):
        """
        This method sets the private data member self._template with one of the available options:
            -5e (For fifth edition games)
            -starfinder (For Starfinder games)
            -Custom (Coming Soon)
        """
        templates = self.get_available_templates()

        # Check to make sure template is valid selection
        if template not in templates.keys():
            raise CreateError('set_template', [template])
        else:
            self._template = templates[template]
            self._template_chosen = True

    def set_channel(self, channel):
        """
        This method sets the self._creator_channel data member
        """
        self._creator_channel = channel

    def set_started(self):
        """
        This method sets self._started to True
        """
        self._started = True

    def set_creds(self, creds):
        """
        This method creates and sets credentials
        """
        self._creds = creds

    def set_num_players_requested(self):
        """
        This method sets the self._num_players_requested step to True
        """
        self._num_players_requested = True

    def set_gm_requested(self, requested=True):
        """
        This method sets the self._gm_requested to True
        """
        self._gm_requested = requested

    def set_num_players(self, num_players):
        """
        This method sets the number of players **NOT** including the GM
        """
        self._num_players = num_players

    def set_players_recorded(self):
        """
        This method increases the player's recorded by 1
        """
        self._recorded_players += 1

    def set_negative_player_recorded(self):
        """
        This method increases the player's recorded by 1
        """
        self._recorded_players -= 1

    def set_name_requested(self):
        """
        This method sets self._name_requested
        """
        self._name_requested = True

    def set_confirmation_requested(self):
        """
        This method sets self._confirmation_requested
        """
        self._confirmation_requested = True

    def set_name(self, name):
        """
        This method sets the LootSheet's name
        """
        # Get current LootSheet info dictionary
        ls_info = self.get_ls_info()
        # Add name info to dictionary
        ls_info['name'] = name
        self.set_ls_info(ls_info)

    def set_ls_edit(self, needs_edit=False, to_edit=None, player_num=0):
        """
        This method sets the corresponding attributes when editing the LootSheet
        during creation
        """
        self._edit_ls = needs_edit
        self._to_edit = to_edit
        self._edit_player_num = player_num

    def set_edit_player(self, player_number):
        """
        This method sets self._recorded_players
        """
        self._recorded_players = player_number

    def set_ls_info(self, ls):
        """
        This method sets self._ls_info
        """
        self._ls_info = ls

    def set_template_type(self, template_type):
        """
        This method sets self._template_type
        """
        self._template_type = template_type

    def set_ls_id(self, ls_id):
        """
        This method sets self._ls_id
        """
        self._ls_id = ls_id

    def set_sheet_ids(self, creds):
        """
        This method sets the sheet IDs dictionary  as "Sheet Name": "Sheet ID"
        """
        # Get Sheets dicitonary
        sheets = self.get_sheet_ids()

        # Create New service and request data
        service = discovery.build('sheets', 'v4', credentials=creds)
        ls_data = service.spreadsheets().get(spreadsheetId=self.get_ls_id(), ranges=[],
                                             includeGridData=False).execute()

        # Set in dictionary as "Sheet Name" : "Sheet ID"
        for sheet in ls_data['sheets']:
            sheets[sheet['properties']['title']] = sheet['properties']['sheetId']

    def set_player_dict(self, role, player):
        """
        This method sets a player in the player dictionary
        """
        players = self.get_players()
        players[role] = player

    # async Functions
    async def begin_lootsheet(self):
        """
        This method begins the creation of the new LootSheet
        """
        parent_bot = self.get_bot()

        # Start DM and send welcome message
        await self.start_message()

        # Listen for ready signal
        parent_bot.add_listener(self.received_message, 'on_message')

        return True

    async def start_message(self):
        """
        This method starts a DM with _creator and sends messages to the chat/creator with directions
        """
        ctx = self.get_context()
        creator = self.get_creator()

        # Send message to chat channel
        await ctx.send(self.text['start_1'] + creator.mention)
        await ctx.send(self.text['start_2'] + creator.mention + self.text['start_3'])

        # Create channel with _creator
        channel = await creator.create_dm()
        self.set_channel(channel)

        # Send message to _creator
        await channel.send(self.text['creator_1'])
        await asyncio.sleep(2)
        await channel.send(self.text['creator_2'])
        await asyncio.sleep(2)
        await channel.send(self.text['creator_3'])

        # Set _started to True
        self.set_started()

    async def request_template(self):
        """
        This method requests template option from creator
        """
        # Get and send message to _creator channel
        channel = self.get_channel()
        await channel.send(self.text['template_1'])
        await asyncio.sleep(2)
        await channel.send(self.text['template_2'])
        await asyncio.sleep(2)
        await channel.send(self.text['template_3'])

    async def received_message(self, message):
        """
        This method receives messages and processes them according to the message
        """
        parent_bot = self.get_bot()

        # Ensure that the bot is not the one sending the message
        if message.author == parent_bot.user or message.channel != self.get_channel():
            return

        # Quit
        elif message.content.lower() == 'quit':
            await self.quit_message()
            parent_bot.remove_listener(self.received_message, 'on_message')

        # Step 1 - Choose a template
        elif message.content.lower() == 'ready' and self.get_started() and not self.get_template_chosen():
            await self.request_template()

        # Step 2 - Confirm Template, Request Number of Players
        elif message.content.lower() in self.get_available_templates() and not self.get_template_chosen():
            self.set_template(message.content.lower())
            self.set_template_type(message.content.lower())
            await self.number_of_players()

        # Step 3 - Set number of players, Request GM
        elif message.content.isnumeric() and self.get_num_players_requested() and not self.get_gm_requested():
            self.set_num_players(int(message.content))
            await self.request_gm()

        # Step 4 - Process GM, Request First Player
        elif self.get_gm_requested() and self.get_recorded_players() == 0:
            await self.set_gm(message.content)
            await self.request_character()

        # Step 5 - Process Players, Request Next Player
        elif 0 < self.get_recorded_players() < self.get_num_players():
            await self.set_player(message.content)
            await self.request_character()

        # Step 6 - Process Final Player, Request LootSheet Name
        elif self.get_recorded_players() == self.get_num_players() and not self.get_name_requested():
            await self.set_player(message.content)
            self.set_name_requested()
            await self.request_name()

        # Step 7 - Process LootSheet Name, Request Confirmation
        elif self.get_name_requested() and not self.get_confirmation_requested():
            self.set_name(message.content)
            await self.request_confirmation()

        # Step 8.a - Process Changes, Re-Request Confirmation
        elif self.get_confirmation_requested() and message.content.lower() != 'correct' and not self.get_ls_edit():
            await self.record_change(message.content)

        # Step 8.b - Process Changes, Re-Request Confirmation
        elif self.get_ls_edit():
            await self.set_change(message.content)
            await self.request_confirmation()

        # Step 9 - Process Confirmation, Create Lootsheet,
        elif self.get_confirmation_requested() and message.content.lower() == 'correct':
            await self.creating_lootsheet()
            self.create_lootsheet()
            await self.created_lootsheet()

        # Error
        else:
            await self.send_error()

    async def send_error(self):
        """
        This method returns an error to the user if an incorrect input was used
        """
        channel = self.get_channel()
        await channel.send(self.text['error'])

    async def quit_message(self):
        """
        This method returns a quit message
        """
        channel = self.get_channel()
        await channel.send(self.text['quit'])

    async def number_of_players(self):
        """
        This method requests the number of players for the LootSheet
        """
        channel = self.get_channel()
        self.set_num_players_requested()
        await channel.send(self.text['num_players'])

    async def request_gm(self):
        """
        This method requests the GM information for the LootSheet
        """
        channel = self.get_channel()
        self.set_gm_requested()
        await channel.send(self.text['char_prep'])
        await channel.send(self.text['gm_request'])

    async def email_error(self):
        """
        This is called when the response does not contain a gmail address.
        """
        channel = self.get_channel()
        await channel.send(self.text['email_error'])

    async def request_character(self):
        """
        This method requests the character information for the LootSheet
        """
        channel = self.get_channel()
        await channel.send(self.text['player_request'].format((self.get_recorded_players() + 1)))
        self.set_players_recorded()

    async def request_name(self):
        """
        This method requests the name for the LootSheet
        """
        channel = self.get_channel()
        await channel.send(self.text['name_request'])

    async def set_gm(self, message):
        """
        This method sets the GM information in self._ls_info
        """
        # Get current LootSheet info dictionary
        ls_info = self.get_ls_info()

        # Split passed message in to list and strip
        info = message.split(',')
        for data in info:
            data.strip()

        # Error Checking for gmail address
        if '@gmail.com' not in info[1]:
            await self.email_error()
            self.set_gm_requested(False)
            return

        # Add list of info to LootSheet info dictionary
        ls_info['gm'] = info

    async def set_player(self, message):
        """
        This method sets the player information in self._ls_info
        """
        # Get current LootSheet info dictionary
        ls_info = self.get_ls_info()

        # Split passed message in to list and strip
        info = message.split(',')
        for data in info:
            data.strip()

        # Error Checking for gmail address
        if '@gmail.com' not in info[1]:
            await self.email_error()
            self.set_negative_player_recorded()
            return

        # Add list of info to LootSheet info dictionary
        ls_info['players'].append(info)

    async def replace_player(self, message):
        """
        This method replaces the player information in self._ls_info
        """
        # Get current LootSheet info dictionary
        ls_info = self.get_ls_info()

        # Split passed message in to list and strip
        info = message.split(',')
        for data in info:
            data.strip()

        # Error Checking for gmail address
        if '@gmail.com' not in info[1]:
            await self.email_error()
            self.set_negative_player_recorded()
            return

        # Add list of info to LootSheet info dictionary
        ls_info['players'][self.get_edit_player_num()] = info

    async def request_confirmation(self):
        """
        This method requests confirmation for inputted LootSheet info
        """
        channel = self.get_channel()
        self.set_confirmation_requested()
        message = self.construct_confirmation()
        await channel.send(message)
        await channel.send(self.text['confirm_request'])

    async def record_change(self, message):
        """
        This method processes the requested changes.
        """
        # Split message up to the required parts
        request = message.split()
        to_change = request[0]
        if len(request) > 1:
            player_num = int(request[1].strip())
        else:
            player_num = 0

        # Set edit attributes
        self.set_ls_edit(True, to_change, player_num)

        # Send required message message to player to request new info
        if to_change.lower() == 'name':
            await self.request_name()
        elif to_change.lower() == 'gm':
            await self.request_gm()
        elif to_change.lower() == 'character':
            self.set_edit_player(player_num - 1)
            await self.request_character()
            self.set_edit_player(self.get_num_players())
        else:
            await self.send_error()

    async def set_change(self, message):
        """
        This method sets the changes requested by the player during the confirmation process
        """
        ls_info = message
        to_edit = self.get_to_edit()

        # Set info depending on message contents
        if to_edit == 'name':
            self.set_name(ls_info)
        elif to_edit == 'gm':
            await self.set_gm(ls_info)
        elif to_edit == 'character':
            self.set_edit_player(self.get_edit_player_num())
            await self.replace_player(ls_info)
            self.set_edit_player(self.get_num_players())

        # Reset edit info
        self.set_ls_edit()

    async def creating_lootsheet(self):
        """
        This method sends creating LootSheet message
        """
        channel = self.get_channel()
        await channel.send(self.text['creating_ls'].format(self.get_ls_info()['name']))

    async def created_lootsheet(self):
        """
        This method sends finished LootSheet message
        """
        channel = self.get_channel()
        await channel.send(self.text['created_ls'].format(self.get_ls_info()['name']))

    # Non-async Functions
    # noinspection PyUnresolvedReferences
    def construct_confirmation(self):
        """
        This method constructs the confirmation message
        """
        ls_info = self.get_ls_info()
        message = ""
        player_num = 1

        # Construct Name Confirmation
        message += self.text['confirm_name'].format(ls_info['name'])

        # Construct GM Confirmation
        message += self.text['confirm_gm'].format(ls_info['gm'][0], ls_info['gm'][1], ls_info['gm'][2])

        # Construct Player Confirmation
        while player_num <= self.get_num_players():
            message += self.text['confirm_player'].format(player=player_num, name=ls_info['players'][player_num][0],
                                                          email=ls_info['players'][player_num][1],
                                                          discord=ls_info['players'][player_num][2])
            player_num += 1

        return message

    def create_lootsheet(self):
        """
        This method is the parent method for creating the custom LootSheet
        """
        # Fresh Credentials
        credentials = self.get_creds()

        # Create New LS from Template
        new_ls = self.copy_template(credentials)
        self.set_ls_id(new_ls['id'])
        self.set_sheet_ids(credentials)

        # Create GM and Players
        self.create_players(credentials)

        # Modify New LS Dimensions
        self.add_player_dimensions(credentials)

        # Add info to LS

        # Send to Players and GM
        self.assign_to_gm(credentials)

    def create_players(self, creds):
        """
        This method creates and sets the players and GM for the LootSheet
        """
        # Players to add
        player = 0
        total_players = self.get_num_players()

        # Create players and add them to player_dict
        while player <= total_players:
            if player == 0:
                char = self.get_gm_info()
                gm = GM(char, creds)
                self.set_player_dict('gm', gm)
            else:
                char = self.get_player_info(player)
                self.choose_player_class(char, creds, player)

            # Increase Player
            player += 1

        # Create Party Chest and add to player_dict
        char = self.get_party_chest_info()
        self.choose_player_class(char, creds, 'party_chest')

    def copy_template(self, creds):
        """
        This method is creates a new template copy from the selected template
        """
        ls_info = self.get_ls_info()
        new_ls_info = {
            'name': ls_info['name'],
            'description': self.text['description'].format(self.get_template_type(), ls_info['name']),
            'starred': True
        }

        # Copy file and return returned File Resource
        service = discovery.build('drive', 'v3', credentials=creds)
        return service.files().copy(fileId=self.get_template(), body=new_ls_info).execute()

    def choose_player_class(self, char, creds, player_num):
        """
        This method creates the correct player object based on the template (game system) being
        used
        """
        template = self.get_template_type()

        # 5e
        if template == '5e':
            self.set_player_dict('player_{}'.format(player_num),
                                 FifthEditionPlayer(char, creds))

        # Star Finder
        elif template == 'starfinder':
            self.set_player_dict('player_{}'.format(player_num),
                                 StarFinderPlayer(char, creds))

    def assign_to_gm(self, creds):
        """
        This method assigns the GM as the owner of the LS
        """
        players = self.get_players()
        gm = players['gm']

        gm_permissions = {
            'type': 'user',
            'role': 'owner',
            'emailAddress': gm.get_email()
        }

        service = discovery.build('drive', 'v3', credentials=creds)
        service.permissions().create(fileId=self.get_ls_id(),
                                     transferOwnership=True,
                                     body=gm_permissions).execute()

    def add_player_dimensions(self, creds):
        """
        This method adds dimensions to the ls for a new player
        """
        pass


class CreateError(Exception):
    """
    Error class for create.py
    """
    def __init__(self, function, specs):
        if function == 'set_template':
            self._message = 'Error in create.py in function: ' + function + '. [ ' + specs[0] + ' ] is not a valid\
                             template.'
