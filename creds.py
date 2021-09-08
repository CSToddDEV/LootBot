# Author: Calvin Todd
# Project: LootBot - creds.py
# Description : Class for creating credentials for Google Sheets

# Import Statements
from google.oauth2.service_account import Credentials


class SheetsCreds:
    """
    This class is for creating and returning Google API credentials
    """
    def __init__(self):
        """
        This method is the __innit__ for the SheetsCreds class
        """
        self._scopes = ['https://www.googleapis.com/auth/drive',
                        'https://www.googleapis.com/auth/spreadsheets']
        self._creds = self.build_creds()

    def get_scopes(self):
        """
        This method returns self._scopes
        """
        return self._scopes

    def get_creds(self):
        """
        This method returns valid creds or None
        """
        return self._creds

    def set_creds(self, creds):
        """
        This method gets credentials for the Google Sheets API
        """
        self._creds = creds

    def build_creds(self):
        """
        This method returns credentials built from lootbot-sa.json
        """
        creds = Credentials.from_service_account_file('./lootbot-sa.json', scopes=self.get_scopes())
        return creds

    def refresh_creds(self):
        """
        This method refreshes the Service Account credentials
        """
        self.set_creds(self.build_creds())
