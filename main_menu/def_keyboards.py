from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def make_reply_keyboard(buttons: tuple, *adjust_params) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for item in buttons:
        builder.button(text=item)
    builder.adjust(*adjust_params)
    return builder.as_markup(resize_keyboard=True)
