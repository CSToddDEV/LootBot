# Author: Calvin Todd
# Project: LootBot - lb.py
# Description : The main file for the LootBot class

# Imports
import os
from dotenv import load_dotenv
from discord.ext import commands
from text_variables import text as t
from create import LootList


class LootBot:
    """
    Class for the LootBot Discord bot.
    """

    def __init__(self):
        """
        Init for LootBot.
        """
        # Load local .env variables in to environment
        load_dotenv()

        self._disc_token = os.getenv("DISCORD_TOKEN")
        self._bot = commands.Bot(command_prefix='$$', description=t.lb.bot_desc)

    def get_disc_token(self):
        """
        This method returns the Discord Token retrieved from the .env file
        """
        return self._disc_token

    def get_bot(self):
        """
        This method returns the Python Discord bot object
        """
        return self._bot

    def bot(self):
        """
        This method holds the async/await for the bot
        """
        bot = self.get_bot()

        # Async calls
        @self._bot.command(name='create', description=t.lb.create_desc)
        async def handle_create_loot_list(ctx):
            """
            This is a handler method
            """
            self.create_loot_list(ctx)

    def create_loot_list(self, ctx):
        """
        This is a handler method
        """
        loot_list = LootList(ctx)

        # Return Loot List ID
        return loot_list.get_id()

