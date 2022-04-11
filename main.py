import discord
import asyncio
import time

client = discord.Client()

@client.event
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.content == '!世界王觸發':
        while True:
            await message.channel.send('!世界王檢查')
            time.sleep(60)

import os

client.run(os.environ["DISCORD_TOKEN"])
