import discord
from discord.ext import commands
from discord_slash import cog_ext

guild_ids = [918591198799749240]

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all())

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ping", description="Shows bot latency", guild_ids=guild_ids)
    async def _ping(self, ctx):
        await ctx.send(f"🌍 Ping is `{round(bot.latency)}ms`")

def setup(bot):
    bot.add_cog(ping(bot))