import os
import discord

from dotenv import load_dotenv

from functions import functions


load_dotenv('./settings.env')
TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()

prefix = '%'


@client.event
async def on_ready():
    print(f'{client.user} has connected to discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content[0] == '%':
        # the line below removes the prefix
        args = message.content.trim().replace(prefix, '', 1).split(' ')
        # the line below separates the command and removes it from the args
        command = args.pop(0)

        try:
            await functions[command](message, args)
        except KeyError as err:
            print(f'Invalid command was given. {err}')


client.run(TOKEN)
