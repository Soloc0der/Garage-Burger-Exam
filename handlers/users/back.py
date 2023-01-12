from aiogram import types
from states.main_state import ShopState
from loader import dp, db
from aiogram.dispatcher.storage import FSMContext
from keyboards.default.main_manu import *


@dp.message_handler(text="⬅️ Назад", state=ShopState.category)
async def go_to_main_menu(message: types.Message):
    await message.answer("Выберите категорию", reply_markup=main_menu)
    
@dp.message_handler(text="⬅️ Назад", state=ShopState.product)
async def go_to_main_menu(message: types.Message):
    await message.answer("Выберите категорию", reply_markup=cat_burger)