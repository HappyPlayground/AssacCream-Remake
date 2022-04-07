import logging
import random

import discord
from discord.ext import tasks
from rich.logging import RichHandler

from tools.bot import Juice

logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s :\t%(message)s",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logging.getLogger("discord").setLevel(logging.INFO)


@tasks.loop(seconds=30)
async def change_pr():
    status = discord.Game(
        name=f'{random.choice(bot.command_prefix)}{random.choice(bot.get_command("help").aliases)} - {len(bot.guilds)} 서버에서 사용중이에요!')
    await bot.change_presence(activity=status)


class Tomato(Juice):
    def __init__(self):
        super().__init__()

        if self.config['isdebug']:
            self.load_extension('jishaku')

        if self.config['cogs']:
            [self.load_extension(f'cogs.{i}') for i in self.config['cogs']]

    async def on_ready(self):
        self.loop.create_task(change_pr())


bot = Tomato()


@bot.command(aliases=['도움말'], extras={'': '도움말을 보여줍니다.'})
async def help(ctx, *, command: str = None):
    pass


bot.run(bot.config['token'])
