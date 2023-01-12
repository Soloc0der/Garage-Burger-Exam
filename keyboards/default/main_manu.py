from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

main_menu.row("🍔 Бургер", "🌭 Хот-Дог")
main_menu.row("🍗 Куриные крылышки(острые)")
main_menu.row("🍹 Напитки", "🍟 Дополнительно")


back_button = KeyboardButton(text="⬅️ Назад")




cat_burger = ReplyKeyboardMarkup(resize_keyboard=True)
cat_burger.row("Бургер Классический", "Бургер Двойной")
cat_burger.add(back_button)


cat_xoddog = ReplyKeyboardMarkup(resize_keyboard=True)
cat_xoddog.row("🌭 Хот-Дог", "Хот-Дог Двойной")
cat_xoddog.add(back_button)



numbers = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

for num in range(1, 10):
    numbers.insert(KeyboardButton(text=str(num)))
numbers.add(back_button)


cat_drinks = ReplyKeyboardMarkup(resize_keyboard=True)
cat_drinks.row("Кола", "Фанта")
cat_drinks.row("Спрайт")
cat_drinks.add(back_button)

    

cat_extras = ReplyKeyboardMarkup(resize_keyboard=True)
cat_extras.row("Картошка Фри")
cat_extras.row("Фирминни Соус", "Кетчуп")
cat_extras.add(back_button)

