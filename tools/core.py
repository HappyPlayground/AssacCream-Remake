import asyncio
import discord
from discord.ext import commands
from logger import getLogger
from tools.db import D_users, D_guilds
from typing import Any, Union
from numba import jit

log = getLogger(__name__)

data_options = {
    "user": "u_",
    "guild": "g_",
    "all": ""
}

database_options = {
    "u_": D_users,
    "g_": D_guilds,
}
class AssacCore():
    def __init__(self, client: commands.Bot):
        '''
        client : 디스코드 봇
        '''
        self.version = "0.0.1"
        self.client = client
        self.data = {}
        
        client.loop.create_task(self.AutomaticApplyData())


    async def Get_Data(self, content_id: Union[int, Any], type: str):
        try:
            content_id = content_id if isinstance(content_id, int) else content_id.id
            type = data_options[type]
        except:
            return None

        user = self.data[type+str(content_id)] if type+str(content_id) in self.data else (await database_options[type].find_one({"_id":content_id}))

        if user is None:
            return None

        self.data[type+content_id] = user

        return user

    async def AutomaticApplyData(self):
        
        await self.client.wait_until_ready()
        
        await asyncio.sleep(300)
        
        while not self.client.is_closed():
            
            await self.Apply_Data("all")
            
            await asyncio.sleep(300)
        
    
    async def Apply_Data(self, options: str = "all"):
        if options not in [*data_options.keys()]:
            result = False
        elif not self.data:
            result = False
        else:
            options = data_options[options]
            for i in dict(filter(lambda e:e[:2].startswith(options), self.data.keys())):
                db = database_options[options] if options != "" else database_options[i[:2]]
                await db.update_one(
                    {"_id":int(i[2:])},
                    {"$set":self.data[i]}
                )
            result = True
        
        log.info("데이터를 적용 하였습니다.")
                    
        return result

    async def updateData(self, data: dict, user_id: Union[int, discord.Member, discord.User]):
        user_id = user_id if isinstance(user_id, int) else user_id.id
        
        user_data = await self.getUser(user_id)

        if "_id" not in data.keys():
            data["_id"] = user_id
        
        data = dict(user_data, **data)
        
        self.data["u_"+user_id] = data
        
        log.info("데이터를 업데이트 하였습니다.")
        
        return data
        
    def clearData(self):
        if not self.data:
            self.data = {}
        
        log.info("데이터를 초기화 하였습니다.")
        
        return 
