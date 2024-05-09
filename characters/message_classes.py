from aiogram import Router, F
from aiogram.types import Message

router = Router()

# t = ["Бард", "Варвар", "Воин", "Плут",
#                "Волшебник", "Изобретатель",
#                "Друид", "Жрец", "Колдун", "Монах",
#                "Паладин", "Следопыт", "Чародей"]
#
# s = ["Прокачка", "Классовые умения", "Заклинания"]


@router.message(F.text == "Изобретатель")
async def cmd_gid(message: Message):
    await message.answer(text=f"/level_artificer - Прокачка\n"
                              f"/ability_artificer - Классовые умения\n"
                              f"/magic_artificer - Заклинания\n")
