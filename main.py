import discord
import asyncio
import time

CHANNEL_ID = 961894870216237107

client = discord.Client()

async def greet():
    channel = client.get_channel(CHANNEL_ID)
    
    while True:
        await channel.send('!世界王檢查')
        time.sleep(60)
    
@client.event
async def on_ready():
    await greet()
    print('目前登入身份：', client.user)

@client.event
async def on_message(message):

    if message.author == client.user:
        return

import os

client.run(os.environ["DISCORD_TOKEN"])
