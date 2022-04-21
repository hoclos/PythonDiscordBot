import discord
import asyncio
import time

CHANNEL_ID = 961894870216237107

client = discord.Client()

async def greet():
    channel = client.get_channel(CHANNEL_ID)
    loopLimit = 0

    while loopLimit < 9:
        await channel.send('!世界王檢查')
        loopLimit += 1
        time.sleep(60)

    client.logout()

@client.event
async def on_ready():
    print('目前登入身份：', client.user)
    await greet()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

import os

client.run(os.environ["DISCORD_TOKEN"])
