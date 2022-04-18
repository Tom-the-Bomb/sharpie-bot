import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_permission
from discord_slash.model import SlashCommandPermissionType
from dotenv import load_dotenv
import os
import random
import asyncio

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

@slash.slash(name="ping", description="Shows bot latency", guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send(f"🌍 Ping is `{round(bot.latency * 1000)}ms`")

@slash.slash(name="playlist", description="Sends a link to the robotics playlist on Spotify", guild_ids=guild_ids)
async def _playlist(ctx):
    await ctx.send("**Quick Disclaimer:** This playlist is a compilation of everyone's different music tastes which means it'll mess with your head in ways you couldn't imagine so listening to it is done at your own risk.\n\nhttps://open.spotify.com/playlist/3S9LxhvckvM5CNMF7nhxmc?si=d37db241881d468d")

@slash.slash(name="annoy", description="Annoy someone", guild_ids = guild_ids, options=[
    create_option (
        name="user",
        description="The user to annoy",
        option_type=6,
        required=True
    ),
    create_option (
        name="amount",
        description="The amount of times to annoy the user",
        option_type=4,
        required=True
    )
])
@slash.permission(guild_id=918591198799749240,
                    permissions=[
                        create_permission(918591198799749240,
                                            SlashCommandPermissionType.ROLE, False),
                        create_permission(918640986618486794,
                                            SlashCommandPermissionType.ROLE, True),
                        create_permission(918638863516328056,
                                            SlashCommandPermissionType.ROLE, True),
                        create_permission(962812802840539136,
                                            SlashCommandPermissionType.ROLE, True),
                ])
async def annoy(ctx, user, amount):
    if amount > 10:
        await ctx.send("That's just too far")
        return
    else:
        for i in range(int(amount)):
            await ctx.send(f"{user.mention}")

@slash.slash(name="reply", description="Heheh", guild_ids=guild_ids, options=[
    create_option(
        name="messageid",
        description="Message ID to reply to",
        option_type=3,
        required=True
    ),
    create_option(
        name="message",
        description="Message",
        option_type=3,
        required=True
    ),
])
@slash.permission(guild_id=918591198799749240,
                    permissions=[
                        create_permission(918591198799749240,
                                            SlashCommandPermissionType.ROLE, False),
                        create_permission(918640986618486794,
                                            SlashCommandPermissionType.ROLE, True),
                        create_permission(918638863516328056,
                                            SlashCommandPermissionType.ROLE, True),
                        create_permission(962812802840539136,
                                            SlashCommandPermissionType.ROLE, True),
                    ])
async def _reply(ctx, messageid, message: str):
    channel = ctx.channel
    msg = await channel.fetch_message(messageid)
    await msg.reply(f"{message}")

bot.run(token)
