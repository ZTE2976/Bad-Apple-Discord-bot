import os
import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True  # Enable the message intent

bot: commands.Bot = commands.Bot(command_prefix='!', intents=intents)

# Event to execute when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Define a command for displaying help
@bot.command()
async def help(ctx: commands.Context):
    embed: discord.Embed = discord.Embed(title="Bad Apple Bot Help", description="Commands for the bot!", color=0x7241408)
    embed.add_field(name="!bad apple", value="Plays the Bad Apple animation.", inline=False)
    embed.add_field(name="!rickroll", value="Get rickrolled.", inline=False)
    embed.add_field(name="!help", value="Commands list.", inline=False)
    embed.add_field(name="!ping", value="Bot's latency", inline=False)
    await ctx.send(embed=embed)

# Define the ping command
@bot.command()
async def ping(ctx: commands.Context):
    latency: int = round(bot.latency * 1000)
    await ctx.send(f'Pong! {latency} ms')

# Define the bad apple command
@bot.command()
async def bad_apple(ctx: commands.Context):
    # Read Imgur URLs from a file
    with open('bad_apple_urls.txt', 'r') as file:
        urls = file.read().splitlines()
    # Send URLs with a delay using asyncio
    for url in urls:
        await ctx.send(url, delete_after=9.9)
        await asyncio.sleep(9.9)
    # Send confirmation message
    await ctx.send("Completed!")

# Define the rickroll command
@bot.command()
async def rickroll(ctx: commands.Context):
    await ctx.send('https://imgur.com/HdvWcB5', delete_after=211.5)

# Run the bot with your token
bot.run(os.getenviron['TOKEN'])
