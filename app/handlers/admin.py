from aiogram import Dispatcher, types
from loguru import logger


from handlers.states import OrderDeals
from services.screenshot import screenshot
from config import bot
from database.db_requests import get_statistic


async def admin(message: types.Message):
    """
    Админка с возможностью получения статистики из бд
    """
    if message.text == admin_buttons.statistic:
        await message.answer("Запросы за сегодня:")
        
        result = get_statistic()
        
        for element in result:
            await message.answer('element[0]')
        logger.info('Запрос статистики администратором')
        return 
    elif message.text == admin_buttons.logout:
        await message.answer("Admin session close")
        logger.info('Сессия администратора завершена',reply_markup= types.ReplyKeyboardRemove())
        await OrderDeals.waiting_for_screenshot.set()
    else:
        await message.answer("Используйте клавиатуру для вызова команд")
        logger.warning(f'Неверная команда администратора: {message.text}')
        return