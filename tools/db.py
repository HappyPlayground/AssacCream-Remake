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

