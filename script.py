from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(token = '8763198603:AAGfXly0jo29YlOgKvEiGesn36CgKCHd9-k')
dp = Dispatcher()


@dp.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.from_user.id)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
