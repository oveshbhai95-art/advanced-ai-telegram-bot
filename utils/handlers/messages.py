from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.openai_helper import get_chat_response, get_image_url

router = Router()

@router.message(state="waiting_for_prompt")
async def handle_prompt(message: Message, state: FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()
    mode = data.get("mode", "chat")
    prompt = message.text.strip()

    if not prompt:
        await message.reply("write something bro!".lower())
        return

    thinking = await message.reply("<i>thinking... ⚡</i>".lower())

    try:
        history = globals()['user_histories'].get(user_id, [])
        if mode == "image":
            url = await get_image_url(prompt)
            if url.startswith("http"):
                await message.answer_photo(url)
                await thinking.delete()
                return
            resp = url
        else:
            if mode == "code":
                full_p = f"expert coder. write clean code with comments. task: {prompt}\nonly code + short explanation."
            elif mode == "translate":
                full_p = f"translate this text: {prompt} (assume english ↔ hindi if no language given)"
            elif mode == "summarize":
                full_p = f"make concise summary of this: {prompt}"
            else:
                full_p = f"helpful witty ai like grok. respond naturally. user: {prompt}"

            resp = await get_chat_response(full_p, history)

        history.append({"role": "user", "content": prompt})
        history.append({"role": "assistant", "content": resp})
        globals()['user_histories'][user_id] = history[-10:]

        await thinking.edit_text(resp.lower() or "something went wrong... try again!".lower())

    except Exception as e:
        await thinking.edit_text(f"error: {str(e)}\nwait a bit and try again.".lower())
