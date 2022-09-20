import interactions

GUILD_IDS = [918591198799749240]

class Images(interactions.Extension):
    def __init__(self, bot: interactions.Client) -> None:
        self.bot = bot

    @interactions.extension_command(name="images", description="Link for the google drive with all the images")
    async def image(self, ctx: interactions.CommandContext) -> None:
        embed = interactions.Embed(
            title="📸 Robotics Media Folder",
            description="All of the pictures and videos we've taken have been uploaded to the [Google Drive folder](https://drive.google.com/drive/folders/1Huch-lIgYjOjULL7cKV6anj-u5IHbLX1?usp=sharing) "
        )
        await ctx.send(embeds=embed)

def setup(bot: interactions.Client) -> None:
    Images(bot)
