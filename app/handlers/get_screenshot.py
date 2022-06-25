from aiogram import Dispatcher, types
from loguru import logger

from services.site_request import site_check, get_site_title
from handlers.states import OrderDeals


async def get_screenshot(message: types.Message):
    """
    Передаёт пользователю скриншот сайта по url
    """
    chat_id = message.from_user.id

    msg = await message.answer("Получение скриншота ...")

    url = message.text
    status_code = site_check(url)
    
    if status_code > 399: 
        await message.answer("Неверный ввод адреса или сайт недоступен")
        # await OrderDeals.waiting_for_screenshot.set()
        return
    
    title = get_site_title(url)
    await msg.edit_text(f"{url}")