import asyncio
from aiogram import Bot
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup
from aiogram.types.bot_command import BotCommand
from loguru import logger

from config import dp, bot


async def bot_start(message: types.Message, state: FSMContext):
    """
    Первый запуск
    """
    await message.answer("Start text")


async def bot_help(message: types.Message, state: FSMContext):
    """
    Вызов справки по боту
    """
    await message.answer("Help text")


def register_handlers_deals(dp: Dispatcher):
    """
    Регистрация хэндлеров
    """
    dp.register_message_handler(callback=bot_start, commands="start", state="*")
    dp.register_message_handler(callback=bot_help, commands="help", state="*")


async def set_commands_model(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Перезапуск"),
        BotCommand(command="/help", description="Помощь"),
    ]
    await bot.set_my_commands(commands)


async def main():
    register_handlers_deals(dp)
    await set_commands_model(bot)
    await dp.start_polling()


if __name__ == '__main__':
    logger.add("bot_logger.log", format="{time} {level} {message}", level="INFO", rotation="1 MB")
    logger.info("Bot start")
    asyncio.run(main())