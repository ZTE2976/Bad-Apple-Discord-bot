import discord
import os
import asyncio

start = 0
client = discord.Client()

@client.event
async def on_ready():
  print('online: {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return
    
  if message.content.startswith('!help'):
    embedVar = discord.Embed(title="Bad Apple bot help", description="Commands for the bot!", color=7241408)
    embedVar.add_field(name="!bad apple", value=" - Plays the Bad Apple animation.", inline=False)
    embedVar.add_field(name="!rickroll", value=" - Get rickrolled.", inline=False)
    embedVar.add_field(name="!help", value=" - Commands list.", inline=False)
    embedVar.add_field(name="!ping", value=" - Bots latency", inline=False)
    await message.channel.send(embed=embedVar)
    
  if message.content.startswith('!bad apple'):
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094441637740564/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094449404674058/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094456485969981/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094463267373116/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094471802650654/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094482653053008/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094488044044338/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094491169062932/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094498323890196/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094508151668756/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094514681413642/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094519731617802/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094523958951946/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094530992537632/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094541919879168/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094547631603743/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094554607648828/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094560709836820/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094570302341170/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094577236049980/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094585150832640/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094594280128512/image0.gif', delete_after = 9.9)
    await asyncio.sleep(9.9)
    await message.channel.send('Finished.', delete_after = 5)
    
  if message.content.startswith('!rickroll'):
    await message.channel.send(('https://imgur.com/HdvWcB5'), delete_after = 211.5)
    
  if message.content.startswith('!ping'):
    await message.channel.send(f'Pong!  {client.latency} ms')

client.run(os.getenv('TOKEN'))
