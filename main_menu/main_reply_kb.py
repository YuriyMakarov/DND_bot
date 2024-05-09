from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def kb_main():
    buttons = ["Ваши персонажи", "Локации", "НПС", "Приключения", "Механики и снаряга"]
    builder = ReplyKeyboardBuilder()
    for item in buttons:
        builder.button(text=item)
    builder.adjust(1, 2, 1, 1)
    return builder.as_markup(resize_keyboard=True)
