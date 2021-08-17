# os is for path for getenv
import os
# dotenv reads valu-key pairs from .env
from dotenv import load_dotenv
# bot commands
from discord.ext import commands
# lootsheet
from LootSheet import add_money
from LSInit import new_loot_sheet
# LSBegin
# sfrom LSBegin import *
import random
from word2number import w2n
import time
from LBTextVariables import *
# gets the value pair from .env file in the SAME directory

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


# sets bot command preface to "-"
bot = commands.Bot(command_prefix='$')

# bot will begin event on -add command
@bot.command(name='add')
# define the ayncronous event looking for message
async def add_command(ctx, money, player):
    # add the sent message to memory, must use " " if there are spaces
    data = money + ' to ' + player
    response = data
    # print(money)
#    print(player)
    add_money(money, player)
    await ctx.send("You have asked to add " + response)

# -start command for creating sheet
@bot.command(name='start')
async def start_ls(ctx):
    member = ctx.message.author
    mainChan = ctx.send
    await ctx.send('Check your DMs {0.author.mention}'.format(ctx.message))
    LBmess = ctx.send('LootBot has just started a new LootSheet with'
                      + ' {0.author.mention}.'.format(ctx.message)
                        + 'LootBot will be unavailable until it is finished.')
    content = 'Hello! Please wait for directions!'
    content2 = ('You will be recieving directions on how to set up your '
                + 'LootSheet here shortly.  Please make sure you have all '
                + 'your player\'s Character Names, emails, and Discord handles'
                + ' ready.  Also ensure that your GM\'s email account is'
                + ' linked to a Google Account')
    content3 = ('Please type \'ready\' if you are ready to begin your '
                + 'Loot Sheet or \'stop\' to cancel LootSheet creation. '
                + ' NOTE:  Lootbot will '
                + 'not be available in your channel chat during the '
                + 'LootSheet creation process.')
    channel = await member.create_dm()
    await channel.send(content)
    time.sleep(3)
    await channel.send(content2)
    time.sleep(3)
    await channel.send(content3)
    dmChanID = channel.id
    lsname = ""
    pnum = 0
    cnt = 1
    plyr = 1
    players = {}
    rdy = False
    Test = bot.event
    chatChan = False
    @Test
    async def on_message(message):
        nonlocal lsname
        nonlocal pnum
        nonlocal cnt
        nonlocal players
        nonlocal plyr
        nonlocal dmChanID
        nonlocal rdy
        nonlocal chatChan
        nonlocal mainChan
        nonlocal member
        if message.author == bot.user:
            return
        if message.channel.id != dmChanID and chatChan is False:
            return
        elif message.content.lower() == 'stop':
            await channel.send('(╯°□°）╯︵ ┻━┻')
            rdy = False
            chatChan = True
            return
        elif message.content.lower() == 'ready':
            rdy = True
            await channel.send('What would you like to name your LootSheet?')
            await LBmess
        elif lsname == "" and rdy is True:
            lsname = message.content
            await channel.send('Your LootSheet\'s name is '
                               + lsname
                               + '.  How many players do you have '
                               + '(including your GM)?')
        elif pnum == 0 and rdy is True:
            try:
                pnum = int(message.content)
                await channel.send('Please enter the GM\'s name')
            except ValueError:
                try:
                    pnum = message.content
                    pnum = w2n.word_to_num(pnum)
                    await channel.send('Please enter the GM\'s name')
                except ValueError:
                    pnum = 0
                    await channel.send('Your number was not accepted'
                                       + ' please try again')
        elif plyr <= pnum and rdy is True:
            if cnt == 1:
                gmname = str(message.content)
                players[plyr] = {}
                players[plyr]['player name'] = gmname
                players[plyr]['role'] = 'gm'
                cnt = cnt + 1
                await channel.send('Please enter ' + gmname + '\'s email and '
                                   + 'Discord handle seperated by a comma. '
                                   + ' Please do not add '
                                   + 'the @ before the Discord handle. '
                                   + ' Example: name@name.com, '
                                   + 'username#1234')
            elif cnt == 2:
                lst = str(message.content)
                if ',' and '#' in lst:
                    lst = lst.split(',')
                    players[plyr]['email'] = lst[0]
                    if lst[1][0] == ' ':
                        players[plyr]['discord'] = lst[1][1:]
                    else:
                        players[plyr]['discord'] = lst[1]
                    cnt += 1
                    plyr += 1
                    await channel.send('Please enter player ' + str(plyr)
                                       + '\'s character name')
                else:
                    await channel.send('Input is invalid!  Please try again'
                                       + ' and ensure you include a comma '
                                       + 'between the character name and '
                                       + 'Discord handle, as well as a '
                                       + 'hashtag between the Discord Handle '
                                       + 'and the ID numbers after.  Example: '
                                       + 'yourname@email.com, Handle#1234')

            elif cnt % 2 != 0:
                cname = str(message.content)
                players[plyr] = {}
                players[plyr]['player name'] = cname
                players[plyr]['role'] = 'player'
                cnt = cnt + 1
                await channel.send('Please enter ' + cname + '\'s email and '
                                   + 'Discord handle seperated by a comma. '
                                   + ' Please do not add '
                                   + 'the @ before the Discord handle. '
                                   + ' Example: name@name.com, '
                                   + 'username#1234')
            elif cnt % 2 == 0:
                lst = str(message.content)
                if ',' and '#' in lst:
                    lst = lst.split(',')
                    players[plyr]['email'] = lst[0]
                    if lst[1][0] == ' ':
                        players[plyr]['discord'] = lst[1][1:]
                    else:
                        players[plyr]['discord'] = lst[1]
                    cnt += 1
                    plyr += 1
                    if plyr <= pnum:
                        await channel.send('Please enter player ' + str(plyr)
                                           + '\'s character name')
                    else:
                        try:
                            await channel.send(holdMess)
                            new_loot_sheet(lsname, players)
                            await channel.send('Your LootSheet ' + lsname
                                               + ' is being created!  Please '
                                               + 'check your email for the link'
                                               + 'to your LootSheet!')
                            await mainChan('Your LootSheet ' + lsname
                                           + ' is being created!  Please '
                                           + 'check your email for the link'
                                           + 'to your LootSheet!')
                        except:
                            await channel.send(ErrorExcept)
                        chatChan = True
                        return
                else:
                    await channel.send('Input is invalid!  Please try again'
                                       + ' and ensure you include a comma '
                                       + 'between the character name and '
                                       + 'Discord handle, as well as a '
                                       + 'hashtag between the Discord Handle '
                                       + 'and the ID numbers after.  Example: '
                                       + 'yourname@email.com, Handle#1234')

        await bot.process_commands(message)


@bot.command(name='players')
async def call_ls_players(ctx):
    await ctx.send(players)


@bot.command(name='testconnection')
async def test_connection(ctx):
    answers = ['donkey', 'doucheface', 'dildo monster', 'R. Kelly wannabe',
               'twat monster', 'literal disappointment', 'wanker',
               'silliest of gooses']
    response = 'I am connected ya ' + random.choice(answers)
    await ctx.send(response)


bot.run(TOKEN)
