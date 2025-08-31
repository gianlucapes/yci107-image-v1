from pydantic import BaseSettings,Field
from langchain_google_genai import ChatGoogleGenerativeAI
from enum import Enum

class LargeLanguageModel(str, Enum):
    GEMINI_FLASH_2_5 = "gemini-2.5-flash"
    GEMINI_FLASH_2_5_IMAGE_PREVIEW = "gemini-2.5-flash-image-preview"

class Settings(BaseSettings):
    GOOGLE_API_KEY: str = Field(..., description="API key per Google Generative AI")
    MAX_TOKENS : int = 32_768


    class Config:
        env_file = ".env"  # carica variabili da file .env
        env_file_encoding = "utf-8"

settings = Settings()