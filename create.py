# Author: Calvin Todd
# Project: LootBot - create.py
# Description : Class for creating a new Loot List

# Import Statements
import asyncio
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
        self._started = False
        self._template_chosen = False
        self._template = None
        self._templates = {'5e': '1XjrB13TOj35aBA9Ayq8iHExcHO48xzOi0zEozBMUIA8',
                           'starfinder': '1-SfI8ynZMvH_jjzFOkSfPUwZXjnhS4W7WiFz5iFVxjk'}
        self._ctx = ctx
        self._creator = ctx.message.author
        self._creator_channel = None
        self._loot_list_id = None
        self._bot = bot
        self._creds = SheetsCreds()
        self.text = t['create']

    # Get Functions
    def get_id(self):
        """
        This method returns the Loot List ID
        """
        return self._loot_list_id

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
        return self._creds

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

    # LootSheet Creation Functions
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

        # Step 1 - Choose a template
        elif message.content.lower() == 'ready' and self.get_started() and not self.get_template_chosen():
            await self.request_template()

        # Step 2 - Confirm Template, Add Players
        elif message.content.lower() in self.get_available_templates() and not self.get_template_chosen():
            self.set_template(message.content.lower())
            print(self._template)

        # Quit
        elif message.content.lower() == 'quit':
            await self.quit_message()
            parent_bot.remove_listener(self.received_message, 'on_message')

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


class CreateError(Exception):
    """
    Error class for create.py
    """
    def __init__(self, function, specs):
        if function == 'set_template':
            self._message = 'Error in create.py in function: ' + function + '. [ ' + specs[0] + ' ] is not a valid\
                             template.'
