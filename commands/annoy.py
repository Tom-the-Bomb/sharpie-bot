import interactions
guild_ids = [918591198799749240]

class annoy(interactions.Extension):
    def __init__(self, bot):
        self.bot: interactions.Client = bot

    @interactions.extension_command(name="annoy", description="Annoy someone", options=[
        interactions.Option (
            name="user",
            description="The user to annoy",
            type=interactions.OptionType.USER,
            required=True
        ),
        interactions.Option (
            name="amount",
            description="The amount of times to annoy the user",
            type=interactions.OptionType.INTEGER,
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
    annoy(bot)