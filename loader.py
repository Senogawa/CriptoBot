from dataclasses import dataclass
from configparser import ConfigParser
from aiogram import Bot

@dataclass
class BotMetaClass:
    token:str
    admin:str
    user:str

@dataclass
class DatabaseMetaClass:
    user:str
    password:str
    host:str
    port:int
    db:str

cnf = ConfigParser()
cnf.read("conf.ini")

bot_cnf = cnf["TELEGRAM"]
db_cnf = cnf["DATABASE"]
bot_meta = BotMetaClass(bot_cnf["token"], bot_cnf["admin"], bot_cnf["user"])
db_meta = DatabaseMetaClass(db_cnf["user"], db_cnf["password"], db_cnf["host"], int(db_cnf["port"]), db_cnf["db"])

bot_mn = Bot(bot_meta.token)

del bot_cnf
del db_cnf