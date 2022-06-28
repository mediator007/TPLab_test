from aiogram import types
from handlers.data_structures import AdminButtons


def create_keyboard(buttons_obj: AdminButtons) -> types.ReplyKeyboardMarkup:
    """
    Create ReplyKeyboardMarkup markup for Admin
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for key, value in buttons_obj.__dict__.items():
        markup.add(value)
    return markup


def whois_inline_keyboard(url):
    """
    Create InlineKeyboardMarkup for WhoIs
    """
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(f'Who Is: {url}', url=f'https://www.whois.com/whois/{url}')
    keyboard_markup.row(button)
    return keyboard_markup