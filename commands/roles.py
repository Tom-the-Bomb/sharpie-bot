import interactions

GUILD_IDS = [918591198799749240]

class Roles(interactions.Extension):
    def __init__(self, bot: interactions.Client) -> None:
        self.bot = bot

    @interactions.extension_command(name="roles", description="Sends role selector")
    async def roles(self, ctx: interactions.CommandContext) -> None:
        team_row = interactions.spread_to_rows(
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                label="Manufacturing Team",
                emoji=interactions.Emoji(name="🛠️"),
                custom_id="manufacturing",
                scope=guild_ids
            ),
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                label="Electrical Team",
                emoji=interactions.Emoji(name="⚡"),
                custom_id="electrical",
                scope=guild_ids
            ),
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                label="Design Team",
                emoji=interactions.Emoji(name="✏️"),
                custom_id="design",
                scope=guild_ids
            ),
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                label="Programming Team",
                emoji=interactions.Emoji(name="🖥️"),
                custom_id="programming",
                scope=guild_ids
            ),
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                label="Business Team",
                emoji=interactions.Emoji(name="💰"),
                custom_id="business",
                scope=guild_ids
            ),
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                label="Media Team",
                emoji=interactions.Emoji(name="📸"),
                custom_id="media",
                scope=guild_ids
            ),
        )
        
        pronoun_row = interactions.spread_to_rows(
            interactions.Button(
                style=interactions.ButtonStyle.SECONDARY,
                label="He/Him",
                custom_id="he_him",
                scope=guild_ids
            ),
            interactions.Button(
                style=interactions.ButtonStyle.SECONDARY,
                label="She/Her",
                custom_id="she_her",
                scope=guild_ids
            ),
            interactions.Button(
                style=interactions.ButtonStyle.SECONDARY,
                label="They/Them",
                custom_id="they_them",
                scope=guild_ids
            ),
            interactions.Button(
                style=interactions.ButtonStyle.SECONDARY,
                label="Any",
                custom_id="any",
                scope=guild_ids
            ),
        )

        embed1 = interactions.Embed(
            description="👋 Hi! Welcome to the NSS Robotics Discord server! "
            "Please use the buttons below to grab various roles for both your positon/positions on the team "
            "as well as your preferred pronouns. You can pick as many as you'd like for both!\n\nThe buttons are toggles "
            "so clicking them once will give you the role and clicking them again will take the role away", 
            color=0x5ccbff
        )
        embed2 = interactions.Embed(description=f"🙋 **Sub-Team Roles**", color=0x5ccbff)
        embed3 = interactions.Embed(description=f"🗣️ **Pronoun Roles**", color=0x5ccbff)

        await ctx.get_channel()
        await ctx.channel.send(embeds=embed1)
        await ctx.channel.send(embeds=embed2, components=team_row)
        await ctx.channel.send(embeds=embed3, components=pronoun_row)

    @interactions.extension_component("manufacturing")
    async def manufacturing_button(self, ctx: interactions.CommandContext) -> None:
        await ctx.get_guild()
        role = 918634757028458507

        if role in ctx.author.roles:
            embed = interactions.Embed(description=f"❌ You've been removed from the Manufacturing Team!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
        else:
            embed = interactions.Embed(description=f"✅ You've been added to the Manufacturing Team!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
        await ctx.send(embeds=embed, ephemeral=True)

    @interactions.extension_component("electrical")
    async def electrical_button(self, ctx: interactions.CommandContext) -> None:
        await ctx.get_guild()
        role = 1021608042023878716

        if role in ctx.author.roles:
            embed = interactions.Embed(description=f"❌ You've been removed from the Electrical Team!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
        else:
            embed = interactions.Embed(description=f"✅ You've been added to the Electrical Team!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
        await ctx.send(embeds=embed, ephemeral=True)

    @interactions.extension_component("design")
    async def design_button(self, ctx: interactions.CommandContext) -> None:
        await ctx.get_guild()
        role = 918634709507014666

        if role in ctx.author.roles:
            embed = interactions.Embed(description=f"❌ You've been removed from the Design Team!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
        else:
            embed = interactions.Embed(description=f"✅ You've been added to the Design Team!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
        await ctx.send(embeds=embed, ephemeral=True)

    @interactions.extension_component("programming")
    async def programming_button(self, ctx: interactions.CommandContext) -> None:
        await ctx.get_guild()
        role = 918634815140556842

        if role in ctx.author.roles:
            embed = interactions.Embed(description=f"❌ You've been removed from the Programming Team!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
        else:
            embed = interactions.Embed(description=f"✅ You've been added to the Programming Team!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
        await ctx.send(embeds=embed, ephemeral=True)

    @interactions.extension_component("business")
    async def business_button(self, ctx: interactions.CommandContext) -> None:
        await ctx.get_guild()
        role = 918634627055353906

        if role in ctx.author.roles:
            embed = interactions.Embed(description=f"❌ You've been removed from the Business Team!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
        else:
            embed = interactions.Embed(description=f"✅ You've been added to the Business Team!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
        await ctx.send(embeds=embed, ephemeral=True)

    @interactions.extension_component("media")
    async def media_button(self, ctx: interactions.CommandContext) -> None:
        await ctx.get_guild()
        role = 982774976287506442

        if role in ctx.author.roles:
            embed = interactions.Embed(description=f"❌ You've been removed from the Media Team!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
        else:
            embed = interactions.Embed(description=f"✅ You've been added to the Media Team!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
        await ctx.send(embeds=embed, ephemeral=True)

    @interactions.extension_component("he_him")
    async def he_him_button(self, ctx: interactions.CommandContext) -> None:
        await ctx.get_guild()
        role = 1021591068774502511

        if role in ctx.author.roles:
            embed = interactions.Embed(description=f"❌ Removed He/Him pronouns!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
        else:
            embed = interactions.Embed(description=f"✅ Added He/Him pronouns!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
        await ctx.send(embeds=embed, ephemeral=True)

    @interactions.extension_component("she_her")
    async def she_her_button(self, ctx: interactions.CommandContext) -> None:
        await ctx.get_guild()
        role = 1021591222789357590

        if role in ctx.author.roles:
            embed = interactions.Embed(description=f"❌ Removed She/Her pronouns!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
        else:
            embed = interactions.Embed(description=f"✅ Added She/Her pronouns!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
        await ctx.send(embeds=embed, ephemeral=True)

    @interactions.extension_component("they_them")
    async def they_them_button(self, ctx: interactions.CommandContext) -> None:
        await ctx.get_guild()
        role = 1021591254020149268

        if role in ctx.author.roles:
            embed = interactions.Embed(description=f"❌ Removed They/Them pronouns!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
        else:
            embed = interactions.Embed(description=f"✅ Added They/Them pronouns!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
        await ctx.send(embeds=embed, ephemeral=True)

    @interactions.extension_component("any")
    async def any_button(self, ctx: interactions.CommandContext) -> None:
        await ctx.get_guild()
        role = 1021591277009109032

        if role in ctx.author.roles:
            embed = interactions.Embed(description=f"❌ Removed Any pronouns!", color=0xd82d42)
            await ctx.author.remove_role(role, ctx.guild.id)
        else:
            embed = interactions.Embed(description=f"✅ Added Any pronouns!", color=0x76b154)
            await ctx.author.add_role(role, ctx.guild.id)
        await ctx.send(embeds=embed, ephemeral=True)


def setup(bot: interactions.Client) -> None:
    Roles(bot)
