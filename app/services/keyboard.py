from aiogram import types
from handlers.data_structures import AdminButtons

def create_keyboard(buttons_obj: AdminButtons) -> types.ReplyKeyboardMarkup:
    """
    Create ReplyKeyboardMarkup markup
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons_obj:
        markup.add(button)
    return markup