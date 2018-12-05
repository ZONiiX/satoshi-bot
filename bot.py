import random
import asyncio
import aiohttp
import json
import requests
import discord
from discord import Game
from discord.ext.commands import Bot


BOT_PREFIX = ("!")
TOKEN = "NTE5NTE3Mjg3MjA4NzE0MjQx.Dul-Zg.VruNVU3_uiClMICRO4TX_fRFmDw"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

"""
@client.command()
async def satusd():
    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    usd_rate = parsed["USD"]

    await client.say("1 Satoshi is: $" + usd_rate)

oh fuck yeah spread it- Barack Obama

@client.command()
async def sateur():
    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    eur_rate = parsed["EUR"]
    await client.say("1 Satoshi is: $" +eur_rate)
"""

@client.command()
async def satusd(number, number2):
    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    usd_rate = parsed["USD"]
    int_usd_rate = float(usd_rate)


    inputed_price = int(number)
    inputed_amount = int(number2)
    price = inputed_amount*inputed_price
    final_price = format(price*int_usd_rate, '.2f')


    await client.say('$'+str(final_price))

@client.command()
async def sateur(number, number2):
    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    eur_rate = parsed["EUR"]
    int_eur_rate = float(eur_rate)

    inputed_price = int(number)
    inputed_amount = int(number2)
    price = inputed_amount*inputed_price
    final_price = format(price*int_eur_rate, '.2f')
    
    await client.say('€'+str(final_price))

@client.command()
async def help():
    embed = discord.Embed(title="Commands", description="", color=0x00ff00)
    embed.add_field(name = "!satusd", value="!satusd {price} {amount}, calculates value", inline = False)
    embed.add_field(name = "!sateur", value ="!sateur {price} {amount}, calculates value", inline = False)
    embed.add_field(name = "!prices", value = "!price, gives prices of BTC and SAT ", inline = False)

    await client.say(embed=embed)


@client.command()
async def price():
    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    embed = discord.Embed(title="Realtime Price Data", color =0x8C00FF)
    embed.add_field(name = "Bitcoin USD", value=)
    embed.add_field(name = "Bitcoin EUR", value= )
    embed.add_field(name = "Satoshi USD", value=)
    embed.add_field(name = "Satoshi EUR", value=)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with Bitcoin"))
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
