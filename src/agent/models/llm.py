from langchain_google_genai import ChatGoogleGenerativeAI
from config import settings,LargeLanguageModel
from typing import Any

gemini_2_5_flash = ChatGoogleGenerativeAI(
    model=LargeLanguageModel.GEMINI_FLASH_2_5.value,
    api_key=settings.GOOGLE_API_KEY,
    temperature=1,
    max_tokens=settings.MAX_TOKENS,
    timeout=None,
    max_retries=2,
)

gemini_2_5_flash_image = ChatGoogleGenerativeAI(
    model=LargeLanguageModel.GEMINI_FLASH_2_5_IMAGE_PREVIEW.value,
    api_key=settings.GOOGLE_API_KEY,
    temperature=1.25,
    max_tokens=settings.MAX_TOKENS,
    timeout=None,
    max_retries=2,
)

class Model:
    def __init__(self):
        self.models : dict[str,Any] ={
            LargeLanguageModel.GEMINI_FLASH_2_5.value:gemini_2_5_flash,
            LargeLanguageModel.GEMINI_FLASH_2_5_IMAGE_PREVIEW.value:gemini_2_5_flash_image
        }
    
    def get_model(self,llm:LargeLanguageModel):
        return self.models.get(llm.value,{})
