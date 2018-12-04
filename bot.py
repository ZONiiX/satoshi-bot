from discord import Game
from discord.ext.commands import Bot
import json
import aiohttp


BOT_PREFIX = ('!')
TOKEN = 'NTE5NTE3Mjg3MjA4NzE0MjQx.Dugd0w.y6PqkMeTNN5h3BfqhRj3MUKShDA'

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def satusd():
    url = 'https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI'
    async with aiohttps.ClientSession()as session:
        raw_response = awate session.get(url)
        response = await raw_response.text()
        repsonse = json.loads(response)

        await client.sat("Satoshi price is : $" + response['USD'])



client.run(TOKEN)
