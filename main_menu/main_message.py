from aiogram import Router, F
from aiogram.types import Message

from characters.keyboard_classes import kb_classes

router = Router()


@router.message(F.text == "Механики и снаряга")
async def cmd_gid(message: Message):
    await message.answer(text=f"Выберите класс", reply_markup=kb_classes())