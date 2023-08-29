import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import register_start_handlers
from create_bot import dp,bot


register_start_handlers(dp)


async def on_startup(dp):
    await bot.send_message(5242177328, 'i am ready')


# Запускаем бота
if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
