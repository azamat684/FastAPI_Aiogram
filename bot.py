from aiogram import Dispatcher,Bot,types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
# btn = ReplyKeyboardMarkup(keyboard=[
#     KeyboardButton(text='salom')
# ],resize_keyboard=True)
TOKEN = "5610232641:AAGlvdgHIhB2yirOSgRLb-Ik5fiCvfyBbjU"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start",state="*")
async def start(message: types.Message):
    await message.answer("Assalomu alaykum!")


@dp.message_handler(text='salom')
async def echo(message: types.Message):
    await message.answer(message.text)
