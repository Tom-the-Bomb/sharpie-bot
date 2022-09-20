import interactions

guild_ids = [918591198799749240]

class roles(interactions.Extension):
    def __init__(self, bot):
        self.bot: interactions.Client = bot

    @interactions.extension_command(name="roles", description="Sends role selector")
    async def _roles(self, ctx):
        manufacturingBtn = interactions.Button(
        style=interactions.ButtonStyle.SECONDARY,
        label="Manufacturing Team",
        emoji=interactions.Emoji(name="🛠️"),
        custom_id="manufacturing",
        scope=guild_ids
        )
        designBtn = interactions.Button(
        style=interactions.ButtonStyle.SECONDARY,
        label="Design Team",
        emoji=interactions.Emoji(name="✏️"),
        custom_id="design",
        scope=guild_ids
        )
        programmingBtn = interactions.Button(
        style=interactions.ButtonStyle.SECONDARY,
        label="Programming Team",
        emoji=interactions.Emoji(name="🖥️"),
        custom_id="programming",
        scope=guild_ids
        )
        businessBtn = interactions.Button(
        style=interactions.ButtonStyle.SECONDARY,
        label="Business Team",
        emoji=interactions.Emoji(name="💰"),
        custom_id="business",
        scope=guild_ids
        )
        mediaBtn = interactions.Button(
        style=interactions.ButtonStyle.SECONDARY,
        label="Media Team",
        emoji=interactions.Emoji(name="📸"),
        custom_id="media",
        scope=guild_ids
        )
        heHim = interactions.Button(
        style=interactions.ButtonStyle.SECONDARY,
        label="He/Him",
        custom_id="heHim",
        scope=guild_ids
        )
        sheHer = interactions.Button(
        style=interactions.ButtonStyle.SECONDARY,
        label="She/Her",
        custom_id="sheHer",
        scope=guild_ids
        )
        theyThem = interactions.Button(
        style=interactions.ButtonStyle.SECONDARY,
        label="They/Them",
        custom_id="theyThem",
        scope=guild_ids
        )
        any = interactions.Button(
        style=interactions.ButtonStyle.SECONDARY,
        label="Any",
        custom_id="any",
        scope=guild_ids
        )
        teamRow = interactions.spread_to_rows(manufacturingBtn, designBtn, programmingBtn, businessBtn, mediaBtn)
        pronounRow = interactions.spread_to_rows(heHim, sheHer, theyThem, any)
        embedOne = interactions.Embed(description=f"👋 Hi! Welcome to the NSS Robotics Discord server! Please use the buttons below to grab various roles for both your positon/positions on the team as well as your preferred pronouns. You can pick as many as you'd like for both!\n\nThe buttons are toggles so clicking them once will give you the role and clicking them again will take the role away", color=0x5ccbff)
        embedTwo = interactions.Embed(description=f"🙋 **Sub-Team Roles**", color=0x5ccbff)
        embedThree = interactions.Embed(description=f"🗣️ **Pronoun Roles**", color=0x5ccbff)
        await ctx.get_channel()
        await ctx.channel.send(embeds=embedOne)
        await ctx.channel.send(embeds=embedTwo, components=teamRow)
        await ctx.channel.send(embeds=embedThree, components=pronounRow)

    @interactions.extension_component("manufacturing")
    async def manufacturing_button(self, ctx):
        await ctx.get_guild()
        role = int(918634757028458507)
        if role in ctx.author.roles:
            roleRemoved = interactions.Embed(description=f"❌ You've been removed from the Manufacturing Team!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
            await ctx.send(embeds=roleRemoved, ephemeral=True)
        else:
            roleAdded = interactions.Embed(description=f"✅ You've been added to the Manufacturing Team!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
            await ctx.send(embeds=roleAdded, ephemeral=True)

    @interactions.extension_component("design")
    async def design_button(self, ctx):
        await ctx.get_guild()
        role = int(918634709507014666)
        if role in ctx.author.roles:
            roleRemoved = interactions.Embed(description=f"❌ You've been removed from the Design Team!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
            await ctx.send(embeds=roleRemoved, ephemeral=True)
        else:
            roleAdded = interactions.Embed(description=f"✅ You've been added to the Design Team!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
            await ctx.send(embeds=roleAdded, ephemeral=True)

    @interactions.extension_component("programming")
    async def programming_button(self, ctx):
        await ctx.get_guild()
        role = int(918634815140556842)
        if role in ctx.author.roles:
            roleRemoved = interactions.Embed(description=f"❌ You've been removed from the Programming Team!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
            await ctx.send(embeds=roleRemoved, ephemeral=True)
        else:
            roleAdded = interactions.Embed(description=f"✅ You've been added to the Programming Team!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
            await ctx.send(embeds=roleAdded, ephemeral=True)

    @interactions.extension_component("business")
    async def business_button(self, ctx):
        await ctx.get_guild()
        role = int(918634627055353906)
        if role in ctx.author.roles:
            roleRemoved = interactions.Embed(description=f"❌ You've been removed from the Business Team!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
            await ctx.send(embeds=roleRemoved, ephemeral=True)
        else:
            roleAdded = interactions.Embed(description=f"✅ You've been added to the Business Team!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
            await ctx.send(embeds=roleAdded, ephemeral=True)

    @interactions.extension_component("media")
    async def media_button(self, ctx):
        await ctx.get_guild()
        role = int(982774976287506442)
        if role in ctx.author.roles:
            roleRemoved = interactions.Embed(description=f"❌ You've been removed from the Media Team!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
            await ctx.send(embeds=roleRemoved, ephemeral=True)
        else:
            roleAdded = interactions.Embed(description=f"✅ You've been added to the Media Team!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
            await ctx.send(embeds=roleAdded, ephemeral=True)

    @interactions.extension_component("heHim")
    async def heHim_button(self, ctx):
        await ctx.get_guild()
        role = int(1021591068774502511)
        if role in ctx.author.roles:
            roleRemoved = interactions.Embed(description=f"❌ Removed He/Him pronouns!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
            await ctx.send(embeds=roleRemoved, ephemeral=True)
        else:
            roleAdded = interactions.Embed(description=f"✅ Added He/Him pronouns!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
            await ctx.send(embeds=roleAdded, ephemeral=True)

    @interactions.extension_component("sheHer")
    async def sheHer_button(self, ctx):
        await ctx.get_guild()
        role = int(1021591222789357590)
        if role in ctx.author.roles:
            roleRemoved = interactions.Embed(description=f"❌ Removed She/Her pronouns!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
            await ctx.send(embeds=roleRemoved, ephemeral=True)
        else:
            roleAdded = interactions.Embed(description=f"✅ Added She/Her pronouns!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
            await ctx.send(embeds=roleAdded, ephemeral=True)

    @interactions.extension_component("theyThem")
    async def theyThem_button(self, ctx):
        await ctx.get_guild()
        role = int(1021591254020149268)
        if role in ctx.author.roles:
            roleRemoved = interactions.Embed(description=f"❌ Removed They/Them pronouns!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
            await ctx.send(embeds=roleRemoved, ephemeral=True)
        else:
            roleAdded = interactions.Embed(description=f"✅ Added They/Them pronouns!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
            await ctx.send(embeds=roleAdded, ephemeral=True)

    @interactions.extension_component("any")
    async def any_button(self, ctx):
        await ctx.get_guild()
        role = int(1021591277009109032)
        if role in ctx.author.roles:
            roleRemoved = interactions.Embed(description=f"❌ Removed Any pronouns!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
            await ctx.send(embeds=roleRemoved, ephemeral=True)
        else:
            roleAdded = interactions.Embed(description=f"✅ Added Any pronouns!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
            await ctx.send(embeds=roleAdded, ephemeral=True)


def setup(bot):
    roles(bot)