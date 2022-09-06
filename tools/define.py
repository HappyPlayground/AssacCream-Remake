from typing import Union
import discord
from tools.db import D_users as users
import re

async def check_User(user: Union[discord.Member, discord.User]):
    data = await users.find_one({"_id": user.id})
    if data is None:
        return False
    else:
        return True

def chunks(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def ad_help_formater(argments=None, example=None): # advenced help formatter
 
    example = example or "{prefix}{command} {argments}" # no example -> default example
    argments = argments or "" # special argments or nothing

    return {"ad_help": {"example": example, "argments": argments}} # return ad_help format

def authorName(ctx: discord.Context):
    return ctx.author.nick or ctx.author.name

async def help_formater(ctx, command):
    extras: dict = command.extras # get extra(dict) from Command Object

    temp = ["{prefix}", "{command}", "{argments}"]  # replace things define

    tmp = [
        ctx.prefix, # Prefix(User Used) insert
        command.name, # Command name Insert
        " ".join( # " " join some list
            [
                f"({await load_text(ctx.author ,i)})" # load text arg
                for i in extras["ad_help"]["argments"] # arg into argments
            ]
        ),
    ]

    tp = extras["ad_help"]["example"] # get example text from extras

    for i in range(0, 3):
        tp = tp.replace(temp[i], tmp[i]) # example replace 

    return tp # return advenced format