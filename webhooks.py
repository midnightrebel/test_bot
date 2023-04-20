import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN= '6053562119:AAFAtpy_8aUcXaiwxPUzP6BmiUUc26OrEqw'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
   await message.reply('Start')


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
   await message.reply('Вы обратились к справке бота')



executor.start_polling(dp, skip_updates=True)
