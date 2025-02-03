from aiogram import Router, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import asyncio

from src.services.parser import CryptoService
from tg_token import TOKEN

router = Router()


bot = Bot(token=TOKEN) 

async def daemon_crypto(chat_id) :
    while True : 
        await asyncio.sleep(1200)
        result = await CryptoService.get_current_data()
        await bot.send_message(chat_id, result)

@router.message(CommandStart())
async def start_message(message: Message) : 
    await message.answer('''👋 Привет! Я ваш виртуальный помощник по криптовалютам! 🚀

Здесь вы можете:

 - Узнать актуальные курсы популярных криптовалют 💰

 - Получить информацию о последних новостях в мире крипты 📰

 - Настроить уведомления о изменениях цен 🔔

 - Задать любые вопросы о криптовалютах и блокчейне ❓

 - Чтобы начать, просто выберите одну из команд ниже:
 
 /now - вывести весь список криптовалют и их курсов''')
    asyncio.create_task(daemon_crypto(message.chat.id))


@router.message(Command('now'))    
async def return_cources(message: Message) :
    result = await CryptoService.get_current_data()
    await message.answer(result) 