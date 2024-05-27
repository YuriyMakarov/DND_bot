import asyncio
import logging

from aiogram import Bot, Dispatcher

from tok import bot_tok
from main_menu import commands_handler
from characters import command_characters, message_classes


async def main():
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()
    bot = Bot(token=bot_tok)

    dp.include_router(commands_handler.router)
    dp.include_router(message_classes.router)
    dp.include_router(command_characters.router)
    # dp.include_router(add_product.router)
    # dp.include_router(delete_product.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
