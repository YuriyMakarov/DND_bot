from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards import make_reply_keyboard, main_keyboard

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text=f"Dungeons&Dragons:\n"
             f"Здесь основная информация о Dungeons&Dragons\n"
             f"______________________________________________________\n"
             f"Миры:\n"
             f"Лор доступных миров мастеров\n"
             f"______________________________________________________\n"
             f"Инструменты:\n"
             f"Инструменты для расчетов различных механик\n"
             f"______________________________________________________\n"
             f"Лист персонажей:\n"
             f"Набор сведений об ваших игровых персонажей",
        reply_markup=make_reply_keyboard(main_keyboard, 1, 1, 1, 1)
    )


@router.message(Command(commands=["h", "help"]))
async def cmd_help(message: Message):
    await message.answer(
        text="Доступные команды:\n"
             "/start"
             "/help или /h"
    )
