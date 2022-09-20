import interactions

guild_ids = [918591198799749240]
class images(interactions.Extension):
    def __init__(self, bot):
        self.bot: interactions.Client = bot

    @interactions.extension_command(name="images", description="Link for the google drive with all the images", options=[])
    async def image(self, ctx):
        embed = interactions.Embed(title="📸 Robotics Media Folder", description="All of the pictures and videos we've taken have been uploaded to the [Google Drive folder](https://drive.google.com/drive/folders/1Huch-lIgYjOjULL7cKV6anj-u5IHbLX1?usp=sharing) ")
        await ctx.send(embeds=embed)

def setup(bot):
    images(bot)