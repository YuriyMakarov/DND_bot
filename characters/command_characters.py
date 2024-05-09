# @router.message(F.text == "Изобретатель")
# async def cmd_gid(message: Message):
#     await message.answer(text=f"/level - Прокачка\n"
#                               f"/ability - Классовые умения\n"
#                               f"/magic - Заклинания\n")
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

router = Router()


@router.message(Command("level_artificer"))
async def cmd_start(message: Message):
    photo = FSInputFile("materials//characters//artificer//level.png")
    await message.answer_photo(photo=photo, caption="Прокачка")


@router.message(Command("ability"))
async def cmd_start(message: Message):
    pass


@router.message(Command("magic"))
async def cmd_start(message: Message):
    pass

