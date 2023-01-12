from aiogram.dispatcher.filters.state import State, StatesGroup


class ShopState(StatesGroup):
    category = State()
    product = State()
    product_burger = State()
    product_xoddog = State()
    product_chiken = State()
    product_drinks = State()
    product_another = State()
    amount = State()