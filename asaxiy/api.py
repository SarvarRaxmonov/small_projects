import logging
from aiogram import Bot, Dispatcher, types

API_TOKEN = "5980978851:AAH8SF6Zk8pPje2jHmLn0IYdqTUMzYYsFco"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


