from aiogram import Router
from aiogram.types import Message

echo_router = Router()


@echo_router.message()
async def echo(message: Message):
    await message.answer(message.text)
