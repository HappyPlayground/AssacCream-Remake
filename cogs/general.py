import discord
from discord.ext import commands
from tools.define import ad_help_formater, authorName


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="테스트1", extras={"bypass": True})
    async def tes2t(self, ctx):
        await ctx.send("테스트")

    @commands.command(name="테스트2")
    async def test1(self, ctx):
        await ctx.send("아마안됨")

    # @commands.command(
    #    name="도움말",
    #    aliases=["도움"],
    #    extras=dict(ad_help_formater(["prefix"]), **{"bypass": "True"})
    # )
    # async def help(self, ctx, *, command: str = ""):
    #    if command != "":
    #        embed = discord.Embed(
    #            title="커맨드 정보",
    #            color=self.bot.color
    #        )
    #        command
    #
    #    embed.set_footer(
    #        text=authorName(ctx),
    #        icon_url=ctx.author.display_avatar.url
    #    )
    #    await ctx.send(embed=embed)
    #
    # @commands.command(
    #    name="가입",
    #    aliases=[],
    #    extras=dict(ad_help_formater(["register"]), **{"bypass": "True"})
    # )
    # @commands.cooldown(rate=1, per=600.0, type=commands.BucketType.user)
    # async def register_user(self, ctx):
    #    embed = discord.Embed()
    #    view =
    #    msg = await ctx.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(General(bot))
