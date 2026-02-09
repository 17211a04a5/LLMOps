from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    API_PORT = int(os.getenv("API_PORT", 8000))
    ALLOWED_MODELS = ["llama3-70b-8192", "llama-3.3-70b-versatile"]

settings = Settings()