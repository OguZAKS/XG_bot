from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_choice():
    buttons = [
        InlineKeyboardButton(text='статистика XG', callback_data='statXG'),
        InlineKeyboardButton(text='перейти к курсу ', callback_data='go_course'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def get_stat():
    buttons = [
        InlineKeyboardButton(text='получить статистику XG', callback_data='get_statXG'),
        InlineKeyboardButton(text='Назад', callback_data='back_stat'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard
