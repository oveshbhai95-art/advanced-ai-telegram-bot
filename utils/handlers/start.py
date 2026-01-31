from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from config import WELCOME_IMAGE
from keyboards.menus import get_main_menu
from pathlib import Path

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    if 'user_histories' not in globals():
        globals()['user_histories'] = {}
    globals()['user_histories'][user_id] = []

    caption = (
        "<b>🚀 welcome to advanced ai bot!</b>\n\n"
        "ask me anything — coding, images, translation, summaries or fun talks.\n\n"
        "<i>use buttons to select mode ↓</i>"
    ).lower()

    if Path(WELCOME_IMAGE).exists():
        await message.answer_photo(
            photo=FSInputFile(WELCOME_IMAGE),
            caption=caption,
            reply_markup=get_main_menu()
        )
    else:
        await message.answer(caption, reply_markup=get_main_menu())
