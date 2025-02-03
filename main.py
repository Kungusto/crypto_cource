import asyncio
from aiogram import Dispatcher, Bot
import logging

from src.api.handlers import router
from tg_token import TOKEN

bot = Bot(token=TOKEN) 
dp = Dispatcher()

async def main() :
    await dp.start_polling(bot)
    
if __name__ == '__main__' :
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())