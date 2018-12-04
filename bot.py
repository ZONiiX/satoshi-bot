import random
import asyncio
import aiohttp
import json
import requests
from discord import Game
from discord.ext.commands import Bot


BOT_PREFIX = ("!")
TOKEN = "NTE5NTE3Mjg3MjA4NzE0MjQx.Dugd0w.y6PqkMeTNN5h3BfqhRj3MUKShDA"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)


@client.command()
async def satusd():
    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    usd_rate = parsed["USD"]

    await client.say("1 Satoshi is: $" + usd_rate)

@client.command()
async def sateur():
    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    eur_rate = parsed["EUR"]
    await client.say("1 Satoshi is: $" +eur_rate)


@client.command()
async def calcsatusd(number):
    finalNumber = int(number)
    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    usd_rate = parsed["USD"]
    final_price = usd_rate*finalNumber
    await client.say("{0.author.mention}" + final_price)

@client.event
async def on_read():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
