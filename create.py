# Author: Calvin Todd
# Project: LootBot - create.py
# Description : Class for creating a new Loot List

class LootList:
    """
    Loot List created by LootBot
    """
    def __init__(self, ctx):
        """
        Init for LootList
        """
        self._created = True
        self._loot_list_id = self.begin_lootsheet()
        self._templates = ['5e', 'starfinder']
        self._template = None
        self._creator_ctx = ctx

    # Get Functions
    def get_id(self):
        """
        This method returns the Loot List ID
        """
        return self._loot_list_id

    def get_creator_context(self):
        """
        This method returns the ctx for the creating command
        """
        return self._creator_ctx

    def get_available_templates(self):
        """
        This method returns all the available templates for LootBot
        """
        return self._templates

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

    def begin_lootsheet(self):
        """
        This method begins the creation of the new LootSheet
        """
        ctx = self.begin_lootsheet()

        # Set template
        self.set_template(self.request_template(ctx))

        return True

    def request_template(self, ctx):
        """
        This method requests template option from creator
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

