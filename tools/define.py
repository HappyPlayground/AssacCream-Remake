from typing import Union
import discord
from discord.ext import commands
from tools.db import D_users as users
import re

URL_REGEX = re.compile(
    r"(?:https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
)  # URL regular expression


async def check_User(user: Union[discord.Member, discord.User]):
    data = await users.find_one({"_id": user.id})
    if data is None:
        return False
    else:
        return True


def chunks(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def ad_help_formater(
    example: list = ["{prefix}{command}"],
    argments: list = [],
):

    return {"example": example, "argments": argments}  # return example


# def help_formatter(ctx: commands.Context, command: str):
#    command = ctx.bot.get_command(command)
#
#    extras = command.extras
#
#    for i in extras['example']:
#        i = i.replace(
#            "{prefix}", ctx.prefix
#        ).replace(
#            "{command}", command.name
#        )
#        try:
#            i = i.format(*extras['argments'])
#        except:
#            pass
#        finally:
#
#    return tmp


def authorName(ctx: commands.Context):
    return ctx.author.nick or ctx.author.name
