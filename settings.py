import os

class Settings:
    OPENAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
    SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
    SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")

    AUTH_TOKEN = os.getenv("API_AUTH_TOKEN")

settings = Settings()
