import logging
from sys import exec_prefix
from aiogram import Bot, Dispatcher, executor, types
import wikipedia
wikipedia.set_lang('uz')
API_TOKEN = '5512033983:AAHUaKoZrpvrbMN1yN9mFvDkEcBrEUgXb30'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message:types.Message):
    await message.reply("Assalomu alekum Botimizga xush kelibsiz Bu bot Developer Umar tomonidan qilingan!!")
 

@dp.message_handler()
async def sendwiki(message : types.Message):
    try:
        response = wikipedia.summary(message.text)
        await message.answer(response)
    except:
        await message.answer("Normalniroq narsa yoz")

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)