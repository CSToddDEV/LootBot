# Author: Calvin Todd
# Project: LootBot - player.py
# Description : Classes for players and GMs


class GM:
    """
    This class represents a GM to use with LootSheet
    """
    def __init__(self, char, creds):
        """
        This __init__ function for the GM class
        """
        # Character Info
        self._character = char['info'][0]
        self._email = char['info'][1]
        self._discord = char['info'][2]
        self._party_bot = char['party_bot']

        # LootSheet Info
        self._ls_id = char['ls_id']
        self._ls_name = char['ls_name']
        self._creds = creds

        # Players Page Locations
        self._players_name = char['cells']['players'][0]
        self._players_email = char['cells']['players'][1]
        self._players_discord = char['cells']['players'][2]


class Player(GM):
    """
    This class represents a player/character combination to use with LootSheet
    """
    def __init__(self, char, creds):
        """
        The __init__ function for the Player Class
        """
        # Calls super on GM class
        super().__init__(char, creds)

        # Funds Page Locations
        self._funds_name = char['cells']['funds'][0]

    def get_funds_name_cell(self):
        """
        This method returns self._funds_name
        """
        return self._funds_name


class FifthEditionPlayer(Player):
    """
    This class represents a player/character combination for 5e to use with LootSheet
    """
    def __init__(self, char, creds):
        """
        The __init__ function for the FifthEditionPLayer Class
        """
        # Calls super on Player class
        super().__init__(char, creds)
        self._funds_currency =

    def set_currency_cells(self):
        """
        This method returns the currency cells in the order PP, GP, EP, SP, and CP for
        for the FifthEditionPlayer class
        """


