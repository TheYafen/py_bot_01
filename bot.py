from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("This message is from Bot")

@dp.message(Command("do"))
async def cmd_start(message: types.Message):
    await message.answer("Another command")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
