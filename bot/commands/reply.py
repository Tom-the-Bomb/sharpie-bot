import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option

guild_ids = [918591198799749240]

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all())

class reply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="reply", description="Heheh", guild_ids=guild_ids, options=[
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
    async def _reply(ctx, messageid, message: str):
        channel = ctx.channel
        msg = await channel.fetch_message(messageid)
        await msg.reply(f"{message}")

def setup(bot):
    bot.add_cog(reply(bot))