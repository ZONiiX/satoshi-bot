import random
import asyncio
import aiohttp
import json
import requests
import discord
from discord import Game
from discord.ext.commands import Bot
 # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix= "!")


TOKEN = "NTE5NTE3Mjg3MjA4NzE0MjQx.DunRAQ.zSB1Gq5WgPq2Gy5Cchmjrrp5HFA"

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
async def commands():
    embed = discord.Embed(title="Commands", description="", color=0x00ff00)
    embed.add_field(name = "!satusd", value="!satusd {price} {amount}, calculates value", inline = False)
    embed.add_field(name = "!sateur", value ="!sateur {price} {amount}, calculates value", inline = False)
    embed.add_field(name = "!prices", value = "!price, gives prices of BTC and SAT ", inline = False)

    await client.say(embed=embed)

@client.command()
async def price():

    url2 = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response2 = requests.get(url2)
    data2 = response2.text
    parsed2 = json.loads(data2)
    usd_parsed_btc = parsed2["bpi"]["USD"]["rate"]
    eur_parsed_btc = parsed2["bpi"]["EUR"]["rate"]

    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    eur_rate = parsed["EUR"]
    usd_rate = parsed["USD"]

    usd_price = "$ `" +usd_rate + "`\n"
    eur_price = "€ `" +eur_rate + "`\n"

    btc_usd_price = "$ `" + usd_parsed_btc+ "`\n"
    btc_eur_price = "€`" + eur_parsed_btc+ "`\n"

    data = "SAT/USD: "+ usd_price + "SAT/EUR: "+ eur_price + "BTC/USD: " + btc_usd_price + "BTC/EUR: " + btc_eur_price

    embed = discord.Embed(title="Realtime Price Data", description=data, color =0x00ff00)
    await client.say(embed=embed)

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
