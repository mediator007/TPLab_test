import os

from aiogram import types
from loguru import logger
from aiogram.types.input_file import InputFile
from aiogram.types.input_media import InputMedia
from dotenv import load_dotenv

from services.site_request import site_check, get_site_title
from handlers.states import OrderDeals
from handlers.data_structures import AdminButtons
from services.screenshot import screenshot
from services.keyboard import create_keyboard, whois_inline_keyboard
from config import bot
from database .data_structures import ScreenshotStatistic
from database.db_requests import create_row

load_dotenv()

ADMIN_PASS = os.getenv('admin_pass')

admin_buttons = AdminButtons(
    statistic='получить статистику',
    logout='выйти'
)

async def get_screenshot(message: types.Message):
    """
    Функционал пользователя: запрос скриншота, начала сессии администратора
    по паролю, занесение статистики в бд
    """
    # Check input text for admin password
    # If true - admin session begin
    if message.text == ADMIN_PASS:
        markup = create_keyboard(admin_buttons)
        await message.answer("Сессия администратора", reply_markup=markup)
        logger.info('Начата сессия администратора')
        await OrderDeals.waiting_for_admin.set()
    # If message not admin pass - send default answer
    else:
        user_id = message.from_user.id
        
        file_path = "./app/services/media/loading.png"
        file = InputFile(file_path)
        msg = await bot.send_photo(chat_id=user_id, photo=file, caption="Получение скриншота ...")

        # Check site response
        url = message.text
        status_code = site_check(url)
        logger.info(f"status code: {status_code}")
        
        if status_code > 399: 
            await message.answer("Неверный ввод адреса или сайт недоступен")
            logger.warning(f'Сайт недоступен. Введен url: {url}')
            return
        # Get site title
        title = get_site_title(url)
        # Make screenshot and return file_name and request time
        file_name, time = screenshot(url, user_id)
        # If screenshot save in dir - prepare data for edit default message
        if os.path.exists(file_name):
            file = InputMedia(media=InputFile(file_name), caption=f"{title}, {url}, {time:.2f} сек")
            # send statisctic to db
            row = ScreenshotStatistic(
                url=url,
                user_id=user_id,
            )
            create_row(row)

            logger.info(f'Скриншот отправлен. {title}, {url}, {time:.2f} сек')
            # Edit default message
            await msg.edit_media(file, reply_markup=whois_inline_keyboard(url))
            return
        else:
            await message.answer("Что-то пошло не так. Попробуйте снова!")
            return
    