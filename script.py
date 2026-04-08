from aiogram import Bot, Dispatcher

bot = Bot(token = '8763198603:AAGfXly0jo29YlOgKvEiGesn36CgKCHd9-k')
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
