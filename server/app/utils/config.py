import os
from dotenv import load_dotenv

load_dotenv()

IMAGE_GENERATION_ENDPOINT = os.environ.get("IMAGE_GENERATION_ENDPOINT")
X_RAPID_API_KEY = os.environ.get("X_RAPID_API_KEY")
X_RAPID_API_HOST = os.environ.get("X_RAPID_API_HOST")
DEFAULT_IMAGE_SIZE = os.environ.get("DEFAULT_IMAGE_SIZE")
DEFAULT_IMAGE_COUNT = 1
