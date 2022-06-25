from googletrans import  Translator
import logging
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5388266518:AAEpTaIdszhUXIodZRU35WMP0YalFKVZmZA'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
translator = Translator()

dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message:types.Message):
    await message.reply("Assalomu alekum Botimizga xush kelibsiz Bu bot Istalgan tildan o`zbek tiliga tarjima qilib beradi!!")
 
 
 

@dp.message_handler()
async def sendwiki(message : types.Message):
    try:
        detected = translator.detect(message.text).lang
        word = translator.translate(message.text, src=detected, dest='uz').text
        await message.answer(f'Siz kiritgan so`z ({detected}) tilida \nMa`nosi: " {word} " ')
    except:
        await message.answer("Kechirasiz xatolik yuz berdi. Qaytadan urinib ko`ring")

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)