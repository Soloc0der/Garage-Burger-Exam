import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_manu import main_menu
from aiogram.dispatcher.storage import FSMContext
from states.main_state import ShopState
from data.config import ADMINS
from loader import dp, db, bot



@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"Здравствуйте,{name}!\nЭто бот службы доставки <b>Garage Burger</b>\nОтдел доставки работает 24/7\nВыберите пожалуйста. ", reply_markup=main_menu)
       
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"Здравствуйте,{name}!\nЭто бот службы доставки <b>Garage Burger</b>\nОтдел доставки работает 24/7\nВыберите пожалуйста. ", reply_markup=main_menu)
        await ShopState.category.set()