"""
Database Load tool
example) from tools.db import YOURDB
"""
from tools.config import config

import motor.motor_asyncio as motor

dbclient = motor.AsyncIOMotorClient(
    config["database"]["address"], config["database"]["port"]
)

db = dbclient.assacdb

D_users = db.users

D_language = db.language

D_customprefix = db.ctprefix
D_blacklists = db.blacklists
D_coinposts = db.coins

D_commands = db.cmds

D_achi = db.achievements

D_u_cb = db.user_chatbot
D_guilds = db.guilds
