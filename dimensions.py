# Author: Calvin Todd
# Project: LootBot - dimensions.py
# Description : Classes for LootSheet Dimensions and manipulating them


class Dimensions:
    """
    The parent class for the dimensions object of a LootSheet
    """

    def __init__(self, lootsheet):
        """
        This method is the __init__ for the Dimensions class
        """
        # LootSheet information
        self._ls_id = lootsheet

        # Inventory Sheet Dimensions
        self._end_wall_coords = ['I1', 'I79']
        self._player_loot_column = ['G6', 'H67']
        self._title_bars = [
            ['C1', 'H1'],                        # Top Black Bar
            ['C2', 'H3'],                        # LootSheet Name
            ['C4', 'H4'],                        # Middle Black Bar
            ['C5', 'H6']                         # Item Tracking Sheet
        ]
        self._bottom_bars = [
            ['B68', 'H68'],                      # Top Black Bar
            ['E69', 'H77'],                      # Middle Black Box
            ['B78', 'H79']                       # Bottom Black Bar
        ]

        # Players Sheet Dimensions
        self._player_char_box = ['B22', 'G25']

    def get_ls_id(self):
        """
        This method returns the LootSheet ID for the dimensions object
        """
        return self._ls_id

    def split_coord(self, coord):
        """
        This method splits the coord in to it's alpha (list) and numerical (string) parts
        and returns them
        """
        coord_split = list(coord)
        column_letters = []
        row_numbers = ''

        for value in coord_split:
            if not value.isnumeric():
                column_letters.append(value)
            else:
                row_numbers += value

        return column_letters, row_numbers

