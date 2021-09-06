###############################################################################
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-------------------------------------------------------------------------------
 ###         #########  #########  #########   #########  #########  #########
 ###         ###   ###  ###   ###     ###      ###   ###  ###   ###     ###
 ###         ###   ###  ###   ###     ###      ###   ###  ###   ###     ###
 ###         ###   ###  ###   ###     ###      #########  ###   ###     ###
 ###         ###   ###  ###   ###     ###      ###   ###  ###   ###     ###
 ###         ###   ###  ###   ###     ###      ###   ###  ###   ###     ###
 ##########  #########  #########     ###      #########  #########     ###
-------------------------------------------------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###############################################################################


                             ***LootBot README***


Overview:

    LootBot is a python based Discord bot for tracking inventory in 5e games.
    Developed in an open-source setting, it is a collaborative ever growing
    project overseen by Calvin Todd.  This repository is updated and improved
    from the LootBot_DEPRECIATED repository that is now private.


Project Specs:

    LootBot adheres to PEP8 Python style guide.  The public GitHub repository
    will use a GitHub workflow to enforce testing suite and style/linter
    requirements.  If your pull request clears the GitHub workflow, it will
    then require review from a project maintainer before the submission in to
    the main branch.  If your pull request is rejected by a project maintainer,
    it will have notes provided for changes requested before pull request will
    be submitted for merge.

    If your pull request is not passing the basic tests set forth in the
    workflow and you believe that is in error, please comment on your pull
    request and request a review from a project maintainer.  You request will
    be reviewed as soon as possible.


Testing Specs:

    If adding tests to tests.py please follow the following naming convention:
        -> def test_(method being tested)_(next incremental test number):
    Please ensure your docstring explicitly states what is being tested, and
    what the expected outcome is.  Proposed tests without proper documentation
    will be rejected by project maintainers.


Features:

    ---> Creates and updates custom LootSheet in Google Sheets from the Discord
    char program.
    ---> Track and manage LootSheet in real time
    ---> GM Sheet Locking Ability and Permissions
    ---> Sheet Email Functionality
    ---> Money Conversion Options

Dependencies:
    -> oauth2client
    -> dotenv
    -> discord
    -> asyncio
    -> os.path
    -> asyncio
    -> google.oauth2.credentials
    -> google_auth_oauthlib.flow
    -> google.auth.transport.requests