import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHAT_MODEL = "gpt-4o-mini"      # fast and good
IMAGE_MODEL = "dall-e-3"

WELCOME_IMAGE = "welcome.jpg"   # optional local file
