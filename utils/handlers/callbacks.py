from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.menus import get_main_menu

router = Router()

@router.callback_query(F.data.startswith("mode:"))
async def set_mode(callback: CallbackQuery, state: FSMContext):
    mode = callback.data.split(":")[1]
    await state.set_state("waiting_for_prompt")
    await state.update_data(mode=mode)

    texts = {
        "chat": "normal ai chat mode on — talk anything! 🔥",
        "image": "want to generate image? send prompt (english best) 🎨",
        "code": "need code? tell language + what you want 💻",
        "translate": "translate text? mention language + text 🌐",
        "summarize": "summarize long text? paste here 📊"
    }
    text = texts.get(mode, "mode set! now send prompt.").lower()
    await callback.message.edit_text(text, reply_markup=get_main_menu())
    await callback.answer()

@router.callback_query(F.data == "help")
async def help_callback(callback: CallbackQuery):
    text = (
        "<b>help & commands</b>\n\n"
        "• /start — open menu\n"
        "• use buttons to change mode\n"
        "• normal chat: just type anything\n"
        "• image: send prompt for photo\n"
        "• code: ask programming questions\n"
        "• translate: convert text to another language\n"
        "• summarize: make long text short\n"
        "• new chat: clear previous conversation\n\n"
        "<i>powered by fast openai backend!</i>"
    ).lower()
    await callback.message.edit_text(text, reply_markup=get_main_menu())
    await callback.answer()

@router.callback_query(F.data == "new_chat")
async def new_chat(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    globals()['user_histories'][user_id] = []
    await state.clear()
    await callback.message.edit_text("new chat started! what’s up? 🚀".lower(), reply_markup=get_main_menu())
    await callback.answer()
