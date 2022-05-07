import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option

guild_ids = [918591198799749240]

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all())

class annoy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="annoy", description="Annoy someone", guild_ids = guild_ids, options=[
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
    async def annoy(self, ctx, user, amount):
        if amount > 10:
            await ctx.send("That's just too far")
            return
        else:
            for i in range(int(amount)):
                await ctx.send(f"{user.mention}")

def setup(bot):
    bot.add_cog(annoy(bot))