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

@dataclass
class Binance:
    key:str
    secret:str
    symbol:str

cnf = ConfigParser()
cnf.read("conf.ini")

bot_cnf = cnf["TELEGRAM"]
db_cnf = cnf["DATABASE"]
binance_cnf = cnf["BINANCE"]

bot_meta = BotMetaClass(bot_cnf["token"], bot_cnf["admin"], bot_cnf["user"])
db_meta = DatabaseMetaClass(db_cnf["user"], db_cnf["password"], db_cnf["host"], int(db_cnf["port"]), db_cnf["db"])
binance_meta =Binance(binance_cnf["key"], binance_cnf["secret"], binance_cnf["symbol"])
bot_mn = Bot(bot_meta.token)


del binance_cnf
del bot_cnf
del db_cnf