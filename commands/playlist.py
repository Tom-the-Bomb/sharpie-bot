import discord
from discord.ext import commands
from discord_slash import cog_ext

guild_ids = [918591198799749240]

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all())

class playlist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="playlist", description="Sends a link to the robotics playlist on Spotify", guild_ids=guild_ids)
    async def _playlist(self, ctx):
        await ctx.send("**Quick Disclaimer:** This playlist is a compilation of everyone's different music tastes which means it'll mess with your head in ways you couldn't imagine so listening to it is done at your own risk.\n\nhttps://open.spotify.com/playlist/3S9LxhvckvM5CNMF7nhxmc?si=d37db241881d468d")

def setup(bot):
    bot.add_cog(playlist(bot))