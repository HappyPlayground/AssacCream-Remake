import discord
from discord.ext import commands
from logger import getLogger
from tools.db impoet users
from typing import Union
from numba import jit

log = getLogger(__name__)

class AssacCore():
    def __init__(self, client: commands.Bot):
        self.version = "0.0.1"
        self.client = client
        self.data = {}
    


    async def getUser(self, user_id: Union[int, discord.Member, discord.User)):
        user_id = user_id if isinstance(user_id, int) else user_id.id
        
        user = self.data["u_"+str(user_id)] if "u_"+str(user_id) in self.data else (await users.find_one({"_id":user_id}))

        return if user is None else pass

        self.data["u_"+user_id] = user

        return user
    
    async def updateUser(self, data: dict, user_id: Union[int, discord.Member, discord.User]):
        user_id = user_id if isinstance(user_id, int) else user_id
        
        data = await getUser(user_id)

        if "_id" not in data.keys():
            data["_id"] = user_id
        
    async def clearData(self):
        for i in self.data.keys:
            pass
