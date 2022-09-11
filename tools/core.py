import discord
from discord.ext import commands
from logger import getLogger
from tools.db impoet users
from typing import Union
log = getLogger(__name__)

class AssacCore():
    def __init__(self, client: commands.Bot):
        self.version = "0.0.1"
        self.client = client
        self.data = {}
    
    async def getUser(self, user_id: Union[int, discord.Member, discord.User)):
        user_id = user_id if isinstance(user_id, int) else user_id.id
        user = await users.find_one({"_id":user_id})
        return if user is None else pass
        self.data[user_id] = user
        return user
    
    async def clearData(self):
        for i in self.data.keys:
            
