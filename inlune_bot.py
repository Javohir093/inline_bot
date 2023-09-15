# import logging
# import sys
# import asyncio
# from config import BOT_TOKEN
# from aiogram import Dispatcher, Bot, types, Router, F
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.filters.command import Command
# from buttons import get_id, burger

# dp=Dispatcher()

# @dp.message(CommandStart())
# async def command_start_handler(message: types.Message) -> None:
#     await message.answer(text=f"Hello, <b>{message.from_user.full_name}</b>!", reply_markup=get_id(message.from_user.id))

# @dp.callback_query(F.data=="burger")
# async def get_callback(call: types.CallbackQuery):
#     await call.answer(cache_time=1)
#     await call.message.edit_text("Burger tanlang\n1.Burger classic (25.000)\n2.Burger dvaynoy (32.000)", reply_markup=burger.as_markup())

# async def main():
#     bot=Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
#     await dp.start_polling(bot)

# if __name__=="__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print("Stopped")