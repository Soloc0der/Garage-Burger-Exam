from aiogram import types
from states.main_state import ShopState
from loader import dp, db
# from aiogram.dispatcher.storage import FSMContext
from keyboards.default.main_manu import *


@dp.message_handler(text="🍔 Бургер", state="*")
async def bot_echo(message: types.Message):
    await message.answer("Выберите пожалуйста", reply_markup=cat_burger)
    await ShopState.product.set()




@dp.message_handler(text="🌭 Хот-Дог", state="*")
async def bot_echo(message: types.Message):
    await message.answer("Выберите пожалуйста", reply_markup=cat_xoddog)
    await ShopState.product_xoddog.set()



@dp.message_handler(text="🍗 Куриные крылышки(острые)", state="*")
async def bot_echo(message: types.Message):
    
    await message.answer("Выберите пожалуйста", reply_markup=numbers)
    await ShopState.product_chiken.set()

@dp.message_handler(text="🍹 Напитки", state="*")
async def bot_echo(message: types.Message):
    await message.answer("Выберите пожалуйста", reply_markup=cat_drinks)
    await ShopState.product_drinks.set()



@dp.message_handler(text="🍟 Дополнительно", state="*")
async def bot_echo(message: types.Message):
    await message.answer("Выберите пожалуйста", reply_markup=cat_extras)
    await ShopState.product_another.set()









@dp.message_handler(text="Бургер Классический", state="*")
async def bot_echo(message: types.Message):
    await message.answer_photo(photo="http://mirpovara.ru/uploads/images/25/main/klassicheskij-burger.jpg", caption="<b>Baxosi: 15 000 so`m</b> \nTam va to`yimliligiga o`zingiz baxo bering", parse_mode="html", reply_markup=numbers)
    await ShopState.amount.set()








