import interactions

GUILD_IDS = [918591198799749240]

class Annoy(interactions.Extension):
    def __init__(self, bot: interactions.Client) -> None:
        self.bot = bot

    @interactions.extension_command(
        name="annoy",
        description="Annoy someone",
        options=[
            interactions.Option(
                name="user",
                description="The user to annoy",
                type=interactions.OptionType.USER,
                required=True
            ),
            interactions.Option(
                name="amount",
                description="The amount of times to annoy the user",
                type=interactions.OptionType.INTEGER,
                required=True
            ),
        ]
    )
    async def annoy(
        self,
        ctx: interactions.CommandContext,
        user: interactions.User,
        amount: int,
    ) -> None:
        if amount > 10:
            await ctx.send("That's just too far")
            return
        else:
            for i in range(amount):
                await ctx.send(user.mention)

def setup(bot: interactions.Client) -> None:
    Annoy(bot)
