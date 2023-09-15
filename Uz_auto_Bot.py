import logging
import sys
import asyncio
from config import BOT_TOKEN
from aiogram import Dispatcher, Bot, types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from buttons import markup, chevrolet_cars, page_2

dp=Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(text="UzAuto ботга хуш келибсиз, керакли бўлимни танланг👇", reply_markup=markup)


@dp.callback_query(F.data=="prise_auto")
async def get_model_auto(call:types.CallbackQuery):
    await call.message.answer(text="Керакли  бӯлимни танланг ⬇️", reply_markup=page_2.as_markup())


@dp.callback_query(F.data=="chevrolet")
async def get_chevrolet_cars(call:types.CallbackQuery):
    await call.message.answer(text="Пастдаги рўйхатдан машинани танланг ⬇️", reply_markup=chevrolet_cars)


async def main():
    bot=Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped")