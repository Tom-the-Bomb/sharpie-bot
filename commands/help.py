import discord
from discord.ext import commands
from discord_slash import cog_ext

guild_ids = [918591198799749240]

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all())

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="help", description="Lists available commands", guild_ids=guild_ids)
    async def _help(self, ctx):
        embed = discord.Embed(title="Help")
        embed.add_field(name="Annoy Someone", value="`/annoy` \n Pings a given user a specified number of times. Only works for <@&918640986618486794>'s <@&918638863516328056>'s & <@&962812802840539136>'s", inline=False)
        embed.add_field(name="Ping", value="`/ping` \n Shows <@963255439963869244>'s latency", inline=False)
        embed.add_field(name="Playlist Link", value="`/playlist` \n Sends the link to the robotics Spotify playlist", inline=False)
        embed.add_field(name="Schedule", value="`/schedule` \n Sends an embed with the schedule for the robotics meetings", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))