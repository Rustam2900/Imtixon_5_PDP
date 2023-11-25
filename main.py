import asyncio
import logging
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from routrs import router as all_routers

load_dotenv('.env')

router = Router()
router.include_router(all_routers)


async def main() -> None:
    bot = Bot(os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
    commans = [
        types.BotCommand(command="start", description="botga ishga tushurish uchun bosing")
    ]
    await bot.set_my_commands(commans)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
