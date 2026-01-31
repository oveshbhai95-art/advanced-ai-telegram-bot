from openai import AsyncOpenAI
from config import OPENAI_API_KEY, CHAT_MODEL, IMAGE_MODEL

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def get_chat_response(prompt: str, history: list) -> str:
    messages = history + [{"role": "user", "content": prompt}]
    response = await client.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages,
        temperature=0.7,
        max_tokens=2000,
    )
    return response.choices[0].message.content.strip()

async def get_image_url(prompt: str) -> str:
    try:
        response = await client.images.generate(
            model=IMAGE_MODEL,
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        return f"image error: {str(e)}"
