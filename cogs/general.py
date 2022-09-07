import discord
from discord.ext import commands
from tools.define import ad_help_formater, authorName

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name="도움말",
        aliases=["도움"],
        extras=ad_help_formater(["prefix"])
    )
    async def help(self, ctx, *, command: str = ""):
        if command != "":
            embed = discord.Embed(
                title="커맨드 정보",
                color=self.bot.color
            )
            cmd = self.bot.get_command(command)
            embed.add_field(
                name=command.
            )
        
        embed.set_footer(
            text=authorName(ctx),
            icon_url=ctx.author.display_avatar.url
        )
        await ctx.send(embed=embed)
    
    @commands.command(
        name="가입",
        aliases=[],
        extras=ad_help_formater()
    )
    async def register_user(self, ctx):
        embed = discord.Embed()

    

async def setup(bot):
    await bot.add_cog(General(bot))
