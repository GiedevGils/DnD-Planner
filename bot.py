import discord, configparser, datetime
from datetime import date

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config.get('Secrets', 'token')

prefix = config.get('Settings', 'prefix')

client = discord.Client()

emoji_green_check = '✅'
emoji_orange_diamond = '🔶'
emoji_red_circle = '🔴'

@client.event
async def on_ready():
    print('Logged in as: ')
    print(client.user.name)
    print(client.user.id)
    print('Using ' + prefix + ' as prefix for commands')
    print('---------')


@client.event
async def on_message(message):
    if message.author.name != 'Ilthy':
        return

    if message.content.startswith(prefix + 'prepdates'):
        if message.channel.name == 'planning':
            await getDatesAndRespond(message.channel)


async def getDatesAndRespond(channel, day=2):
    d = date.today() + datetime.timedelta(1)


    for i in range(0,4):
        
        d = d + datetime.timedelta( ( (day - 1) - d.weekday()  )  % 7 )   

        await channel.send(d.strftime('%A %d-%m-%Y'))
        
        
        last_message = channel.last_message
        await last_message.add_reaction(emoji_green_check)
        await last_message.add_reaction(emoji_orange_diamond)
        await last_message.add_reaction(emoji_red_circle)

        d += datetime.timedelta(1)
    

client.run(TOKEN)