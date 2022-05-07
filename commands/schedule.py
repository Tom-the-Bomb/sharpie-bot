import discord
from discord.ext import commands
from discord_slash import cog_ext

guild_ids = [918591198799749240]

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all())

class schedule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="schedule", description="Sends robotics schedule", guild_ids=guild_ids, options=[])
    async def _schedule(self, ctx):
        embed = discord.Embed(title="Robotics Club Schedule")
        embed.add_field(name='Monday', value='No Robotics', inline=False)
        embed.add_field(name='Tuesday', value='3:00 - When everyone leaves', inline=False)
        embed.add_field(name='Wednesday', value='3:00 - When everyone leaves', inline=False)
        embed.add_field(name='Thursday', value='3:00 - When everyone leaves', inline=False)
        embed.add_field(name='Friday', value='3:00 - When everyone leaves earlier', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(schedule(bot))