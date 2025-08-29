import os

class Config:
    def __init__(self):
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        self.DEEP_LAKE_API_KEY = os.getenv("DEEP_LAKE_API_KEY")
        self.OTHER_CONFIG = os.getenv("OTHER_CONFIG", "default_value")  # Add other configurations as needed

    def validate(self):
        if not self.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
        if not self.DEEP_LAKE_API_KEY:
            raise ValueError("DEEP_LAKE_API_KEY is not set in the environment variables.")
        # Add more validation as needed

config = Config()