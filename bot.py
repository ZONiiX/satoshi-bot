import discord, json, requests, chalk
from discord.ext import commands

bot = commands.Bot(command_prefix="!", status=discord.Status.idle, activity=discord.game(name="Eating Fiat..."))

bot.remove_command("help")

@bot.event
async def on_ready():
    print(chalk.green("Ready!"))
    print(chalk.blue(f"Serving: {len(bot.guilds)} guilds.")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(nae="Fiat destroyed!"))


@bot.command()
async def satusd():
    url = 'https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI'
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    satusd = parsed['USD']

    msg = "Satoshi price is : $" + format(satusd)
    await client.send_message(message.channel, msg)

@bot.command()
async def sateur():
    url = 'https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI'
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    sateur = parsed['EUR']

    msg = "Satoshi price is : €" + format(sateur)
    await client.send_message(message.channel, msg)



"""from discord import Game
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

client.run(TOKEN)"""
