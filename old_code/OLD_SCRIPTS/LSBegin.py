# define the function for asking players via the bot
# for all their infor and returning it in a dictionary
# for LSInit.py
from discord.ext import commands
import time

bot = commands.Bot(command_prefix='-')


async def make_LS(ctx, member):
    await ctx.send('Check your DMs')
    content = 'Hello! Please wait for directions!'
    channel = await member.create_dm()
    await channel.send(content)
    time.sleep(5)
    lsname = ""
    pnum = ""
    cnt = 1
    players = {}
    await channel.send('What would you like to name your LootSheet?')
    @bot.event
    async def on_message(message):
        nonlocal lsname
        nonlocal pnum
        nonlocal cnt
        nonlocal players
        if message.author == bot.user:
            return
        if lsname == "":
            lsname = message.content
            await channel.send('Your LootSheet\'s name is ' + lsname + '.  How many players do you have?')
        elif pnum == "":
            pnum = int(message.content)
            await channel.send('What is the Character "Name|Last" "Email" "Role(player/gm)" of player 1 (no qoutes)')
        elif cnt <= pnum:
            lst = str(message.content).split()
            name = lst[0].split('|')
            players[cnt] = {}
            players[cnt]['player name'] = name[0] + ' ' + name[1]
            players[cnt]['email'] = lst[1]
            players[cnt]['role'] = lst[2]
            cnt = cnt + 1
            cnt2 = str(cnt)
            if cnt <= pnum:
                await channel.send('What is the "Character Name" "Email" "Role(player/gm)" of player ' + cnt2)
            else:
                response = 'Done!\nYour LootSheet for ' + str(pnum) + ' players \
                is created\nType -players to see your players'
                await channel.send(players)
        await bot.process_commands(message)
