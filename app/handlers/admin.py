from aiogram import Dispatcher, types
from handlers.states import OrderDeals
from services.screenshot import screenshot
from config import bot
from database.db_requests import get_statistic
from loguru import logger


async def admin(message: types.Message):
    """
    Админка с возможностью получения статистики из бд
    """
    if message.text == 'Statistic':
        await message.answer("Запросы за сегодня:")
        
        result = get_statistic()
        
        for element in result:
            await message.answer('element[0]')
        logger.info('Запрос статистики администратором')
        return 
    elif message.text == 'LogOut'
        await message.answer("Admin session close")
        logger.info('Сессия администратора завершена')
        await OrderDeals.waiting_for_screenshot.set()
    else:
        await message.answer("Use buttons")
        logger.warning('Неверная команда администратора')
        return