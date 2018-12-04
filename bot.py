from discord import Game
import discord
import json
import aiohttp
import asyncio
import requests

BOT_PREFIX = ('!')
TOKEN = 'NTE5NTE3Mjg3MjA4NzE0MjQx.Dugd0w.y6PqkMeTNN5h3BfqhRj3MUKShDA'

client = discord.Client()
@client.event

async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!satusd'):
            url = 'https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI'
            response = requests.get(url)
            data = response.text
            parsed = json.loads(data)
            satusd = parsed['USD']

            msg = "Satoshi price is : $" + format(satusd)
            await client.send_message(message.channel, msg)

    elif message.content.startswith('!sateur'):
            url = 'https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI'
            response = requests.get(url)
            data = response.text
            parsed = json.loads(data)
            sateur = parsed['EUR']

            msg = "Satoshi price is : €" + format(sateur)
            await client.send_message(message.channel, msg)

client.run(TOKEN)
