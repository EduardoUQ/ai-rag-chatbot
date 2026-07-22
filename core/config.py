import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY no está configurada.")

OPENAI_MODEL = "gpt-4.1-mini"
TOP_K_RESULTS = 3