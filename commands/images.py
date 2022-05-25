import discord
from discord.ext import commands
from discord_slash import cog_ext

guild_ids = [918591198799749240]

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all())

class images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="images", description="Link for the google drive with all the images", guild_ids = guild_ids, options=[])
    async def image(self, ctx):
        embed = discord.Embed(title="📸 Robotics Media Folder", description="All of the pictures and videos we've taken have been uploaded to the [Google Drive folder](https://drive.google.com/drive/folders/1Huch-lIgYjOjULL7cKV6anj-u5IHbLX1?usp=sharing) ")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(images(bot))