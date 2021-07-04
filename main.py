import discord
import os

start = 0
client = discord.Client()

@client.event
async def on_ready():
  print('online: {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return
    

  if message.content.startswith('!bad apple'):
    import time
    await message.channel.send('loaded!', delete_after = 0.05)
    
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094441637740564/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094449404674058/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094456485969981/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094463267373116/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094471802650654/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094482653053008/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094488044044338/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094491169062932/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094498323890196/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094508151668756/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094514681413642/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094519731617802/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094523958951946/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094530992537632/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094541919879168/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094547631603743/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094554607648828/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094560709836820/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094570302341170/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094577236049980/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094585150832640/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('https://media.discordapp.net/attachments/858094390663839754/858094594280128512/image0.gif', delete_after = 0.05)
    time.sleep(9.9)
    await message.channel.send('Finished, Coded by ZTE2976.', delete_after = 5)
    time.sleep(5)

  import random
  rick_roll = ['https://tenor.com/view/together-foreverd-sike-bitch-you-just-got-together-foreverd-gif-21449028', 'https://media0.giphy.com/media/Ju7l5y9osyymQ/giphy.gif']
  if message.content.startswith('!rickroll'):
    await message.channel.send(random.choice(rick_roll), delete_after = 4.1)


client.run(os.getenv('TOKEN'))
