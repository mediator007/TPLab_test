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


def whois_inline_keyboard(url):
    """
    Create InlineKeyboardMarkup
    """
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    keyboard_markup.add(f'{url}', url=f'https://www.whois.com/whois/{url}')
    
    return keyboard_markup