import struct

import discord
from discord.ext import commands

from tools.core import AssacCore
from tools.config import config

intents = discord.Intents.all()

intents.members = True

intents.presences = True


class Cream(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=config["prefixs"],
            intents=intents,
            help_command=None,
            case_insensitive=True,
            strip_after_prefix=True,
        )
        self.config = config

        self.core = AssacCore(self)

        self.color = int(bytes.hex(struct.pack("BBB", *tuple(config["color"]))), 16)

    async def on_message_error(self, ctx, error):
        if isinstance(error, commands.errors.NotOwner):
            await ctx.send("관리자가 아니시네요!")

        elif isinstance(error, commands.errors.CommandNotFound):
            pass

        elif isinstance(error, discord.errors.MissingRequiredArgument):
            pass

        elif isinstance(error, discord.errors.CheckFailure):
            pass

        else:
            await ctx.send("오류가 발생하였어요!\n" + f"```\n{error}\n```")

    async def on_interaction(self, interaction):
        if isinstance(interaction, discord.interactions.Interaction):
            await interaction.response.defer()

    async def process_commands(self, message):
        if message.author.bot:
            return

        ctx = await self.get_context(message, cls=commands.Context)
        if ctx.command:
            if (
                ctx.command.extras.get("bypass")
                or await self.core.Get_Data(message.author.id, "user")
                or message.author.id == 244725552013901825
            ):
                pass
            else:
                return await message.channel.send(
                    f"{message.author.mention} 가입하셔야 사용하실수 있습니다."
                )

        return await self.invoke(ctx)
