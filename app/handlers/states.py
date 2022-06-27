from aiogram.dispatcher.filters.state import State, StatesGroup


class OrderDeals(StatesGroup):
    """
    Состояния для конечного автомата
    """
    waiting_for_screenshot = State()
    waiting_for_admin = State()
    