from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Выбрать язык')]
        [KeyboardButton(text='Изучать слова')]
        [KeyboardButton(text='Мой словарь')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню'
)