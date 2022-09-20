import interactions

GUILD_IDS = [918591198799749240]

class Ping(interactions.Extension):
    def __init__(self, bot: interactions.Client) -> None:
        self.bot = bot

    @interactions.extension_command(name="ping", description="Shows bot latency")
    async def ping(self, ctx: interactions.CommandContext) -> None:
        await ctx.send("Hello! I'm Sharpie!")

def setup(bot: interactions.Client) -> None:
    Ping(bot)
