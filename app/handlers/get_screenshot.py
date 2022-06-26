from aiogram import Dispatcher, types
from loguru import logger
from aiogram.types.input_file import InputFile
from aiogram.types.input_media import InputMedia

from services.site_request import site_check, get_site_title
from handlers.states import OrderDeals
from services.screenshot import screenshot
from config import bot


async def get_screenshot(message: types.Message):
    """
    Передаёт пользователю скриншот сайта по url
    """
    user_id = message.from_user.id

    # msg = await message.answer("Получение скриншота ...")
    
    file_path = "/home/viktor/Desktop/TPLab_test/app/services/media/loading.png"
    file = InputFile(file_path)
    msg = await bot.send_photo(chat_id=user_id, photo=file, caption="Получение скриншота ...")

    url = message.text
    status_code = site_check(url)
    
    if status_code > 399: 
        await message.answer("Неверный ввод адреса или сайт недоступен")
        # await OrderDeals.waiting_for_screenshot.set()
        return
    
    title = get_site_title(url)
    file_name, time = screenshot(url, user_id)
    file_name = "/home/viktor/Desktop/TPLab_test/app/services/media/spinner.png"
    file = InputMedia(media=InputFile(file_name), caption=f"{title}, {url}, {time:.2f} сек")

    await msg.edit_media(file)