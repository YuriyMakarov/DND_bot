from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def kb_classes():
    buttons = ["Бард", "Варвар", "Воин", "Плут",
               "Волшебник", "Изобретатель",
               "Друид", "Жрец", "Колдун", "Монах",
               "Паладин", "Следопыт", "Чародей"]
    builder = ReplyKeyboardBuilder()
    for item in buttons:
        builder.button(text=item)
    builder.adjust(4, 2, 4, 3)
    return builder.as_markup(resize_keyboard=True)


# def kb_classes_info():
#     buttons = ["Прокачка", "Классовые умения", "Заклинания"]
#
#     builder = InlineKeyboardBuilder()
#     for i in range(len(buttons)):
#         builder.button(text=buttons[i], callback_data=f"class_{str(i)}")
#     builder.adjust(1, 1, 1)
#     return builder.as_markup(resize_keyboard=True)
