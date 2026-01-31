from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="💬 ai assist", callback_data="mode:chat"),
            InlineKeyboardButton(text="🖼️ image gen", callback_data="mode:image"),
        ],
        [
            InlineKeyboardButton(text="💻 code gen", callback_data="mode:code"),
            InlineKeyboardButton(text="❓ help", callback_data="help"),
        ],
        [
            InlineKeyboardButton(text="🔄 new chat", callback_data="new_chat"),
            InlineKeyboardButton(text="🌐 translate", callback_data="mode:translate"),
        ],
        [
            InlineKeyboardButton(text="📊 summarize", callback_data="mode:summarize"),
        ]
    ])
    return kb
