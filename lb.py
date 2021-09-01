# Author: Calvin Todd
# Project: LootBot - lb.py
# Description : The main file for the LootBot class

# Imports
import os
from dotenv import load_dotenv
import discord.ext as d
import text_variables as t
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
        self._bot = d.commands.Bot(command_prefix='$$', help_command='??', description=t.description)

        # Async calls
        @self._bot.command(name='create')
        async def create_loot_list(ctx):
            """
            LootBot creates a new Loot List
            """
            loot_list = LootList()

    def get_disc_token(self):
        """
        This method returns the Discord Token retrieved from the .env file
        """
        return self._disc_token

    def get_bot(self):
        """
        This method returns the Discord Bot object
        """
        return self._bot
