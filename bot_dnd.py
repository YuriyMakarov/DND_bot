import asyncio
import logging

from aiogram import Bot, Dispatcher

from main_menu import commands_handler
from characters import command_characters, message_classes
from tools import calc_handlers


async def main():
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()
    bot = Bot(token="7255273514:AAFr0juF2PVIxtVB9_NDjBxladnoZpaBAvY")

    dp.include_router(commands_handler.router)
    dp.include_router(calc_handlers.router)
    dp.include_router(message_classes.router)
    dp.include_router(command_characters.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
