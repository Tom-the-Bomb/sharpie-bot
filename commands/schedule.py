import interactions

guild_ids = [918591198799749240]

class schedule(interactions.Extension):
    def __init__(self, bot):
        self.bot: interactions.Client = bot

    @interactions.extension_command(name="schedule", description="Sends robotics schedule", options=[])
    async def _schedule(self, ctx):
        embed = interactions.Embed(title="Robotics Club Schedule")
        embed.add_field(name='Monday', value='No Robotics', inline=False)
        embed.add_field(name='Tuesday', value='3:00 - When everyone leaves', inline=False)
        embed.add_field(name='Wednesday', value='3:00 - When everyone leaves', inline=False)
        embed.add_field(name='Thursday', value='3:00 - When everyone leaves', inline=False)
        embed.add_field(name='Friday', value='3:00 - When everyone leaves earlier', inline=False)
        await ctx.send(embeds=embed)


def setup(bot):
    schedule(bot)