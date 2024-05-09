from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from main_menu.main_reply_kb import kb_main

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=f"Здравствуйте, {message.from_user.full_name}",
                         reply_markup=kb_main())
