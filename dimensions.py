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
        self._end_wall_coords = ['I1', 'J80']
        self._player_loot_column = ['G6', 'I68']
        self._title_bars = [
            ['C1', 'I2'],                        # Top Black Bar
            ['C2', 'I4'],                        # LootSheet Name
            ['C4', 'I5'],                        # Middle Black Bar
            ['C5', 'I7']                         # Item Tracking Sheet
        ]
        self._bottom_bars = [
            ['B68', 'I69'],                      # Top Black Bar
            ['E69', 'I78'],                      # Middle Black Box
            ['B78', 'I80']                       # Bottom Black Bar
        ]

        # Players Sheet Dimensions
        self._player_char_box = ['B22', 'H26']

    # Get Methods
    def get_ls_id(self):
        """
        This method returns the LootSheet ID for the dimensions object
        """
        return self._ls_id

    def get_wall_coords(self):
        """
        This method gets the wall coords
        """
        return self._end_wall_coords

    def get_wall_coord_indexes(self):
        """
        This method returns the coordinate indexes for the wall of the inventory sheet
        """
        coords = self.get_wall_coords()
        start_col_i, start_row_i = self.convert_coord_to_int(coords[0])
        end_col_i, end_row_i = self.convert_coord_to_int(coords[1])

        return start_col_i, end_col_i, start_row_i, end_row_i

    # Set Methods
    def set_wall_coords(self, num_players):
        """
        This method sets the end wall coordinates based on the number of players being
        added to the lootsheet, it then returns the indexes for the new wall coords.
        """
        coords = self.get_wall_coords()

        self._end_wall_coords[0] = self.increase_coord(coords[0], num_players * 2, 0)
        self._end_wall_coords[1] = self.increase_coord(coords[1], num_players * 2, 0)

        return self.convert_coord_to_int(self._end_wall_coords[0])


    # Dimensions Methods
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

    def increase_row_number(self, row_number, to_increase):
        """
        This method increases the row_number (string) passed by the
        to_increase (int) variable and returns the new row number (string)
        """
        return str(int(row_number) + to_increase)

    def increase_column_letter(self, column):
        """
        This method increases the column (list) by 1 and returns it as a list
        """
        # Find index of last column letter
        i = len(column) - 1

        # Handle Z as a column letter and adding a new column letter ( example 'Z' -> 'AA')
        while column[i] == 'Z':
            # Change Z to A
            column[i] = 'A'

            # If there is another letter in the column letter
            if i > 0:
                i -= 1

            # Add leading A if Z was the leftmost column letter and return since will be updated
            else:
                column.insert(0, 'A')
                return column

        # Now increase already existing non-Z column letter by converting to ASCII
        column[i] = chr(ord(column[i]) + 1)
        return column

    def increase_column_letter_times(self, column, increase_by):
        """
        Increases column (list of letters) by increase_by (int)
        """
        i = 0

        while i < increase_by:
            column = self.increase_column_letter(column)
            i += 1

        return column

    def combine_coord(self, column, row):
        """
        This method combines column (list of chars) with row (string) and
        returns them in a string.
        """
        return ''.join(column) + row

    def increase_coord(self, coord, inc_column, inc_row):
        """
        This method increases the coordinate (coord - string) columns by inc_column (int)
        and rows by inc_row (int).  Returns string of new coordinate
        """

        # Split coordinate in to workable parts
        column, row = self.split_coord(coord)

        # Increase column and rows by requested amount
        column = self.increase_column_letter_times(column, inc_column)
        row = self.increase_row_number(row, inc_row)

        # Re-Create coordinate format and return
        return self.combine_coord(column, row)

    def convert_coord_to_int(self, coord):
        """
        This method splits a coordinate in to two different pieces and converts them in to integer
        representation and returns them in [column (int), row (int)] form
        """
        column, row = self.split_coord(coord)

        # Calculate column int
        column_int = 0
        i = len(column) - 1
        power = 0

        while i >= 0:
            column_int += 26**power * (ord(column[i]) - ord('A') + 1)
            i -= 1
            power += 1

        # Adjust column_int for zero-based index
        column_int -= 1

        return column_int, int(row)

    def move_inventory_end_column(self, num_players):
        """
        This method returns the JSON to move the inventory sheet end column
        to accommodate num_players many more player columns
        """
        ls_id = self.get_ls_id()
        start_col_i, end_col_i, start_row_i, end_row_i = self.get_wall_coord_indexes()
        new_col_i, new_row_i = self.set_wall_coords(num_players)

        cut_paste = {
            "source": {
                {
                    "sheetID": int(ls_id["inventory"]),
                    "startRowIndex": int(start_row_i),
                    "endRowIndex": int(end_row_i),
                    "startColumnIndex": int(start_col_i),
                    "endColumnIndex": int(end_col_i)
                }
            },
            "destination": {
                {
                    "sheetID": int(ls_id["inventory"]),
                    "rowIndex": int(new_row_i),
                    "columnIndex": int(new_col_i)
                }
            },
            "pasteType": "PASTE_NORMAL"
        }

        return cut_paste
