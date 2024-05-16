from mody import Mody
import logging

from aiogram import Bot, Dispatcher, executor, types
import random
from time import sleep
from func import *

API_TOKEN =Mody.ELHYBA,

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("اهلا بك في بوت زخرفه \n\n تم صنع هاذه البوت بواسطة @Rdthon \n\n البوت متكون من 25 نوع زخرفة🏻",  reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("⚙️ الاستخدام", switch_inline_query="ism")))


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery):
    text = inline_query.query or 'You'
    rs = []
    for i in make_nick(text):
        id = random.randint(1,2242252682114)
        i_van = types.InlineQueryResultArticle(
            id=id,
            thumb_url="https://telegra.ph/file/ceeb5762a3a7442436437.jpg",
            title=i,
            description=i,
            input_message_content=types.InputTextMessageContent(i),
        )
        rs.append(i_van)
    await inline_query.answer(results=rs, cache_time=1)


@dp.message_handler()
async def nick(message: types.Message):
    for i in make_nick(message.text):
        await message.answer(i)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)