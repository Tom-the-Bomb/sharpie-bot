import discord
import os
import asyncio
import random
from dotenv import load_dotenv
from discord.ext.commands import bot
from discord.ext import commands
from discord_slash import SlashCommand

load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True, override_type=True)

guild_ids = [918591198799749240]

async def changePres():
    await bot.wait_until_ready()
    statuses = ["Sharpies ≠ Markers", "Animal Crossing Takeover!"]
    await bot.change_presence()
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name=f"{status}"))

        await asyncio.sleep(8)
bot.loop.create_task(changePres())

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        print(f'Loaded Command: {filename[:-3]}')
        bot.load_extension(f'commands.{filename[:-3]}')

bot.run(token)
