import logging
import random

import discord
from discord.ext import tasks
from rich.logging import RichHandler
from tools.bot import Cream
from tools.core import AssacCore

logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s :\t%(message)s",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logging.getLogger("discord").setLevel(logging.INFO)

logging.getLogger("AssacCore").setLevel(logging.INFO)


@tasks.loop(seconds=30)
async def change_pr():
    status = discord.Game(
        name=f"{random.choice(bot.command_prefix)}help - {len(bot.guilds)} 서버에서 사용중이에요!"
    )
    await bot.change_presence(activity=status)


class Assac(Cream):
    def __init__(self):
        super().__init__()

    async def on_ready(self):

        self.loop.create_task(change_pr())
        self.loop.create_task(self.core.AutomaticApplyData())

        await self.load_extension("jishaku")

        if self.config["cogs"]:
            [await self.load_extension(f"cogs.{i}") for i in self.config["cogs"]]


bot = Assac()

bot.run(bot.config["token"])
