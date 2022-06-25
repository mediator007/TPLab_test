from aiogram import Bot
from aiogram import Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('token')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())