from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
import keyboards as kb
bot = Bot(token = '8763198603:AAGfXly0jo29YlOgKvEiGesn36CgKCHd9-k')
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Добро пожаловать в бот',
                         reply_markup=kb.menu)


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Вы написали команду /help')


@dp.message()
async def echo(message: Message):
    await message.answer('неизвестная комманда')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
