from aiogram import types,executor,Bot,Dispatcher
from req import send_answer

api='7123263232:AAFLJA-AsiuJl7EzLF2TdgCGnNy0IuF0I1s'
bot=Bot(api)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
               await message.answer('Bizge soraw jazip jiberin:')

@dp.message_handler()
async def save(message:types.Message):
        answer=await send_answer(message.text)
        await message.answer(answer)

if __name__=='__main__':
        executor.start_polling(dp,skip_updates=True)