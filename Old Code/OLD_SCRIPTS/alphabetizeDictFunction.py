#Alphabetize the player ditionary
from operator import itemgetter

playersdict1 = {1: {'player name': 'Calvin Todd', 'email': 'cstodd88@gmail.com', 'role': 'gm', 'discord': 'LockeX'}, 2: {'player name': 'Lolan Spiritwolf', 'email': 'FreePourPod@gmail.com', 'role': 'player', 'discord': 'LolanS'}, 3: {'player name': 'Locke Orion', 'email': 'lockeorion@gmail.com', 'role': 'player', 'discord': 'Locke'}, 4: {'player name': 'Clockwork Coyote', 'email': 'wallenprog@gmail.com', 'role': 'player', 'discord': 'ClockworkCoyote'}}


def alphabetize_players(players):
    players = sorted(players.items(), key = lambda x: x[1]['player name'])
    print(players)

alphabetize_players(playersdict1)
