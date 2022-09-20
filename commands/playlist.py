import interactions

guild_ids = [918591198799749240]

class playlist(interactions.Extension):
    def __init__(self, bot):
        self.bot: interactions.Client = bot

    @interactions.extension_command(name="playlist", description="Sends a link to the robotics playlist on Spotify")
    async def _playlist(self, ctx):
        await ctx.send("**Quick Disclaimer:** This playlist is a compilation of everyone's different music tastes which means it'll mess with your head in ways you couldn't imagine so listening to it is done at your own risk.\n\nhttps://open.spotify.com/playlist/3S9LxhvckvM5CNMF7nhxmc?si=d37db241881d468d")

def setup(bot):
    playlist(bot)