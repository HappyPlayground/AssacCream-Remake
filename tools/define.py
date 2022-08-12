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
