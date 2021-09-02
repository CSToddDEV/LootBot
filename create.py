# Author: Calvin Todd
# Project: LootBot - create.py
# Description : Class for creating a new Loot List

# Import Statements
import asyncio
from text_variables import text as t


class LootList:
    """
    Loot List created by LootBot
    """
    def __init__(self, ctx, bot):
        """
        Init for LootList
        """
        self._created = True
        self._templates = ['5e', 'starfinder']
        self._template = None
        self._ctx = ctx
        self._creator = ctx.message.author
        self._loot_list_id = 666
        self._bot = bot
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
        if template not in templates:
            raise CreateError('set_template', [template])
        else:
            self._template = template

    async def begin_lootsheet(self):
        """
        This method begins the creation of the new LootSheet
        """
        parent_bot = self.get_bot()

        # Start DM and send welcome message
        await self.start_message()

        # Listen for ready signal
        parent_bot.add_listener(self.received_message, 'on_message')

        # Set template
        self.set_template(self.request_template())

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

        # Send message to _creator
        channel = await creator.create_dm()
        await channel.send(self.text['creator_1'])
        await asyncio.sleep(2)
        await channel.send(self.text['creator_2'])
        await asyncio.sleep(2)
        await channel.send(self.text['creator_3'])

    def request_template(self):
        """
        This method requests template option from creator
        """
        return '5e'

    async def received_message(self, message):
        """
        This method receives messages and processes them according to the message
        """
        if message.content.lower() == 'ready':



class CreateError(Exception):
    """
    Error class for create.py
    """
    def __init__(self, function, specs):
        if function == 'set_template':
            self._message = 'Error in create.py in function: ' + function + '. [ ' + specs[0] + ' ] is not a valid\
                             template.'
