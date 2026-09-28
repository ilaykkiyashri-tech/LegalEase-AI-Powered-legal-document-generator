import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
LOGO_PATH = os.getenv("LOGO_PATH", "Image/Logo.png")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
