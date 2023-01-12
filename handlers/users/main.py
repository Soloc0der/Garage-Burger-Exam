from aiogram import types
from states.main_state import ShopState
from loader import dp, db
# from aiogram.dispatcher.storage import FSMContext
from keyboards.default.main_manu import *


@dp.message_handler(text="🍔 Бургер", state="*")
async def bot_echo(message: types.Message):
    await message.answer("Выберите пожалуйста", reply_markup=cat_burger)
    await ShopState.category.set()




@dp.message_handler(text="🌭 Хот-Дог", state="*")
async def bot_echo(message: types.Message):
    await message.answer("Выберите пожалуйста", reply_markup=cat_xoddog)
    await ShopState.category.set()



@dp.message_handler(text="🍗 Куриные крылышки(острые)", state="*")
async def bot_echo(message: types.Message):
    
    await message.answer("Выберите пожалуйста", reply_markup=cat_chicken_wings)
    await ShopState.category.set()

