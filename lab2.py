import logging
import random
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7855617855:AAGn9r2oeDahDE4PRFtVx4UYtbPJIAFz04w'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


user_data = {}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот-игра 'Угадай число'. Напиши /play чтобы начать.")

@dp.message_handler(commands=['play'])
async def play_game(message: types.Message):
    user_data[message.from_user.id] = random.randint(1, 100)
    await message.reply("Я загадал число от 1 до 100. Попробуй угадать!")

@dp.message_handler()
async def guess_number(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        await message.reply("Сначала напиши /play чтобы начать игру.")
        return

    try:
        guess = int(message.text)
    except ValueError:
        await message.reply("Пиши только числа!")
        return

    number = user_data[user_id]
    if guess < number:
        await message.reply("Больше!")
    elif guess > number:
        await message.reply("Меньше!")
    else:
        await message.reply("Угадал! Напиши /play чтобы сыграть снова.")
        del user_data[user_id]

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
