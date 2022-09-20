import interactions

guild_ids = [918591198799749240]

class ping(interactions.Extension):
    def __init__(self, bot):
        self.bot: interactions.Client = bot

    @interactions.extension_command(name="ping", description="Shows bot latency")
    async def _ping(self, ctx):
        await ctx.send("Hello! I'm Sharpie!")

def setup(bot):
    ping(bot)