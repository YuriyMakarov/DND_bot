from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from data.collections_of_keyboards import main_keyboard
from main_menu.def_keyboards import make_reply_keyboard

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
