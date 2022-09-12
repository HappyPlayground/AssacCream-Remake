import struct

import discord
from discord.ext import commands

from tools.config import config

intents=discord.Intents.all()

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

        self.color = int(bytes.hex(struct.pack("BBB", *tuple(config["color"]))), 16)

    async def on_message_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("관리자가 아니시네요!")
            
        elif isinstance(error, commands.CommandNotFound):
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
        
        return await self.invoke(ctx)