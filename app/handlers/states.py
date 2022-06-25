from aiogram.dispatcher.filters.state import State, StatesGroup


class OrderDeals(StatesGroup):
    """
    Состояния для конечного автомата
    """
    waiting_for_ID = State()
    waiting_for_admindeals = State()
    waiting_for_modeldeals = State()
    waiting_for_model_add = State()
    waiting_for_model_delete = State()
    waiting_for_date = State()
    waiting_for_report = State()
    waiting_for_report_sum = State()