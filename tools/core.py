import asyncio
from discord.ext import commands
from logging import getLogger
from tools.db import D_users, D_guilds
from typing import Any, Union
from discord.ext import tasks

log = getLogger(__name__)

data_options = {"user": "u_", "guild": "g_", "all": ""}

database_options = {
    "u_": D_users,
    "g_": D_guilds,
}


class AssacCore:
    def __init__(self, client: commands.Bot):
        """
        client : 디스코드 봇
        """
        self.version = "0.0.1"
        self.client = client
        self.data = {}

    async def Get_Data(self, content_id: Union[int, Any], type: str):
        try:
            content_id = str(
                content_id if isinstance(content_id, int) else content_id.id
            )
            type = data_options[type]
        except:
            return None

        user = (
            self.data[type + content_id]
            if type + content_id in self.data
            else (await database_options[type].find_one({"_id": int(content_id)}))
        )

        if user is None:
            return None

        self.data[type + content_id] = user

        return user

    @tasks.loop(minutes=10)
    async def AutomaticApplyData(self):

        await self.client.wait_until_ready()

        while not self.client.is_closed():
            await self.Apply_Data("all")

    async def Apply_Data(self, options: str = "all") -> bool:
        if options not in [*data_options.keys()]:
            result = False

        elif not self.data:
            result = False

        else:
            options = data_options[options]
            for i in dict(
                filter(lambda e: e[:2].startswith(options), self.data.keys())
            ):
                db = (
                    database_options[options]
                    if options != ""
                    else database_options[i[:2]]
                )
                await db.update_one({"_id": int(i[2:])}, {"$set": self.data[i]})

            result = True

        self.Clear_Data(options)

        log.info("데이터를 적용 하였습니다.")

        return result

    async def Update_Data(
        self, type: str, content_id: Union[int, Any], data: dict, isDelete: bool = False
    ):
        try:
            content_id = content_id if isinstance(content_id, int) else content_id.id
            type = data_options[type]
        except:
            return None

        if type == "all":
            return None

        content_data = await self.Get_Data(content_id, type)

        if not content_data:
            for i in data.keys():
                content_data.pop(i, None)

        if "_id" not in data.keys():
            data["_id"] = content_id

        if isDelete:
            data = content_data
        else:
            data = dict(content_data, **data)

        self.data[type + str(content_id)] = data

        log.info("데이터를 업데이트 하였습니다.")

        return data

    def Clear_Data(self, options: str = "all"):
        if self.data:
            if options == "all":
                self.data = {}
            else:
                options = data_options[options]
                self.data = dict(
                    filter(lambda e: not e[:2].startswith(options), self.data.keys())
                )

        log.info("데이터를 초기화 하였습니다.")

        return
