# Author: Calvin Todd
# Project: LootBot - creds.py
# Description : Class for creating credentials for Google Sheets

# Import Statements
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


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
        self._sheet_id = '1XjrB13TOj35aBA9Ayq8iHExcHO48xzOi0zEozBMUIA8'
        self._creds = None

    def get_scopes(self):
        """
        This method returns self._scopes
        """
        return self._scopes

    def get_creds(self):
        """
        This method returns valid creds or None
        """
        creds = self._creds

        if not creds or not creds.valid:
            return None
        else:
            return creds

    def set_creds(self):
        """
        This method gets credentials for the Google Sheets API
        """
        if os.path.exists('lootbot_secret.json'):
            # Return credentials
            self._creds = Credentials.from_authorized_user_file('lootbot_secret.json', self.get_scopes())
        else:
            # Incorrect Secret
            self._creds = None

    def build_token(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.get_scopes())
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.get_scopes())
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
